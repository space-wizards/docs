# Cartridge Loaders

Cartridge loaders are things like PDAs and PCs.

Cartridges will be interchangeably referred to as program or cartridge depending on if they are installed onto the cartridge loader or just inserted into it.

## Concepts
### Insertion
The `CartridgeLoaderSystem` will send a `CartridgeAddedEvent` event to the cartridge entity when it gets inserted or installed onto the loader.
### Installation
Cartridge prototypes can be specified on the `CartridgeLoaderComponent` that should be installed on map init and inserted cartridges can be installed onto the loader by players.
Cartridge loaders have a maximum amount of programs they can have installed.
The installation limit is ignored when installing cartridges specified in the loaders prototype.
### Activation
A cartridge/program will be saved as active on the cartridge loader component and the `CartridgeActivatedEvent` will be raised at it when the player opens the program throught the ui.
### Deactivation
When the player exits a program or changes to another program the `CartridgeDeactivatedEvent` will be raised at the currently active program and the saved active program will be changed/cleared.
This doesn't happen when the players closes the loaders UI. Opening the UI agian will just display currently active program ui.
### Event relay
The `CartridgeLoaderSystem` will relay specific events to the currently active program and all programs that are running in the background. This includes device networking events.

#### Currently relayed events:
- `DeviceNetworkPacketEvent` using the `CartridgeDeviceNetPacketEvent`
- `AfterInteractEvent` using the `CartridgeAfterInteractEvent`
- Any subclass of `CartridgeMessageEvent` which gets wrapped using `CartridgeUiMessage`, a subclass of `BoundUserInterfaceMessage` for sending messages from the cartridges ui
  
All relayed events contain the cartridge loaders entity uid as the property: `LoaderUid`.
### Background programs
A program can register and deregister itself as active in the background and it will receive mostly the same events as the active program.
The `CartridgeUiMessage` event won't be relayed to background programs.

Something like a messaging program would run in the background for example.
### Program UI fragments
Cartridge UIs are subclasses of the abstract `CartridgeUi` class which defines methods for getting the root control of that piece of UI and methods for setting it up and updating it. The root control returned gets attached to a control in the catridge loaders UI using that controls `AddChild` method. Those pieces of UI are called UI fagments.

Cartridge prototypes specify the UI fragment to use in the`CartridgeUiComponent`'s `Ui` field.
Example:
```yaml
  - type: CartridgeUi
    ui: !type:NotekeeperUi
```
### Homescreen Items
```admonish danger
Homescreen items are not yet implemented
```

Cartridges can add something to homescreen of a CartridgeLoader. The specific variant of cartridge loader isn't required to show these. (PDAs will but PCs might not)

Homescreen Items are just text that will be displayed on the homescreen like:
```
- Alerts: 0
- New Messages: 14
- Latest news:
    John Genero caused an uproar when he slipped the clown that
    was leaving banana peels everywhere
```
The items are sorted by a priorty property and there are a limited number of items that can be displayed.
If an Item is added when the items are already full the lowest priority one gets removed.