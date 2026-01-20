# PR Guidelines
This document states the guidelines for submitting changes to Atmospherics.
Similar to but different from the project's Coding Conventions, atmoscode has special considerations that should be followed when making new features or writing bugfixes.

```admonish question "But why?"
Atmospherics has been in a rough state. It has been through several refactors, both by its original SS14 creator, and by other maintainers following suit.

Major changes have been made that have silently broken core atmospherics features, which have impacted the overall game negatively to a point where poor design decisions were made to counteract the percieved effects.

A recent effort is being undergone by Maintainers (mainly just me, Roomba) to fully redocument and write tests for Atmospherics.
As such, these guidelines represent all of the lessons I have learned so far in fixing, maintaining, and expanding Atmospherics.
```

## General Coding Conventions
### Re-assertions
You should be familiar with the projects Coding Conventions and their core tenants of:
- **Do not copy-paste code.**
- **Do not use magic strings/numbers.**
- **Comment your code's purpose fully, don't just comment what it does.**

### All members must be documented regardless of access level
All code should be documented, even `private` members, even if they are simple helper methods or datafields.

This greatly assists maintainers in reviewing your code, and helps contributors establish the bigger picture on how Atmospherics functions.

Generally, public-facing methods should have a proper summary, parameter documentation, caveats to consider, method return documentation if applicable, as well as an example if applicable. Extending this level of documentation to `private` members is appreciated.

```C#
/// <summary>
/// Calculates the dimensionless fraction of gas required to equalize pressure between two gas mixtures.
/// </summary>
/// <param name="gasMixture1">The first gas mixture involved in the pressure equalization.
/// This mixture should be the one you always expect to be the highest pressure.</param>
/// <param name="gasMixture2">The second gas mixture involved in the pressure equalization.</param>
/// <returns>A float (from 0 to 1) representing the dimensionless fraction of gas that needs to be transferred from the
/// mixture of higher pressure to the mixture of lower pressure.</returns>
/// <remarks>
/// <para>
/// This properly takes into account the effect
/// of gas merging from inlet to outlet affecting the temperature
/// (and possibly increasing the pressure) in the outlet.
/// </para>
/// <para>
/// The gas is assumed to expand freely,
/// so the temperature of the gas with the greater pressure is not changing.
/// </para>
/// </remarks>
/// <example>
/// If you want to calculate the moles required to equalize pressure between an inlet and an outlet,
/// multiply the fraction returned by the source moles.
/// </example>
public float FractionToEqualizePressure(GasMixture gasMixture1, GasMixture gasMixture2) {...}
```

### Subsystems should reside in their own partial class
Subsystems refer to the routines that Atmospherics performs during an update.
These are the big processing states, like `Revalidate`, `TileEqualize`, `ExcitedGroups`, `DeltaPressure`, etc.

Most of the logic relating to these subsystems should reside in their own partial class in `AtmosphereSystem` under the format `AtmosphereSystem.<Subsystem>.cs`.

Any `[Dependency]` imports should reside in the root `AtmosphereSystem` partial.
Any `const`s or private fields that are heavily used or control configuration for said subsystem should reside in the subsystem's partial class.
If these `const` fields are useful on the client, they should belong in the `Atmospherics` static class.

### Avoid god methods when possible
Do not have a horrifyingly long (ex. 350+ LOC) method that performs the bulk of your subsystem logic.
Split your method up into distinct processing steps that your main method calls.

This may allow you to turn your helper method into generic methods that can be called throughout Atmospherics.
For example, if you've derived a useful mathematical function that assists in equalizing pressure between two `GasMixture`s, make that a public method that systems can call in `AtmosphereSystem.API`.

### Mathematical derivations must be properly documented
Documentation should be provided for your mathematical derivations for any functions you made.

The documentation should be embedded in the code as a multi-line comment and be formatted in a semi-readable way.
Pseudo-LaTeX notation is preferred.

While self-documenting variable named and single-line comments on each step is always desired, a general overview on the steps you took to reach your solution is preferred. 

