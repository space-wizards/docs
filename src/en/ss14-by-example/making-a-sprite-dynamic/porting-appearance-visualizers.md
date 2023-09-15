# Porting Appearance Visualizers

As explained in the [sprite docs](../making-a-sprite-dynamic.md) Visualizer Systems are how client-side sprites are modified using appearance data from the server. 

The old method is by using a class inheriting from `AppearanceVisualizer` which is specified on the `AppearanceComponent`. New way is by just using a component for the data used to tweak the visualizer and a system for the actual logic instead of just one class. Benefits are that they can use anything that ECS Systems can (including event subscriptions importantly!)

This doc explains how to migrate an `AppearanceVisualizer` to a new component & system using a basic example found in this PR: https://github.com/space-wizards/space-station-14/pull/6571/files with some very minor deviation. Includes and such will not be put so you'll need to do those yourself

Here's the full visualizer we're porting:

```csharp
    [UsedImplicitly]
    public class ItemCabinetVisualizer : AppearanceVisualizer
    {
        [DataField("openState", required: true)]
        private string _openState = default!;

        [DataField("closedState", required: true)]
        private string _closedState = default!;

        public override void OnChangeData(AppearanceComponent component)
        {
            base.OnChangeData(component);

            var entities = IoCManager.Resolve<IEntityManager>();
            if (entities.TryGetComponent(component.Owner, out SpriteComponent sprite)
                && component.TryGetData(ItemCabinetVisuals.IsOpen, out bool isOpen)
                && component.TryGetData(ItemCabinetVisuals.ContainsItem, out bool contains))
            {
                var state = isOpen ? _openState : _closedState;
                sprite.LayerSetState(ItemCabinetVisualLayers.Door, state);
                sprite.LayerSetVisible(ItemCabinetVisualLayers.ContainsItem, contains);
            }
        }
    }
```

## 1. Separate data and logic

First task is to copy the data into a new component and copy the logic into a new system. Don't worry about porting it fully just yet or if there are errors, we'll do that later.

Component:

```csharp
    [RegisterComponent]
    public sealed class ItemCabinetVisualsComponent : Component
    {
        [DataField("openState", required: true)]
        private string _openState = default!;

        [DataField("closedState", required: true)]
        private string _closedState = default!;
    }
```

System:

```csharp
    public sealed class ItemCabinetVisualizerSystem : VisualizerSystem<ItemCabinetVisualsComponent>
    {
        public override void OnChangeData(AppearanceComponent component)
        {
            base.OnChangeData(component);

            var entities = IoCManager.Resolve<IEntityManager>();
            if (entities.TryGetComponent(component.Owner, out SpriteComponent sprite)
                && component.TryGetData(ItemCabinetVisuals.IsOpen, out bool isOpen)
                && component.TryGetData(ItemCabinetVisuals.ContainsItem, out bool contains))
            {
                var state = isOpen ? _openState : _closedState;
                sprite.LayerSetState(ItemCabinetVisualLayers.Door, state);
                sprite.LayerSetVisible(ItemCabinetVisualLayers.ContainsItem, contains);
            }
        }
    }
```


## 2. ECS-ify data

Now we need to convert the component into the proper ECS state!

1) Turn all private fields public
2) Remove any properties and just use the backing fields, any logic should go in member methods on the system
3) Change the names of all fields to match naming conventions
4) Add more datafields if necessary
5) Move the corresponding `VisualLayers` enum if one exists to the component class as well

So it'll look like this now:

```csharp
    [RegisterComponent]
    public sealed class ItemCabinetVisualsComponent : Component
    {
        [DataField("openState", required: true)]
        public string OpenState = default!;

        [DataField("closedState", required: true)]
        public string ClosedState = default!;
    }
```

## 3. ECS-ify logic

Logic needs to be ported in two ways:
- The `OnAppearanceChange` method needs to be converted into the proper entity system override
- Any `InitializeEntity` method needs to be converted into a new `ComponentInit` event handler directed at the component you made

A couple other things need to be done:
- Any dependencies should be moved to the system
- Any manual resolves should be made into dependencies
- Any `IEntityManager` resolves should use the `EntityManager` field that already exists on `EntitySystem`, or the proxy methods
- Any TryGets for `SpriteComponent` should use the `Sprite` field on the event args instead
- Any references to fields that used to be on the visualizer need to be converted into references to fields on the component

This one just needs the first but I'll show an example of the second later as well

Appearance change signature is now `protected override void OnAppearanceChange(EntityUid uid, T component, ref AppearanceChangeEvent args)`, so we'll update the function to reflect that.

We also need to remove the `IEntityManager` resolve and convert the calls to it into the proxy methods. However, since the method calls used are just to get the `SpriteComponent`, we can use the field on the event args instead.

