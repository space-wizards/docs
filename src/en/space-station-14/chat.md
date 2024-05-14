# Chat and Other Messaging

## What is Chat?
Chat and other messages sent between players are grouped into the following types:

### "In round" messages:

* Local: Normal verbal communication.
* Whisper: Quiet verbal communication that is very short range and features occlusion mechanics.
* Emote: Visual communication via body langage. Requires line-of-sight.
* LOOC: Out-of-character chat that is supposed to be used for asking for help or "I need to go AFK" messages, but is actually used for being salty.
* Radio: Wireless communication via hub servers or other technology that can be listened to via equipment or innate powers. Covers all "role-specific" communications like Binary for robots or the Syndicate channel for traitors and nuclear operatives.
    * Equipment radio covers radio that is granted by having access to a worn piece of equipment, such as a headset.
    * Internal radio covers radio that is granted by some internal power, like Binary for robots or "nearly everything" for Nar'sie.
    * Device radio covers radio that sends and receives from a specific location in the game, like handheld radios or intercoms.
* Dead: The place ghosts talk where players can't hear them (and the place admins post when they want to be seen by dead people)
* Announcements: Various announcements from automated messages through to adminbus messages or comms console notifications.
* Background: Where automated chats like vending machine announcements are issued. Essentially identical to local chat, but these messages are "not real" and do not go into chat logs or get message IDs (see below)
* Prayer: Messages sent from players in-game to admins via some artifact like the red phone or the maint altar.
* Subtle: Messages targeted at one specific player, currently solely an adminbus feature.

These chat types cover messages that are "round-scoped". This means they relate to something that shows up in replays and are "things that happened in that particular round".

### "Out of round" messages

* OOC: Lobby comms for people out-of-game. Usually switched off by cvar during games.
* Admin: Admin notices, from all-player bwoinks to requests for feedback on events.
* Server: "PLAYER JOINED, PLAYER LEFT" yadda yadda. Also covers tips.

These are "server-scoped" messages. They don't need to show up in replays (although it's an implementation note if they do or not) and cover all out-of-game conversation.

Generally you can summarize the difference between the two types by "the former is sent by something that exists in the Space Station 14 universe, and the latter is sent by people in the real world".

### Examples of Weird Crossovers

* Server tips are out-of-round, but Tippy (the rare pop-up clown that gives a tip) is considered in-round by players.
* LOOC is out-of-round in topic but said by characters in-game.
* Faxing and other player-to-player messages like PDA messages (proposed) work like chatting but don't use the same devices like the chat log and fall out of most of the "chat" domain.

## Component-based Chat Privilages

Chat is driven by components, rather than having its functionality defined completely in C#. The rights a mob has to use most channels (excluding LOOC and Dead) are governed by components they have. For example, to actually speak in local chat, a mob must have the following component:

```cs
using Robust.Shared.GameStates;

namespace Content.Shared.Chat.V2.Components;

/// <summary>
/// Declares that this entity can chat in local chat
/// </summary>
[RegisterComponent, NetworkedComponent, AutoGenerateComponentState]
public sealed partial class CanLocalChatComponent : Component
{
    // TODO: Ensure you can't locally chat in insufficient atmosphere

    /// <summary>
    /// How far can this entity be heard from?
    /// </summary>
    [DataField, AutoNetworkedField]
    public float Range = 10.0f;
}
```

Note that this component not only grants them the right to use local chat, it also determines how they use it. In this case, it governs the range they can be heard from. It stands to reason that Nar'sie, eldritch god, probably speaks louder than Pun-Pun.

## The Chat Message Lifecycle

Chat messages are created and used via a lifecycle of events. This can also be described as "chat is event-driven". What both of these terms mean is that a series of events build a step-by-step process that turns a player's input into output other players can read.

The lifecycle can be summarized by the following steps.

1. In the client, a player attempts to send a chat message to a channel by issuing a chat message attempt event.
    * This attempt goes over the network to the server.
2. The attempt is processed by a **chat message attempt processor** on the server.
    * The validator issues a chat validation event that is consumed by processors. 
    * If no processor fails the attempt, the validator will then sanitize the message's contents. 
    * The result of sanitization is handed to the **chat message repository**.
