# Device Network

Device networking allows machines and devices to communicate with each other while adhering to restrictions like range or being connected to the same powernet. Players will also have the abillity to interact with the device network in multiple ways. For example one could use a packet sniffer in their pda *(Not yet implemented)* to listen to messages sent over the wireless device network.

## Quick Overview
Entities can join a network and will be assigned a network address. These entities can then optionally choose to listen on some frequency. Any device on a network can send packets on any frequency (not just one it's listening on). The packets can either be broadcast, or directed at a specific address. The actual packets take the form of ECS events. A system just needs to listen for a `DeviceNetworkPacketEvent`. This event contains information about the sender and a `NetworkPayload`, which is basically just a `Dictionary<string, object>`. The contents of the payload and how to interpret them is just hard coded in each system. Some commonly used string keys are defined in `DeviceNetworkConstants.cs`.

### Network ids:
Device Net Ids are used to segregate devices into different sub networks. This is done for performance and organisational reasons and to prevent players from interacting with packets that are not supposed to be interacted with.

```admonish warning
Device net ids **do not** specify how a device connects to other devices (e.g wireless). Use the components for that.
```

 **0 - PRIVATE `netId: Private`**
    This network is not supposed to be interacted with by players.
 
 **1 - WIRED `netId: Wired`**
    Used for wired networks. This is supposed to be used with the `WiredNetworkComponent` if the device doesn't use a custom device net id.
 
 **2 - WIRELESS `netId: Wireless`**
    Used for wireless networks. This is supposed to be used with the `WirelessNetworkComponent` if the device doesn't use a custom device net id.
    
 **3 - ApcNet `netId: Apc`**
    Used for wired networks that are limited to apc extension cables. E.g. light switches. This is supposed to be used with the `ApcNetworkComponent` if the device doesn't use a custom device net id.

 **4 - AtmosDevices `netId: AtmosDevices`**
   Used for atmospherics devices like scrubbers to segregate them from other networks 


## Network Connection Components
To use the device network you need to add the DeviceNetworkComponent and the component for the type of connection you want. You can also not use one of the connection components when you want the device to always be able to send and receive messages.
There are different types of connection components.
### Device Network Component
This is the required component for sending and receiving device network messages.

<details>
<summary>YAML</summary>

```yaml=
components:
- type: DeviceNetwork
  deviceNetId: <Private|Wired|Wireless|Apc>
  receiveFrequency: <uint?>
  receiveFrequencyId: <string?>
  transmitFrequency: <uint?>
  transmitFrequencyId: <string?>
  address: <string>
  customAddress: <bool>
  prefix: <string>
  receiveAll: <bool>
  autoConnect: <bool>
  sendBroadcastAttemptEvent: <bool>
```

**deviceNetId**
Set the DeviceNetId of this device. If you need to add a new one add it to `DeviceNetIdDefaults` in `DeviceNetworkComponent.cs`.
  Defaults to 0 (Private).

**receiveFrequency**
The frequency this connection receives packets on. Defaults to null, in which case this device will not receive any packets (though it can still send them).

Unless your device has to possibly listen for messages, this should be set to null for performance reasons. E.g., while every player's suit-sensors will send packets on a given frequency, they do not listen for packets on any frequency.

**receiveFrequencyId**
The ID string for a `FrequencyPrototype`. If this field is not null, then during mapinit component's `receiveFrequency` will be updated to match the prototype's frequency. These prototypes are basically just named uints. E.g., the `SuitSensor` prototype should be used for all suit-sensor or crew-monitor related devices.

**transmitFrequency**
This is the default frequency that a device will use to transmit packets. It is simply used as a default argument for the send-packet function.
  
**transmitFrequencyId**
Like `receiveFrequencyId`, but for `transmitFrequency`
  
**address**
The address of a device on a network. Used to ensure that devices have persistent addresses when a map is saved or loaded. By default, addresses are auto-generated when first connecting to a network. If the address field is already filled in, and the requested address is already taken, it will simply generate a new address. 
  
**customAddress**
Specifies whether the `address` was randomly generated when connecting to a network, or explicitly specified. If the address is a custom address, it will not be overriden by automatically generated addresses when connecting to networks.

**prefix**
A prefix string that is prepended to any randomly generated addresses (which are just hex-code strings). Useful for allowing a device-type to be identifiable via the address. E.g., all atmos vents have a `Vnt-` prefix.
  
**receiveAll**
If true, this device will receive all packets sent on the `receiveFrequency`, instead of only those that are either broadcast or directed at this devices' address. Can be used to snoop in on messages.
  
**autoConnect**
Determines whether a device should attempt to join a network on map init. Usually true, unless a device was explicitly disconnected from a network, in which case it should not re-connect when a map is re-loaded.

**sendBroadcastAttemptEvent**
Sends the broadcast recipients list to the sender before breadcasting a packet so it can be filtered if set to `true`.
Defaults to `false`.
  
</details>

### Wireless Network Component
The wireles network component checks if the devices are in range of each other before allowing a message to be sent.

<details>
<summary>YAML</summary>

Allows a devices to send packets to other devices as long as the are the sender's wireless range is large enough.

```yaml=
components:
    - type: DeviceNetworkComponent
    ...
    - type: WirelessNetworkConnection
      range: <int>
```

**range**
The range this connection sends and receives at.
  
</details>

### Apc Network Component

```admonish danger
It's very hard to prevent APCs from connection with each other during mapping and limiting an APC to a specific room or making sure all the devices you want are connected is difficult. This component might get removed in the future because of that.
```

Allows devices send packets to each other as long as they are drawing power from the same APC.
  
<details>
<summary>YAML</summary>
  
```yaml=
components:
    - type: DeviceNetworkComponent
    ...
    - type: ApcNetworkConnection
```

</details>

  
### Wired Network Component

```admonish danger
Currently it only checks if the devices are on the same grid. Behavior will be implemented in the future.
```

<!--The wired network component connects to the wired device network, which currently uses power cables for connecting devices to each other.
This means that every wired network connection that is connected to the same power source is on the same wired network.
-->

<details>
<summary>YAML</summary>
  
```yaml=
components:
    - type: DeviceNetworkComponent
    ...
    - type: WiredNetworkComponent
```

</details>

### Station Limited Network Component

Allows devices that belong to the same station to send and receive packets to each other.

<details>
<summary>YAML</summary>
  
```yaml=
components:
    - type: DeviceNetworkComponent
    ...
    - type: StationLimitedNetwork
      allowNonStationPackets: <bool>
```

**allowNonStationPackets**
Allows the device to receive packets from devices that don't have a `StationLimitedNetwork` component.

</details>

### Device Network Requires Power Component

Prevents any packets from being received if the device doesn't have power.

<details>
<summary>YAML</summary>
  
```yaml=
components:
    - type: DeviceNetworkComponent
    ...
    - type: DeviceNetworkRequiresPower
```

</details>
  
## The device network system

### Events
There are three events used by the system to send messages to devices:

**BeforeBroadcastAttemptEvent**
This event is sent to an entity that is about to breadcast a packet if `sendBroadcastAttemptEvent` is set to true on the sending device. This event can be used to modify the recipients of that broadcast or to cancel it.

<details>
<summary>DETAILS</summary>
  
``BeforeBroadcastAttemptEvent(IReadOnlySet<DeviceNetworkComponent> recipients)``
 
 **recipients**
   The list of recipients the broadcast is about to send packets to.
 **Property: ModifiedRecipients**
   This is a property on the event that can to be set to the new list of recipients.
	 If this property is null the breadcast will be canceled.

</details>  
  
**BeforePacketSentEvent**
This event is raised before a device network message is sent. Subscribed to by other systems to prevent the message from being sent.
<details>
<summary>DETAILS</summary>
  
``BeforePacketSentEvent(EntityUid sender, TransformComponent xform, Vector2 senderPosition)``
 
 **sender**
   The EntityUid of the entity the message was sent from.
 **xform**
   The transform component of the sender.
 **senderPosition**
   The world-position of the sender.

</details>
  
**DeviceNetworkPacketEvent**
  Event raised directed at an entity when a device network message is received.
<details>
<summary>DETAILS</summary>
  
 ``DeviceNetworkPacketEvent(ConnectionType netId, string? address, uint frequency, string senderAddress, EntityUid sender, NetworkPayload data)``
  
  **netId**
    The network that was used to send the packet.
 
  **address**
  	The address that the packet was sent to. Null if the packet was broadcast.
  
  **frequency**
    The frequency the message was sent on.
  
  **senderAddress**
  	The device network address of the sending entity
  
  **sender**
  	The sender's EntityUid
  
  **data**
    The data that is beeing sent.
</details>

  
### Methods

**QueuePacket**
  Sends the given payload as a device network message to the entity with the given address and frequency.
  
  <details>
<summary>DETAILS</summary>
  
 ``QueuePacket(EntityUid uid, string? address, NetworkPayload data, uint? frequency = null, int? network = null, DeviceNetworkComponent? device = null)``
 
  **uid**
    The EntityUid of the sending entity.
  
  **address**
  	The address of the entity that the packet gets sent to. If null, the packet gets broadcast.
  
  **data**
    The data that is beeing sent.
      
  **frequency**
  	The frequency on which to send the data. If null, will default to the devices current transmit frequency.

  **network**
  	The network id to send on. 
</details>
  
The device network system contains more public methods for things like setting the listening frequency of a device.
  
## The network payload class
The network payload class contains the data that is sent over the device network which can eventually be seen by the player.
The player will only be able to see and manipulate primitive types if they can see or manipulate the payload.

Creating a network payload:
```csharp=
var payload = new NetworkPayload
{
    ["Key1"] = Value1,
    ["Key2"] = Value2,
    ["Key3"] = Value3
    //...
};
```

## The device network constants class
The class DeviceNetworkConstants contains common network ids and string constants for creating network payloads. You are not restricted to using the ids or string constants provided in this class but you should try to use COMMAND when applicable.

When creating network payloads you should try to use constants for keys and values that are always the same.

One example of a command and message is the mailing units `get_mailer_tag` for querying other units and its `mailer_tag` message for responding with its tag.

### Standard payload constants:

 **COMMAND**
    The key used for specifying the command/type of payload e.g. pda_mail.
  
## Examples:
### Sending a network Message

```csharp=
//This is somewhere at the top of your entity system
[Dependency] private readonly DeviceNetworkSystem _deviceNetworkSystem = default!;

public const string NetCmdPdaMail = "pda_mail";
public const string NetTargetMail = "target_mail_address";
public const string NetSenderMail = "sender_mail_address";
public const string NetMessage = "message";
...
//When you want to send a network message you need to construct a network payload and send it using the DeviceNetworkSystems QueuePacket method.
var payload = new NetworkPayload
{
    [DeviceNetworkConstants.COMMAND] = NetCmdPdaMail,
    //You're not restricted to using DeviceNetworkConstants.COMMAND
    [NetMessage] = "Hi Bob, bla bla bla...",
    [NetTargetMail] = "5525bob@nanotrasen.com",
    [NetSenderMail] = "7361joe.genero@nanotrasen.com"
};

_deviceNetworkSystem.QueuePacket(uuidOfCurrentEntity, addressOfMailserverOrSomething, payload);
```
The sending entity should either be pre-configured to send on the mailing frequency, or else you would need to resolve the mailing frequency prototype and pass the correct frequency as an argument.

### Receiving and handling a network message

```csharp=
...
[Dependency] private readonly DeviceNetworkSystem _deviceNetworkSystem = default!;

public const string NetCmdPing = "ping"
public const string NetMessage = "message";

public override void Initialize()
{
    base.Initialize();

		...
	  SubscribeLocalEvent<DeviceNetworkComponent, DeviceNetworkPacketEvent>(OnPacketReceived);
		...
}
...

private void OnPacketReceived(Entity<DeviceNetworkComponent> ent, ref DeviceNetworkPacketEvent args)
{
    //Since we are doing it the recommended way of using the command constant we try to get it from the payload
    if (args.Data.TryGetValue(DeviceNetworkConstants.COMMAND, out String command))
    {
        //If that command is the PING command (you can check for your own command here)
        if (command == NetCmdPing)
        {
            //We create a payload containing the ping_response command and "Hello World" as a message. 
            //(For this example I just passed the command name as a string instead of creating a constant.)
            var payload = new NetworkPayload
            {
                [DeviceNetworkConstants.COMMAND] "ping_response",
                [NetMessage] = "Hello World"
            };
            
            //And send the response to that ping
            _deviceNetworkSystem.QueuePacket(ent, args.SenderAddress, payload, args.Frequency);
        }
    }
}
```
