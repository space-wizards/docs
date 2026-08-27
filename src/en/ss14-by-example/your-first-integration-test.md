# Your First Integration Test

In this guide you will learn about SS14 integration testing and how to create an integration test.

### What is integration testing?

**Integration testing** is ensures that changes to one part of the game don't unexpectedly cause another part of the game to change too.
It can catch unintended behavior, bugs and even rare game-crashing errors when used properly!
Integration testing is performed through the use of **integration tests**, which basically run short simulations of the game and make sure the end results of those simulations match what the test expects.

An example would be changing a Cargo order to cost less. If this change would end up making the order cost less than it would to sell it, players could just repeatedly buy and resell the order to generate infinite money! 
If you have an integration test that compares order costs to sell values, you'll be able to automatically catch if the change results in an infinite money loop!

Integration tests are automatically run on all pull requests submitted to the SS14 repository, and all tests must pass for a PR to be mergeable.
You can also run tests locally in your IDE (useful if you fail a specific test when submitting a PR). Most IDEs have a dedicated "Tests" view that allows you to select tests to run and view results: [JetBrains Rider](https://www.jetbrains.com/help/rider/Reference_Windows_Unit_Tests.html); [Visual Studio](https://learn.microsoft.com/en-us/visualstudio/test/run-unit-tests-with-test-explorer?view=visualstudio); [VSCode](https://code.visualstudio.com/docs/debugtest/testing). 

### The structure of a test

Tests generally follow this flow:

- Select which base test class the test should use.
- Define test-specific prototypes & settings.
- Spawn entities and retrieve components/systems to test.
- Assert default values (i.e. "are the starting values what I expect?").
- Run the test scenario.
- Assert that values have changed (i.e. "did the test result in what I expected?").
- Clean up the test environment if necessary.

We will go through this flow in the tutorial below.

## Making your first test

In this tutorial we are going to make a test to check that hugging works.
Hugging is done via `InteractionPopupSystem` using entities with a `InteractionPopupComponent`.
When a hug is performed, the `LastInteractTime` datafield of the user's `InteractionPopupComponent` should get updated to a new value. 

We decide our test will try to simulate a hug and then verify that it happened by checking if `LastInteractTime` updated.

### Setup

Integration tests are created in a relevant area folder in `Content.IntegrationTests/Tests`, so we create a new folder `InteractionPopup` and a new C# script `InteractionPopupTest`.

Our first decision will be to choose which base test class to use.
These are used to handle boilerplate code all tests should run (e.g. setting up and disposing of finished tests) and enable specific functionalities (such as spawning a default player mob or a walkable grid).
Some choices include `GameTest`, `InteractionTest` and `MovementTest`.

For our test, we will use `InteractionTest` as our base class.
It spawns a simple player mob with a single hand and has a lot of helper functions related to interactions that we can make use of later:
```
using Content.IntegrationTests.Tests.Interaction;

namespace Content.IntegrationTests.Tests.InteractionPopup;

public sealed class InteractionPopupTest : InteractionTest
{

}
```
We will also create the method inside of which our test is run, `HugTest()`. The method requires two properties:
- A `[Test]` attribute, to mark the method as a test.
- The `async` keyword, since the test simulation will run alongside other tests, and some behaviors (such as spawning) will take time to run.
```
using Content.IntegrationTests.Tests.Interaction;

namespace Content.IntegrationTests.Tests.InteractionPopup;

public sealed class InteractionPopupTest : InteractionTest
{

  [Test]
  public async Task HugTest()
  {

  }
}
```
With this, the test should now be visible in the Tests tab of your IDE!
Exactly where the Tests tab is located depends on the IDE you use, but once found you should be able to see `InteractionPopupTest` among the other test folders. If you can't see it, you may need to rebuild your solution first.

You can even run the test if you want, though since the test is empty it will always return a Success.

### Spawning an entity
Since `InteractionTest` handles spawning the player mob automatically, our first actual step in creating the test will be to spawn in the mob we will hug. We have two options here:

- Rely on an existing mob prototype with `InteractionPopupComponent`.
- Create a dummy prototype inside the test class to only use for this test.  

We will choose the first one since the `MobHuman` prototype is a base mob that we expect will always be huggable, and using it additionally makes the test keep an eye on if that prototype ever accidentally gets changed.

`InteractionTest` has a built-in spawning method `SpawnTarget`, which spawns an entity one tile next to the player entity and sets it as the target for any future interactions of the player entity.

```
private static readonly EntProtoId _humanPrototype = "MobHuman";

[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget(_humanPrototype);
}
```

### Checking for components

`InteractionTest` has a helper method to get the server component: `Comp<T>(NetEntity? target)`. This also checks that the component exists on the entity, and fails the test if it doesn't.

```
private static readonly EntProtoId _humanPrototype = "MobHuman";

[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget(_humanPrototype);
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);
}
```

### Asserts

What we want to do is *assert* that the property has the value we expect it to have, and if it doesn't the test should fail.
The `Assert` class enables this, with the method [`Assert.That`](https://docs.nunit.org/articles/nunit/writing-tests/assertions/assertion-models/constraint.html) being the preferred method of evaluating property values. 

`InteractionPopupComponent` has the property `LastInteractTime`, and while we can *assume* that it will always start at the default value, core to testing is never assuming if you can test it. We can check this with `Is.Default`.

```
private static readonly EntProtoId _humanPrototype = "MobHuman";

[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget(_humanPrototype);
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);

    Assert.That(interactionPopupComp.LastInteractTime, Is.Default);
}
```

### Simulation & Checking

`InteractionTest` has many helper methods used for simulating interactions.
With our testcase being simply clicking on the huggable entity, we can use the basic `await Interact();` method to simulate hugging. Since we spawned the `MobHuman` with `SpawnTarget` earlier, all we have to do is run the method, which will use the `Target` as default!

Since the player entity spawns with one free hand, we should expect a basic interaction to result in the `InteractionPopupSystem.InteractHandEvent` event subscription triggering, and therefore `LastInteractTime` should be updated to the current time. We assert that the previous `LastInteractTime` should not be equal to the new `LastInteractTime`. 

```
private static readonly EntProtoId _humanPrototype = "MobHuman";

[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget(_humanPrototype);
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);

    Assert.That(interactionPopupComp.LastInteractTime, Is.Default);

    var previousInteractTime = interactionPopupComp.LastInteractTime;

    await Interact(); // Perform the hug!

    Assert.That(interactionPopupComp.LastInteractTime, !Is.EqualTo(previousInteractTime));
}
```

If you run the `HugTest()` test now, it should pass!
If any future changes accidentally makes another empty-handed action override hugging, this test will now be able to catch that. You made your first test!

### Clean-up & Recycling

To make integration tests run fast and efficiently, the testing system is set up to save time by reusing servers, clients and entity systems across multiple tests.
Much of this is handled automatically under the hood. `TestPair`, a class used to facilitate the test simulation, deletes the test map and any entities in it when a test has finished. There may however be instances where you will have to clean up manually.

An example would be spawning entities in nullspace; since that is a different map to the one set up via `GameTest`, any such entities should be tracked and deleted at the end of the test to prevent accidentally leaking their behavior into the next test being run.
There are some helper functions that assist with this, such as `GameTest.SSpawn` that spawns a server-side entity and adds it to an internal tracking list.

Sometimes it might not be viable to do all the clean-up manually, such as when there are extensive round changes like running multiple game rules. In such cases a test can be marked as Dirty. This indicates to the underlying manager that the simulated server and client should be disposed of and restarted before the next test. Be aware that this makes testing take longer and should only be done if necessary!

```
// Simply add this override to the start of the test class to mark it as Dirty.
public override PoolSettings PoolSettings => new PoolSettings
{
    Dirty = true
};
```

Luckily, our test is simple enough that letting the test handle map deletion and clean-up automatically should be sufficient.

This tutorial only brushes the surface of how tests can be made.
The test can expand to cover trying to hug with an item in the player's hand, hugging all different player species, checking that hugs don't come out faster than the cooldown and much more. It is recommended that you look at existing tests in the repository to get an idea of the different ways a test can be ran.

## Extra Credit: How Do Tests Work Under The Hood?

There is a lot going into the setup of integration testing that the test base classes do automatically when initialized.
It can be good to understand this process since a lot can be modified and extended, and there are several helper methods that can save time and make your tests much better.

`PoolManager` is a static core class that manages server-client simulation relationships, and is used for tests, benchmarks and map rendering.
For tests specifically it allows for server-clients to be reused for multiple tests and for tests to be run in parallel, instead of constantly starting and shutting down such systems. This ends up becoming a massive time save over the course of several tests.

It's unlikely you will access `PoolManager` yourself, but a key property that all integration tests make use of is the `TestPair` class.
`TestPair` gives you access to the Client and Server instances and therefore the ability to set CVars, resolve manager/system dependencies and map management.
The test base classes all make use of this to create helper methods and properties.

It is strongly recommended you check out `GameTest.Entities.cs`, `GameTest.Pair.cs` `InteractionTest.Helpers.cs`, `Pair/TestPair.Helpers.cs` and `Pool/TestPair.Helpers.cs` to see what helper methods are available!