3. The **chat message repository** stashes the chat message away to be referred to later.
    * It gives the message a unique ID that can be used to reference the message at any point later on.
    * It associates all messages with the player who sent them, allowing for easy mass-deletion by an admin.
    * It issues a chat message created event that allows further processors to respond.
4. The **chat message created processor** listens for chat message creation events.
    * The processor issues an chat message accent transformation event that is consumed by processors.
    * These processors modify the sent message to add "global" modifiers, such as a lizard person's trailing s's, a voice mask, and so on.
    * It issues a chat reception event that is consumed by processors.
    * These processors determine who receives the event.
    * The receiver processor then emits a chat message mutation event for each receiver.
    * These processors determine how a chat message is altered due to obfuscation, language, and so on.
    * After each mutation event is fully processed, the processor emits a chat message received event to the receiver.
    * This received event goes over the network to the client.
5. The **chat message received processor** listens to chat message received events on the client.
    * The various types of chat messages are then formatted and emitted in the various ways the client displays chat (in the chat log, in speech bubbles, etc)

It's not required that the processors in the above lifecycle are synchronous. For example, the chat message created processor could be broken up into accent transformation, receiver determination, mutation transformation and emission to clients. But the overall set of steps remains the same.

Likewise, it's not required these names to be stuck to absolutely - naming things is hard.

### Intended benefits of this approach

1. Code is split between "is this legal to send" and "how to handle that it has been sent". This means concerns are separated, which tends to make code easier to maintain - security requirements shouldn't bleed into other aspects of the chat management system, for example.
2. A set of events is easy to refactor. The work of the chat message repository does not assume anything about validation, who the eventual receivers are, and so on. It's one tightly-bounded component in a larger set of processors. This means it's easy to add or remove any one part.
3. The events can listened in on for wider functionality to be added, without that code living with irrelevant code nearby. For example, handheld radios don't ever really need to share code space with actual radios, but they both listen for radio message creation events. The handheld radio code would implement its own chat message created processor, handling accent, reception and mutation events itself. An example of why this is beneficial is that it makes a "universal translator" radio easy to implement.
4. All messages have a common ID. This means de-duplication is possible. For example, if the same message is sent to a handheld radio, an intercom and someone's headset, the frontend can detect that it has already displayed the chat message once, and thus the message does not need to be spammed repeatedly into the chat log, or might have a reduced impact in message bubbles.
    * This also means specific "delete/modify this message" and "nuke all of this player's messages" commands are possible for admin!

### Technical Details

This document can't describe the exact names and properties of every single event this process issues, but at an overall level there are a few technical notes worth considering.

1. Messages use inheritance and generics where possible to allow for code reuse. For example, all chat attempt events inherit from "ChatAttemptEvent", which specifies they must have a NetEntity and a message. Sometimes, like with internal, device and equipment radio events, this can involve multiple stages of inheritance.
2. Inheritance (and generics) are prioritized over in-message state flags. For example, there are several "radio attempt event" messages, rather than one "radio attempt event" message that has an internal type enum. This is so we can leverage the message bus effectively. In general, letting the message bus handle directing messages where they need to go is more efficient and cleaner, even
if it occasionally causes handler code duplication.
3. Generics are used for processor events, like chat sanitization events. For example, ChatValidationEvent\<T\> allows for different events to be validated in different ways: a radio event can have its channel checked to make sure it exists, for example.
4. Processor events should have the "abstract generic" raised first, then the "implementation generic" events. The event bus can't handle deep type comparison. For example, when T implements ChatAttemptEvent, ChatValidationEvent\<ChatAttemptEvent\> is raised before ChatValidationEvent\<T\>. Only when both types of event are raised and processed can the overall process continue onwards.

### Code examples

Using validation as an example, read the following:

```cs
using System.Diagnostics.CodeAnalysis;
using Content.Server.Administration.Managers;
using Content.Shared.Chat.V2;
using Content.Shared.Chat.V2.Components;
using Content.Shared.Ghost;
using Content.Shared.Mobs.Systems;
using Robust.Shared.Player;

namespace Content.Server.Chat.V2.Systems;

/// <summary>
/// ChatAttemptHandlerSystem defines a set of handlers and processes for managing chat attempts sent by clients.
/// </summary>
public sealed class ChatAttemptHandlerSystem : EntitySystem
{
    private const string DeadChatFailed = "chat-system-dead-chat-failed";
    private const string EmoteFailed = "chat-system-emote-failed";
    private const string LocalChatFailed = "chat-system-local-chat-failed";
    private const string RadioFailed = "chat-system-radio-failed";
    private const string WhisperFailed = "chat-system-whisper-failed";
    private const string EntityNotOwnedBySender = "chat-system-entity-not-owned-by-sender";

    [Dependency] private readonly ChatRepositorySystem _repo = default!;
    [Dependency] private readonly IAdminManager _admin = default!;
    [Dependency] private readonly MobStateSystem _mobState = default!;

    private string _deadChatFailed = "";
    private string _emoteFailed = "";
    private string _localChatFailed = "";
    private string _radioFailed = "";
    private string _whisperFailed = "";
    private string _entityNotOwnedBySender = "";

    public override void Initialize()
    {
        base.Initialize();

        _deadChatFailed = Loc.GetString(DeadChatFailed);
        _emoteFailed = Loc.GetString(EmoteFailed);
        _localChatFailed = Loc.GetString(LocalChatFailed);
        _radioFailed = Loc.GetString(RadioFailed);
        _whisperFailed = Loc.GetString(WhisperFailed);
        _entityNotOwnedBySender = Loc.GetString(EntityNotOwnedBySender);

        SubscribeNetworkEvent<AttemptDeadChatEvent>(OnAttemptDeadChat);
        SubscribeNetworkEvent<AttemptEmoteEvent>(OnAttemptEmote);
        SubscribeNetworkEvent<AttemptLocalChatEvent>(OnAttemptLocalChat);
        SubscribeNetworkEvent<AttemptLoocEvent>(OnAttemptLooc);
        SubscribeNetworkEvent<AttemptEquipmentRadioEvent>(OnAttemptEquipmentRadio);
        SubscribeNetworkEvent<AttemptInternalRadioEvent>(OnAttemptInternalRadio);
        SubscribeNetworkEvent<AttemptWhisperEvent>(OnAttemptWhisper);
    }

    private void OnAttemptDeadChat(AttemptDeadChatEvent ev, EntitySessionEventArgs args)
    {
        var entityUid = GetEntity(ev.Sender);

        if (!ValidateMessage(entityUid, ev, args.SenderSession, out var reason))
        {
            RaiseNetworkEvent(new DeadChatFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        var isAdmin = _admin.IsAdmin(entityUid);

        // Non-admins can only talk on dead chat if they're a ghost or currently dead.
        if (!isAdmin && !HasComp<GhostComponent>(entityUid) && !_mobState.IsDead(entityUid))
        {
            RaiseNetworkEvent(new DeadChatFailedEvent(ev.Sender, _deadChatFailed),
                args.SenderSession);

            return;
        }

        _repo.Add(new DeadChatCreatedEvent(entityUid, SanitizeMessage(ev), isAdmin));
    }

    private void OnAttemptEmote(AttemptEmoteEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _emoteFailed, out CanEmoteComponent? comp))
        {
            RaiseNetworkEvent(new EmoteFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new EmoteCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), comp.Range));
    }

    private void OnAttemptLocalChat(AttemptLocalChatEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _localChatFailed, out CanLocalChatComponent? comp))
        {
            RaiseNetworkEvent(new LocalChatFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new LocalChatCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), comp.Range));
    }

    private void OnAttemptLooc(AttemptLoocEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(GetEntity(ev.Sender), ev, args.SenderSession, out var reason))
        {
            RaiseNetworkEvent(new LoocFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new LoocCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev)));
    }

    private void OnAttemptEquipmentRadio(AttemptEquipmentRadioEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _radioFailed,
                out CanRadioUsingEquipmentComponent? comp))
        {
            RaiseNetworkEvent(new RadioFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new RadioCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), ev.Channel));
    }

    private void OnAttemptInternalRadio(AttemptInternalRadioEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _radioFailed, out CanRadioComponent? comp))
        {
            RaiseNetworkEvent(new RadioFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new RadioCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), ev.Channel));
    }

    private void OnAttemptWhisper(AttemptWhisperEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _whisperFailed, out CanWhisperComponent? comp))
        {
            RaiseNetworkEvent(new WhisperFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new WhisperCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), comp.MinRange, comp.MaxRange));
    }

    /// <summary>
    /// Validates messages. Return true means the message is valid.
    /// </summary>
    private bool ValidateMessage<T>(EntityUid entityUid, T ev, ICommonSession player, out string reason) where T : ChatAttemptEvent
    {
        // This check is simple, so we don't need to raise an event for it.
        if (player.AttachedEntity != null || player.AttachedEntity != entityUid)
        {
            reason = _entityNotOwnedBySender;

            return false;
        }

        // Raise both the general and specific ChatValidationEvents. This allows for general
        var validate = new ChatValidationEvent<ChatAttemptEvent>(ev);
        RaiseLocalEvent(entityUid, validate);

        if (validate.IsCancelled)
        {
            reason = validate.Reason;

            return false;
        }

        var validateT = new ChatValidationEvent<T>(ev);
        RaiseLocalEvent(entityUid, validateT);

        if (validate.IsCancelled)
        {
            reason = validate.Reason;

            return false;
        }

        reason = "";

        return true;
    }

    /// <summary>
    /// Validates messages which depend on a sentinel component to be legal.
    /// </summary>
    private bool ValidateMessage<T1, T2>(
        T1 ev,
        ICommonSession player,
        out string reason,
        string invalidCompReason,
        [NotNullWhen(true)] out T2? comp
    ) where T1 : ChatAttemptEvent where T2 : IComponent
    {
        comp = default;

        var entityUid = GetEntity(ev.Sender);

        if (!ValidateMessage(entityUid, ev, player, out reason))
        {
            return false;
        }

        if (TryComp(entityUid, out comp))
            return true;

        reason = Loc.GetString(invalidCompReason);

        return false;
    }

    /// <summary>
    /// Sanitizes messages. The return string is sanitized.
    /// </summary>
    private string SanitizeMessage<T>(T evt) where T : ChatAttemptEvent
    {
        var sanitize = new ChatSanitizationEvent<T>(evt);
        RaiseLocalEvent(sanitize);

        return sanitize.ChatMessageSanitized ?? sanitize.ChatMessageRaw;
    }
}
```