```csharp
    public sealed class ItemCabinetVisualizerSystem : VisualizerSystem<ItemCabinetVisualsComponent>
    {
        public override void OnChangeData(EntityUid uid, ItemCabinetVisualsComponent component, ref AppearanceChangeEvent args)
        {
            if (args.Sprite != null)
                && component.TryGetData(ItemCabinetVisuals.IsOpen, out bool isOpen)
                && component.TryGetData(ItemCabinetVisuals.ContainsItem, out bool contains))
            {
                var state = isOpen ? component.OpenState : component.ClosedState;
                args.Sprite.LayerSetState(ItemCabinetVisualLayers.Door, state);
                args.Sprite.LayerSetVisible(ItemCabinetVisualLayers.ContainsItem, contains);
            }
        }
    }
```

This doesn't use `InitializeEntity` but if it did the full class would look like this:

```csharp
    public sealed class ItemCabinetVisualizerSystem : VisualizerSystem<ItemCabinetVisualsComponent>
    {
        public override void Initialize()
        {
            base.Initialize(); // this is very important! need it this time

            SubscribeLocalEvent<ItemCabinetVisualsComponent, ComponentInit>(OnComponentInit);
        }

        private void OnComponentInit(EntityUid uid, ItemCabinetVisualsComponent component, ComponentInit args)
        {
            // behavior!
    		}

        protected override void OnChangeData(EntityUid uid, ItemCabinetVisualsComponent component, ref AppearanceChangeEvent args)
        {
            if (args.Sprite != null)
                && component.TryGetData(ItemCabinetVisuals.IsOpen, out bool isOpen)
                && component.TryGetData(ItemCabinetVisuals.ContainsItem, out bool contains))
            {
                var state = isOpen ? component.OpenState : component.ClosedState;
                args.Sprite.LayerSetState(ItemCabinetVisualLayers.Door, state);
                args.Sprite.LayerSetVisible(ItemCabinetVisualLayers.ContainsItem, contains);
            }
        }
    }
```


## 4. Update YAML & IgnoredComponents.cs

Now we need to update YAML for our new component as well as the server ignored comps list.

Go to `Content.Server/Entry/IgnoredComponents.cs` and add a line with your new component name like this:

```csharp
        public static string[] List => new [] {
            ... snip ...
            "ItemCabinetVisuals",
        };
 ```
 
 This is done automatically for server components that don't exist on the client, but not vice versa since this is usually a more uncommon operation, and you can't do both. So this just tells the server to not worry about seeing this component in YAML.
 
 Find usages of the old visualizer using CTRL+SHIFT+F or an equivalent in any IDE like so:
 
 ```yaml
     - type: Appearance
      visuals:
        - type: ItemCabinetVisualizer
          openState: open
          closedState: closed
```

Replace it like this:

 ```yaml
     - type: Appearance
     - type: ItemCabinetVisuals
       openState: open
       closedState: closed
```

**Keeping the appearance component there is important!** Easily missed bug. Basically just un-indent the visuals block and change the name of the component.

You should be done!

## 5. If possible, generalize.

Instead of adding many separate visualier systems & components, it is often possible to just make a visualier more general by adding an extra yaml data-field. To this end, there is a `GenericVisualizerSystem` & component, which replaces the older `GenericEnumVisualizer`. If all you need the visualizer to do is to set some sprite layer data based on simple appearance data entries, you very likely can, and should, just use the generic visualizer instead of creating your own custom one. However, if you need to do fancy things like use animations or have more complex logic, you will still need to create your own.

For example, the functionality of the above cabinet visualizer simply sets a sprite layer states & visibility based on two appearance data entries. Instead of having this system & component, the same functionality could be achieved by using the generic visualizer:
```yaml
     - type: Appearance
     - type: GenericVisualizer
       visuals:
         enum.ItemCabinetVisuals.IsOpen: # <- Appearance data key. Either an enum or a general string.
           enum.ItemCabinetVisualLayers.Door: # <- sprite layer key. Either an enum or a general string.
            True: # <- Appearance data value
              state: open # <- Sprite layer data that should be used for this appearance value
            False: { state: closed } # <- You can also inline yaml, which can reduce indentation and improve readability.
         # and then again for the other appearance entry:
         enum.ItemCabinetVisuals.ContainsItem:
           enum.ItemCabinetVisualLayers.ContainsItem:
             True: { visible: true}
             False: { visible: false}
```
The sprite sprite layer data can set the `sprite`, `state`, `texture`, `shader`, `scale`, `rotation`, `offset`, `visible` and `color`.
Note that the yaml for the appearance values are simply the `ToString()` results of a the appearance data values.
So `bool`s become "True"/"False", while an enum like `VentPumpState.Off` just becomes "Off".
