# ECS Example

```csharp
// A system running on the server...
// Whenever an user interacts with an entity that has this component,
// a counter in it will be incremented by zero. An event will be raised too.
// Other Entity Systems can interact with FooComponent using the public API here.
public sealed class FooSystem : EntitySystem
{
    [Dependency] protected readonly SharedAppearanceSystem _appearanceSystem = default!;

    // Always subscribe to events here, on initialize
    public override void Initialize()
    {
        // Subscribe to FooComponent being initialized...
        SubscribeLocalEvent<FooComponent, ComponentInit>(OnFooInit);

        // Subscribe to FooComponent being interacted on by an user with an item.
        SubscribeLocalEvent<FooComponent, InteractUsingEvent>(Handle);

        // Subscribe to the MoveEvent broadcast event, raised whenever
        // an entity moves... Just an example subscription
        SubscribeLocalEvent<MoveEvent>(OnEntityMove);
    }

    // This is called each game tick
    public override void Update(float frameTime)
    {
        // This code is ran every tick
    }

    // This is called when a FooComponent is initialized.
    private void OnFooInit(Entity<FooComponent> ent, ref ComponentInit _)
    {
        // Initialize your FooComponent here
    }

    // Example handler for when FooComponent is interacted with by an user.
    private void Handle(Entity<FooComponent> ent, ref InteractUsingEvent args)
    {
        // Increase interact counter by one
        // We call this method as it handles everything for us.
        SetInteractCounter((ent, ent.Comp), ent.Comp.InteractCounter + 1);
    }

    // This is called whenever an entity moves.
    private void OnEntityMove(ref MoveEvent ev)
    {
        // Do something here! Although we do nothing because this is an example...
    }

    // Public method that other systems can call to interact with FooComponent
    public void ResetInteractCounter(Entity<FooComponent?> ent)
    {
        // We just call our other method, which handles everything for us.
        SetInteractCounter(ent, 0);
    }

    // Public method that other systems can call to interact with FooComponent
    public void SetInteractCounter(Entity<FooComponent?> ent, int count)
    {
        // Try to resolve the component...
        if (!Resolve(ent, ref ent.Comp))
            return;

        // Store the old counter, for later...
        var oldCounter = ent.Comp.InteractCounter;

        // Set the new interact counter
        ent.Comp.InteractCounter = count;

        // Now we set some appearance data, if the entity has an appearance comp
        if (TryComp(ent, out AppearanceComponent? appearance))
            _appearanceSystem.SetData(ent, FooVisualData.InteractCounter, count, appearance);

        // Now, we raise an event to let everyone know InteractCounter changed
        // Because the third argument is false, this event will not be broadcast.
        // This is raised as a directed event only!
        RaiseLocalEvent(ent, new FooInteractCounterChangedEvent(oldCounter, ent.Comp.InteractCounter));
    }
}

[RegisterComponent]
public sealed partial class FooComponent : Component
{
    // This will be increased every time an user interacts with us.
    // Notice how the logic for this is not in this component, but in the system.
    [DataField]
    public int InteractCounter = 0;
}

// Event that will be raised whenever the FooComponent interact counter changes.
// This event is immutable and informative, meaning it cannot be changed by handlers
// and its only purpose is to inform of some event, in this case, a change in a value
public sealed class FooInteractCounterChangedEvent : EntityEventArgs
{
    public int OldCounter { get; }
    public int NewCounter { get; }

    public FooInteractCounterChangedEvent(int oldCounter, int newCounter)
    {
        OldCounter = oldCounter;
        NewCounter = newCounter;
    }
}

[Serializable, NetSerializable]
public enum FooVisualData
{
    InteractCounter,
}
```