```C#
public float FractionToEqualizePressure(GasMixture gasMixture1, GasMixture gasMixture2)
{
    /*
    Problem: the gas being merged from the inlet to the outlet could affect the
    temp. of the gas and cause a pressure rise.
    We want the pressure to be equalized, so we have to account for this.

    For clarity, let's assume that gasMixture1 is the inlet and gasMixture2 is the outlet.

    We require mechanical equilibrium, so \( P_1' = P_2' \)

    Before the transfer, we have:
    \( P_1 = \frac{n_1 R T_1}{V_1} \)
    \( P_2 = \frac{n_2 R T_2}{V_2} \)

    After removing fraction \( x \) moles from the inlet, we have:
    \( P_1' = \frac{(1 - x) n_1 R T_1}{V_1} \)
    
    [...]
```

### New additions should have tests
Whether it be a new API method or a new Atmospherics feature, the implementation should have tests that properly cover the changes.
Tests are invaluable for Atmospherics, as most of it is untested, and indirect changes have significantly disrupted core mechanics before.

There is an available test helper class `AtmosTest` that can help you write tests for your feature.

### Performance improvements should be demonstrated by a benchmark
It has been proven multiple times (via my own performance improvement attempts, and others as well) that some performance changes have little to no impact.

This is unfortunate as most performance changes made the code more complicated and hard to read, whether it be via multithreading, branchless code, or vectorized code.

As such, all performance improvements should be demonstrated by a benchmark.
You'll find that this is effectively required for meaningfully iterating on any performance goal you'd like to achieve.
It also greatly helps out future contributors trial out their own performance tweaks, and reduces hypothetical-posting for content changes that may decrease performance.

### Do not hide potential numerical instability or noise
When writing code for Atmospherics, do not ignore potential numerical instability, as this could hide bad edge-cases during testing or during gameplay.
For example, if dividing a `HeatContainer` into $n$ parts, ensure that $n$ is a `uint` and use `ArgumentOutOfRangeException` helpers to throw if $n = 0$:

```C#
public static HeatContainer[] Divide(this HeatContainer c, uint num)
{
    ArgumentOutOfRangeException.ThrowIfZero(num);

    var fraction = 1f / num;
    [...]
```

If your numerical method has natural numerical instability that shouldn't be seen in gameplay (ex. an exploded exponential), be sure to either clamp the potential value to a known range of good values, or fall back to a more stable method, all while logging an error to keep track.

Unchecked numerical instability leads to more painful debugging as the problem propagates down the call stack.
This can easily cause long simulation stages in Atmospherics to blow up.

If you make an assumption in your code (ex. skipping a nullcheck because you know that your data is not null), be sure to:
- Debug assert (`DebugTools.Assert` or `DebugTools.AssertNotNull`) your condition.
- Demonstrate that whatever logic you skip is worth skipping using a benchmark.

### Large features or processing states should be as configurable as possible
When adding a new large feature, ensure that the specific processing state can be disabled via a CVAR.

`const` values that aren't performance critical or shouldn't be changed often can be made into a CVAR.

This allows forks to enable, disable, or otherwise configure certain Atmospherics stages to their liking.
A fork shouldn't have to pull out the entire subsystem if they want to disable it.

### Don't tack on major features to an existing processing state
When adding new behavior for a processing state, ensure that you are not effectively hardcoding more checks and logic handling.
This makes the logic inflexible, because if anyone wants to add another behavior onto the feature, they likely have to append even more checks onto the checks you appended yourself.

For example, take the `Hotspot` system, which checks if a tile is allowed to start a gas fire on itself:

```C#
if ((tile.Hotspot.Temperature < Atmospherics.FireMinimumTemperatureToExist) ||
    (tile.Hotspot.Volume <= 1f) ||
    tile.Air == null ||
    tile.Air.GetMoles(Gas.Oxygen) < 0.5f ||
    (tile.Air.GetMoles(Gas.Plasma) < 0.5f &&
    tile.Air.GetMoles(Gas.Tritium) < 0.5f))
{...}
```

Do not add more checks onto this system in order to make reagent fires possible like so:

```C#
if ((tile.Hotspot.Temperature < Atmospherics.FireMinimumTemperatureToExist) ||
    (tile.Hotspot.Volume <= 1f) ||
    tile.Air == null ||
    tile.Air.GetMoles(Gas.Oxygen) < 0.5f ||
    (tile.Air.GetMoles(Gas.Plasma) < 0.5f &&
    tile.Air.GetMoles(Gas.Tritium) < 0.5f)) &&
    tile.SolutionFlammability == 0))
{...}
```