From the top, working down:

```cs
    private void OnAttemptDeadChat(AttemptDeadChatEvent ev, EntitySessionEventArgs args)
    {
        var entityUid = GetEntity(ev.Sender);

        if (!ValidateMessage(entityUid, ev, args.SenderSession, out var reason))
        {
            RaiseNetworkEvent(new DeadChatFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        var isAdmin = _admin.IsAdmin(entityUid);

        // Non-admins can only talk on dead chat if they're a ghost or currently dead.
        if (!isAdmin && !HasComp<GhostComponent>(entityUid) && !_mobState.IsDead(entityUid))
        {
            RaiseNetworkEvent(new DeadChatFailedEvent(ev.Sender, _deadChatFailed),
                args.SenderSession);

            return;
        }

        _repo.Add(new DeadChatCreatedEvent(entityUid, SanitizeMessage(ev), isAdmin));
    }

    private void OnAttemptEmote(AttemptEmoteEvent ev, EntitySessionEventArgs args)
    {
        if (!ValidateMessage(ev, args.SenderSession, out var reason, _emoteFailed, out CanEmoteComponent? comp))
        {
            RaiseNetworkEvent(new EmoteFailedEvent(ev.Sender, reason), args.SenderSession);

            return;
        }

        _repo.Add(new EmoteCreatedEvent(GetEntity(ev.Sender), SanitizeMessage(ev), comp.Range));
    }
```
A set of handlers process each type of attempt. These follow a pattern: validate, emit a failure event if validation fails, then input into the chat repository.

```cs
    /// <summary>
    /// Validates messages. Return true means the message is valid.
    /// </summary>
    private bool ValidateMessage<T>(EntityUid entityUid, T ev, ICommonSession player, out string reason) where T : ChatAttemptEvent
    {
        // This check is simple, so we don't need to raise an event for it.
        if (player.AttachedEntity != null || player.AttachedEntity != entityUid)
        {
            reason = _entityNotOwnedBySender;

            return false;
        }

        // Raise both the general and specific ChatValidationEvents. This allows for general
        var validate = new ChatValidationEvent<ChatAttemptEvent>(ev);
        RaiseLocalEvent(entityUid, validate);

        if (validate.IsCancelled)
        {
            reason = validate.Reason;

            return false;
        }

        var validateT = new ChatValidationEvent<T>(ev);
        RaiseLocalEvent(entityUid, validateT);

        if (validate.IsCancelled)
        {
            reason = validate.Reason;

            return false;
        }

        reason = "";

        return true;
    }
```
ChatValidationEvents, both abstract and specific, are raised to check each message.

