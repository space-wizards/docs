# Containers

Containers contain entities. Whether for inventory, backpacks, solutions, or actions. Containers contain lists of entities for usage in systems.

## Review

Any code that subscribes to container events should have a guard clause that checks for only the relevant containers.

```cs
private void OnContainerModified(EntityUid uid, MicrowaveComponent component, ContainerModifiedMessage args)
{
    if (component.Storage != args.Container)
        return;

    // Code continues ...
}
```

There have been problems in the past with [updating UI on unrelated containers (#27500)](https://github.com/space-wizards/space-station-14/pull/27500)