# Your First Integration Test

In this guide you will learn about integration testing and how to create an integration test.

### What is integration testing?

**Integration testing** is a useful tool to ensure that changes to one part of the game doesn't unexpectedly cause another part of the game to change too.
It can catch unintended behavior, bugs and even rare game-crashing errors when used properly!
This is achieved through **integration tests**, which basically run short simulations of the game and makes sure ingame values match what the test expects.

An example would be changing a Cargo order to cost less.
If you have an integration test that compares order costs to sell values, you'll be able to automatically catch if this change would result in an infinite money loop!

Integration tests are ran on all pull requests submitted to the SS14 repository and all tests must pass for a PR to be mergeable.
You can also run tests locally in your IDE (useful if you fail a specific test when submitting a PR).

### The structure of a test

Tests generally follow this flow:

- Select which base test class the test should use.
- Define test-specific prototypes & settings.
- Spawn entities and retrieve components/systems to test.
- Assert default values (i.e. "are the starting values what I expect?").
- Do the test scenario.
- Assert that values have changed (i.e. "did the test result in what I expected?").

We will go through this flow in the tutorial below:

## Making your first test

In this tutorial we are going to make a test to check that hugging works.
Hugging is done via `InteractionPopupSystem` and `InteractionPopupComponent`, and when a hug is performed `InteractionPopupComponent.LastInteractTime` should get updated to a new value. 

We decide our test will try to simulate a hug and then verify that it happened by checking if `LastInteractTime` updated.

### Setup

Integration tests are created in a relevant area folder in `Content.IntegrationTests/Tests`, so we create a new folder `InteractionPopup` and a new C# script `InteractionPopupTest`.

Our first decision will be to choose which base test class to use.
These are used to handle boilerplate (e.g. setting up and disposing of finished tests) and enable specific functionalities (such as spawning a default player mob or a walkable grid).
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
Exactly where the Tests tab is located depends on the IDE you use, but if once found you should be able to see `InteractionPopupTest` among the other test folders.
You can even run the test if you want, though since the test is empty it will just return a Success.

### Spawning an entity
Since `InteractionTest` handles spawning the player mob automatically, our first actual step in creating the test will be to spawn in the mob we will hug. We have two options here:

- Rely on an existing mob prototype with `InteractionPopupComponent`.
- Create a dummy prototype inside the test class to only use for this test.  

We will choose the first one since the `MobHuman` prototype is a base mob that we expect will always be huggable, and using it additionally makes the test keep an eye on if that prototype ever accidentally gets changed.

`InteractionTest` has a built-in spawning method `SpawnTarget`, which spawns an entity one tile next to the player entity and sets it as the target for any future interactions of the player entity.

```
[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget("MobHuman");
}
```

### Checking for components

`InteractionTest` has a helper method to get the server component: `Comp<T>(NetEntity? target)`. This also checks that the component exists on the entity, and fails the test if it doesn't.

```
[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget("MobHuman");
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);
}
```

### Asserts

What we want to do is *assert* that the property has the value we expect it to have, and if it doesn't the test should fail.
The `Assert` class has several methods for this, but the most common is `Assert.That` which allows comparing values of properties. 

`InteractionPopupComponent` has the property `LastInteractTime`, and while we can *assume* that it will always start at the default value, core to testing is never assuming if you can test it. We can check this with `Is.Default`.

```
[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget("MobHuman");
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);

    Assert.That(interactionPopupComp.LastInteractTime, Is.Default);
}
```

### Simulation & Checking

`InteractionTest` has many helper methods used for simulating interactions.
With our testcase being simply clicking on the huggable entity, we can use of the basic `await Interact();` method to simulate hugging. Since we spawned the `MobHuman` with `SpawnTarget` earlier, all we have to do is run the method!

Since the player entity spawns with one free hand, we should expect a basic interaction to result in the `InteractionPopupSystem.InteractHandEvent` event subscription triggering, and therefore `LastInteractTime` should be updated to the current time. We assert that the previous `LastInteractTime` should not be equal to the new `LastInteractTime`. 

```
[Test]
public async Task HugTest()
{
    var urist = await SpawnTarget("MobHuman");
    var interactionPopupComp =  Comp<InteractionPopupComponent>(urist);

    Assert.That(interactionPopupComp.LastInteractTime, Is.Default);

    var previousInteractTime = interactionPopupComp.LastInteractTime;

    await Interact(); // Perform the hug!

    Assert.That(interactionPopupComp.LastInteractTime, !Is.EqualTo(previousInteractTime));
}
```

If you run the `HugTest()` test now, it should pass!
If any future changes accidentally makes another empty-handed action override hugging, this test will now be able to catch that. You made your first test!

This tutorial only brushes the surface of how tests can be made.
The test can expand to cover trying to hug with an item in the player's hand, hugging all different player species, checking that hugs don't come out faster than the cooldown and much more.