Instead, the `Hotspot` logic should be reworked so that both gas states and reagent states can contribute to a general flammability score that increases the temperature of the tile.
This allows future contributors to simply add more mechanics that contribute to a tile's overall flammability (ex. carpet or wooden furniture, a Diona standing on the tile, etc.).

Hardcoding more checks into the subsystem instead of making your own bespoke subsystem or making contributions generic also means that it wil be harder to make your feature configurable/disablable.

### Atmospherics logic should be mindful of its time budget
Atmospherics spans its processing over multiple ticks in order to soften the blow that it makes to `EntitySystem` tick timing.
Because of this, subsystems have to be mindful of how much time they've taken since the tick began, and yield processing to the next processing tick when necessary.

This is commonly done via the simulation stopwatch in `AtmosphereSystem._simulationStopwatch`.
Processing states will inspect this stopwatch every few seconds and yield if processing time exceeded the budget for the tick:
```C#
private bool ProcessHotspots(
    Entity<GridAtmosphereComponent, GasTileOverlayComponent, MapGridComponent, TransformComponent> ent)
{
    var atmosphere = ent.Comp1;
    if(!atmosphere.ProcessingPaused)
        QueueRunTiles(atmosphere.CurrentRunTiles, atmosphere.HotspotTiles);

    var number = 0;
    while (atmosphere.CurrentRunTiles.TryDequeue(out var hotspot))
    {
        ProcessHotspot(ent, hotspot);

        if (number++ < LagCheckIterations)
            continue;

        number = 0;
        // Process the rest next time.
        if (_simulationStopwatch.Elapsed.TotalMilliseconds >= AtmosMaxProcessTime)
        {
            return false;
        }
    }

    return true;
}
```

As such, your subsystem should not be designed where it has to execute its entire simulation stage in one go, rather it should be able to pause and resume its processing over many ticks.
Many systems accomplish this by processing what needs to be done per-unit, and checking the stopwatch occasionally to see if time is up.

Note that this gets more complicated for multithreaded and/or vectorized processing stages - benchmarking should be used to ensure that single runs of a processing stage do not dramatically exceed the maximum time allowed.

### Reuse memory whenever possible - avoid allocating on the heap for simulation
When writing code for Atmospherics, be mindful of any heap allocations that you make, even if it's something like a `foreach` enumeration or a `List<T>`.

Object allocations put unnecessary pressure on the GC, especially if said object allocations are in simulation code, code that is running per atmostick.
As such, reuse memory like arrays as much as possible.
For example, `AtmosphereSystem.Monstermos` holds arrays for queueing tiles and computing pressure spreading:

```C#
public sealed partial class AtmosphereSystem
{
    [Dependency] private readonly FirelockSystem _firelockSystem = default!;

    private readonly TileAtmosphereComparer _monstermosComparer = new();

    private readonly TileAtmosphere?[] _equalizeTiles = new TileAtmosphere[Atmospherics.MonstermosHardTileLimit];
    private readonly TileAtmosphere[] _equalizeGiverTiles = new TileAtmosphere[Atmospherics.MonstermosTileLimit];
    private readonly TileAtmosphere[] _equalizeTakerTiles = new TileAtmosphere[Atmospherics.MonstermosTileLimit];
    private readonly TileAtmosphere[] _equalizeQueue = new TileAtmosphere[Atmospherics.MonstermosTileLimit];
    private readonly TileAtmosphere[] _depressurizeTiles = new TileAtmosphere[Atmospherics.MonstermosHardTileLimit];
    private readonly TileAtmosphere[] _depressurizeSpaceTiles = new TileAtmosphere[Atmospherics.MonstermosHardTileLimit];
    private readonly TileAtmosphere[] _depressurizeProgressionOrder = new TileAtmosphere[Atmospherics.MonstermosHardTileLimit * 2];
    ... 
}
```

Notice that the initial sizes for the arrays are all `const` values as per the previously mentioned conventions.

Since you're usually writing for `Content.Server` and `Content.Server` only, you can take advantage of `stackalloc` and `ArrayPool`.
Note that you should always be very careful when using `stackalloc` as your desired array size for your data has the potential to overflow the stack.

In multithreading contexts (ex. `IParallelRobustJob`), it is preferable to use `ArrayPool` to quickly rent arrays for use.
Be sure to always return them in the event of an exception.
