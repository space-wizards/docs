# Running Tests

It's very important to Space Station 14 that things are _tested_. It would wreck someone's experience for their game to not work or flat out crash. Worst case scenario, a bug could even leave players open to exploits and malware.

As well as that, you don't want your PR to magically fail during CI and not get merged. You should always test it before pushing!

To deal with this, there are three types of tests that are implemented through SS14 & RobustToolkit's codebase:

1. **Unit Tests**, that test specific methods and their results
2. **Integration Tests**, that tests how the whole system integrates together
3. **Linters**, that makes sure that certain files follow the rules

## Unit Tests

Unit Tests are tests that are made to test a specific method or subsystem. 

To execute the tests, run:

```bash
dotnet test --configuration DebugOpt Content.Tests -- NUnit.ConsoleOut=0
```

The flags explained are:
- `--no-build`: Don't build the game because we don't need to.
- `--configuration DebugOpt`: This tells the test runner to build the project as DebugOpt.
- `Content.Tests/Content.Tests.csproj`: Tells it to run the unit tests.
- `-- NUnit.ConsoleOut=0`: Tells NUnit to throw away all of the stdout instead of putting it in your face.  

To write an integration test, you follow the [Microsoft NUnit guide](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-nunit#creating-the-first-test). 

## Integration Tests

Integration Tests are the real meat and potatoes that SS14 relies on. These test larger systems and how they interact across the client-server boundary.

To execute the integration tests, run:

```bash
dotnet test -e COMPlus_gcServer=1 --configuration DebugOpt Content.IntegrationTests -- NUnit.ConsoleOut=0 NUnit.MapWarningTo=Failed
```

The new flags are:
- `-e COMPlus_gcServer=1`: This tells .NET to use the [Server GC](https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/workstation-server-gc) and thus greatly increases the speed of integration tests.
- `NUnit.MapWarningTo=Failed`: Turns all warnings into test failures

### Writing Integration Tests

Now, to actually write an Integration Test, you first have to understand the directory structure of the project:

1. `Content.IntegrationTests` is broken into two parts: 
    - `Tests` (where tests are stored) 
    - `Pairs` (where the backend for server + client testing is implemented).
2. Now inside of `Tests`, there's a bunch of subdirectories and folders for testing specific subsystems.

Now to actually write an integration test, you follow the [Microsoft NUnit guide](https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-with-nunit#creating-the-first-test).

``````admonish example title="Example Integration Test" collapsible=true

```cs
using Content.Client.Chemistry.UI;
using Content.IntegrationTests.Tests.Interaction;
using Content.Shared.Chemistry;
using Content.Server.Chemistry.Components;
using Content.Shared.Containers.ItemSlots;
// NUnit is auto imported, see Content.IntegrationTests/GlobalUsings.cs

namespace Content.IntegrationTests.Tests.Chemistry;

public sealed class DispenserTest : InteractionTest
{
    /// <summary>
    ///     Basic test that checks that a beaker can be inserted and ejected from a dispenser.
    /// </summary>
    [Test]
    public async Task InsertEjectBuiTest()
    {
        await SpawnTarget("ChemDispenser");
        ToggleNeedPower();

        // Insert beaker
        await InteractUsing("Beaker");
        Assert.That(Hands.ActiveHandEntity, Is.Null);

        // Open BUI
        await Interact();

        // Eject beaker via BUI.
        var ev = new ItemSlotButtonPressedEvent(SharedReagentDispenser.OutputSlotName);
        await SendBui(ReagentDispenserUiKey.Key, ev);

        // Beaker is back in the player's hands
        Assert.That(Hands.ActiveHandEntity, Is.Not.Null);
        AssertPrototype("Beaker", SEntMan.GetNetEntity(Hands.ActiveHandEntity));

        // Re-insert the beaker
        await Interact();
        Assert.That(Hands.ActiveHandEntity, Is.Null);

        // Re-eject using the button directly instead of sending a BUI event. This test is really just a test of the
        // bui/window helper methods.
        await ClickControl<ReagentDispenserWindow>(nameof(ReagentDispenserWindow.EjectButton));
        await RunTicks(5);
        Assert.That(Hands.ActiveHandEntity, Is.Not.Null);
        AssertPrototype("Beaker", SEntMan.GetNetEntity(Hands.ActiveHandEntity));
    }
}
```

Source: [`Content.IntegrationTests/Tests/Chemistry/DispenserTest.cs`](https://github.com/space-wizards/space-station-14/blob/5e51a1d73c3a90438969b8100a32e43e44a5a5fb/Content.IntegrationTests/Tests/Chemistry/DispenserTest.cs)

``````

## Linter

Linters are programs that browse through files and warn when something is wrong, like a stylistic or syntactic error. These help verify that all the code sent upstream would be read correctly and won't silently break.

There's actually many different linters that SS14 uses, some of which are:

- **RSI**, which verifies all of the `meta.json` files are correct and use valid properties.
- **YAML**, which verifies all the YAML is correctly formed.

### RSI Verifier

To verify that all of the RSI is good, you need to:

1. Install of the dependencies 
    ```bash
    pip3 install jsonschema
    ```
2. Run the script  
    ```bash
    python3 RobustToolbox/Schemas/validate_rsis.py Resources
    ```

### YAML Linter

To verify that YAML is working, you need to run:

```bash
dotnet run --project Content.YAMLLinter
```