```cs
    /// <summary>
    /// Validates messages which depend on a sentinel component to be legal.
    /// </summary>
    private bool ValidateMessage<T1, T2>(
        T1 ev,
        ICommonSession player,
        out string reason,
        string invalidCompReason,
        [NotNullWhen(true)] out T2? comp
    ) where T1 : ChatAttemptEvent where T2 : IComponent
    {
        comp = default;

        var entityUid = GetEntity(ev.Sender);

        if (!ValidateMessage(entityUid, ev, player, out reason))
        {
            return false;
        }

        if (TryComp(entityUid, out comp))
            return true;

        reason = Loc.GetString(invalidCompReason);

        return false;
    }

    /// <summary>
    /// Sanitizes messages. The return string is sanitized.
    /// </summary>
    private string SanitizeMessage<T>(T evt) where T : ChatAttemptEvent
    {
        var sanitize = new ChatSanitizationEvent<T>(evt);
        RaiseLocalEvent(sanitize);

        return sanitize.ChatMessageSanitized ?? sanitize.ChatMessageRaw;
    }
}
```
Different events are emitted to handle different kinds of work. Anything can subscribe to these messages and apply their own logic and context, without knowing about irrelevant implementation details.

```cs
using Content.Shared.Chat.V2;
using Content.Shared.Chat.V2.Components;
using Content.Shared.Radio;
using Robust.Shared.Prototypes;

namespace Content.Server.Chat.V2.Systems;

public sealed class RadioChannelValidationSystem : EntitySystem
{
    private const string RadioChannelFailed = "chat-system-radio-channel-failed";
    private const string RadioChannelKey = "channel";

    [Dependency] private readonly IPrototypeManager _proto = default!;

    public override void Initialize()
    {
        base.Initialize();

        SubscribeLocalEvent<ChatValidationEvent<AttemptEquipmentRadioEvent>>(OnValidateAttemptEquipmentRadioEvent);
        SubscribeLocalEvent<ChatValidationEvent<AttemptInternalRadioEvent>>(OnValidateAttemptInternalRadioEvent);
    }

    private void OnValidateAttemptEquipmentRadioEvent(ChatValidationEvent<AttemptEquipmentRadioEvent> msg, EntitySessionEventArgs args)
    {
        if (!_proto.TryIndex(msg.Event.Channel, out _) ||
            !TryComp<CanRadioUsingEquipmentComponent>(GetEntity(msg.Event.Sender), out var comp) ||
            !comp.Channels.Contains(msg.Event.Channel))
            msg.Cancel(Loc.GetString(RadioChannelFailed, (RadioChannelKey, msg.Event.Channel)));
    }

    private void OnValidateAttemptInternalRadioEvent(ChatValidationEvent<AttemptInternalRadioEvent> msg, EntitySessionEventArgs args)
    {
        if (!_proto.TryIndex(msg.Event.Channel, out _) ||
            !TryComp<CanRadioComponent>(GetEntity(msg.Event.Sender), out var comp) ||
            !comp.SendChannels.Contains(msg.Event.Channel)
        )
            msg.Cancel(Loc.GetString(RadioChannelFailed, (RadioChannelKey, msg.Event.Channel)));
    }
}
```
Here, two radio validators make sure radio messages have valid channels.

```cs
using Content.Server.Administration.Logs;
using Content.Server.Chat.Managers;
using Content.Shared.CCVar;
using Content.Shared.Chat.V2;
using Content.Shared.Database;
using Content.Shared.Players;
using Robust.Shared.Configuration;
using Robust.Server.Player;
using Robust.Shared.Timing;

namespace Content.Server.Chat.V2.Systems;

public sealed class ChatRateLimitSystem : EntitySystem
{
    [Dependency] private readonly IPlayerManager _playerManager = default!;
    [Dependency] private readonly IGameTiming _gameTiming = default!;
    [Dependency] private readonly IConfigurationManager _configuration = default!;
    [Dependency] private readonly IChatManager _chatManager = default!;
    [Dependency] private readonly IAdminLogManager _adminLogger = default!;

    private int _periodLength;
    private bool _chatRateLimitAnnounceAdmins;
    private int _chatRateLimitAnnounceAdminDelay;
    private int _chatRateLimitCount;
    private int _maxChatMessageLength;

    public override void Initialize()
    {
        base.Initialize();

        _configuration.OnValueChanged(CCVars.ChatRateLimitPeriod, periodLength => _periodLength = periodLength, true);
        _configuration.OnValueChanged(CCVars.ChatRateLimitAnnounceAdmins, announce => _chatRateLimitAnnounceAdmins = announce, true);
        _configuration.OnValueChanged(CCVars.ChatRateLimitAnnounceAdminsDelay, announce => _chatRateLimitAnnounceAdminDelay = announce, true);
        _configuration.OnValueChanged(CCVars.ChatRateLimitCount, limitCount => _chatRateLimitCount = limitCount, true);
        _configuration.OnValueChanged(CCVars.ChatMaxAnnouncementLength, maxLen => _maxChatMessageLength = maxLen, true);

        SubscribeLocalEvent<ChatValidationEvent<ChatAttemptEvent>>((msg, args) => OnValidationEvent(msg, args));
    }

    private void OnValidationEvent(ChatValidationEvent<ChatAttemptEvent> validationEvent, EntitySessionEventArgs args)
    {
        if (validationEvent.IsCancelled)
            return;

        if (IsRateLimited(GetEntity(validationEvent.Event.Sender), validationEvent.Event.Message.Length, out var reason))
        {
            validationEvent.Cancel(reason);
        }
    }

    private bool IsRateLimited(EntityUid entityUid, int messageLen, out string reason)
    {
        reason = "";

        if (!_playerManager.TryGetSessionByEntity(entityUid, out var session))
            return false;

        var data = session.ContentData();

        if (data == null)
            return false;

        var time = _gameTiming.RealTime;

        if (data.MessageCountExpiresAt < time)
        {
            data.MessageCountExpiresAt = time + TimeSpan.FromSeconds(_periodLength);

            // Backoff from spamming slowly
            data.MessageRateOverTime /= 2;
            data.NetMessageLengthOverTime /= 2;

            data.RateLimitAnnouncedToPlayer = false;
        }

        data.MessageRateOverTime += 1;
        data.NetMessageLengthOverTime += messageLen;

        if (data.MessageRateOverTime <= _chatRateLimitCount && data.NetMessageLengthOverTime <= _maxChatMessageLength)
            return false;

        // Breached rate limits, inform admins if configured.
        if (_chatRateLimitAnnounceAdmins)
        {
            if (data.CanAnnounceToAdminsNextAt < time)
            {
                _chatManager.SendAdminAlert(Loc.GetString("chat-manager-rate-limit-admin-announcement", ("player", session.Name)));

                data.CanAnnounceToAdminsNextAt = time + TimeSpan.FromSeconds(_chatRateLimitAnnounceAdminDelay);
            }
        }

        if (data.RateLimitAnnouncedToPlayer)
            return true;

        reason = Loc.GetString(Loc.GetString("chat-manager-rate-limited"));

        _adminLogger.Add(LogType.ChatRateLimited, LogImpact.Medium, $"Player {session} breached chat rate limits");

        data.RateLimitAnnouncedToPlayer = true;

        return true;
    }
}
```
Here, a validation handler makes sure that a sender is not spamming.

## Frontend Considerations

This document is almost entirely concerned with the backend implementation of chat. However, from exploration, there are a few considerations to take place:

1. It should not be too hard to bolt this new system on to the legacy frontend chat system, although this will need old and new code to live side-by-side for a while. Transformation between the new backend events and the old ChatMessage events, with their janky WrappedMessage fields and so on, will be necessary.
2. When building the new frontend system, it would be best to mimic the separation of concerns that the backend server code has implemented. The frontend chat management system is a large class that is exceptionally difficult to read. Reception, formatting and display should be broken apart into their own steps, with the former not assuming the implementation details of the latter.
3. It'd be really funny if shouting made your text bigger. I'm just saying. Bold is fine, but, like, size eighteen font would really sell that you're being loud.