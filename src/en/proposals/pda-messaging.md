## PDA messaging program and server

[Julian, VasilisThePikachu, Unapproved]

*(Taken by [Julian doc](https://hackmd.io/iu2yK9bcQb-veuCOLl-FYw?both#Optional-Channels-and-Department-based-Channels) in hackmd and modified a lil. Mostly replacing "email" to "message", "Email address" to "user/user id" and adding some of my own twists. Julian was fine with this if i understood correctly (i was in vc with em))*

*(This is mostly taken from how PDA messages work in ss13)*
Allows sending messages to others using PDAs

### Message storage
Messages are stored on a server most likely will be stored in telecoms. There can be one server per station, others on the same station won't be used unless the first one loses power or gets destroyed.

*Optional* The active server synchronises itself with all of the inactive servers on the same station (This happens inside the system directly, no device networking here).

### One active / Multiple inactive server model

(This talks about some refactor stuff and Julian told me they forgot to paste the link, im keeping it to be safe in case its actually useful.)

The one active / multiple inactive server model uses the system that will get refactored into its own system from the crew monitoring server [link text]() 

The messaging client system will use the `GetActiveServer` method of the message server system to retrieve the active server if the client doesn't have a server set yet or that server timed out. *This is also from the system that gets refactored out.*

### Sending and receiving messages

When sending a message to someone via the program the PDA sends the message together with an 'user id' to the server and the server will send the message to the target device. 

When a PDA recieves a message it plays the PDAs ringtone and vibrates, showing the sent message on the chat. This message can also be viewed on the PDA via a program.

Notifications can be disabled if desired.

This user id could be generated into the ID card so that if you get a new PDA your messages are kept as long as you are using the same ID card. Potencially HoP can move your 'user account' to the new ID card rendering the old ID card useless. This can also prevent powergaming.

### Users list

When opening the PDA messaging app, you will be able to start a chat session with everyone connected to the server (aka everyone with a PDA)

They will be listed by name and job title like this "Vapor-Tail (Captain)"

*Optional* Add the ability for people to not be allowed to initiate a conversation with an option. This can be useful for high command staff like captain from getting message spammed by clown and others at the start of the shift.

### Optional: Detomatix PDA Cartridge

(find the original item in the tg wiki here: https://tgstation13.org/wiki/Syndicate_Items)

The detomatrix is... a zip bomb in easy to say terms. Allowing you to send a spoofed message that when opened by the target fast enough bricking the PDA and its ID (instead of exploding... even though thats funnier maintainers please allow this)

It will have a chance to fail and have an even lower chance of working on "high profile" PDA's like the Captains.

It could be used as a way to get people to turn off their messanger function in fear to not being up next if someone screams in radio about it and could be useful.

### Optional: Multiple network support

The server is able send on the wireless and the wired network because it saves what network the registered devices are on along with the user id and the network address.

This requires devices to be able to register themselves with two device net ids at once (which should only be done if it is really needed).

### Optional: Channels and Department based Channels
Channels are special groups that relay the messages sent to them to users who are subscribed to that channel.

Channels can be created and they can be deleted by the channel creator.

When registering to a server the client also sends the job of the inserted ID so the server can put them into special department channels.

Department channels can't be joined, left or deleted.

### Optional: RDs messager admin management console
The research director and potencially Captain get a console which connects to the message server via device net that can be used to view and manage all messages and groups.
It uses device net with an `AccessComponent` on the message server so the management functions can be hijacked by traitors that got their hands on an ID card with the right access. (This requires [device net access restrictions](https://hackmd.io/gPjP95_zRUiT-bX4hKxE6w) to be implemented.

### Optional: pAI as a chat assistant.
This will add new gameplay for the pAI ghost role. Allowing the pAI to chat as their master on their behalf. Could have a little pAI icon in the chatbox to show it was sent by the pAI and not the actual player. pAI's for a while have been kinda boring and may deserve their own design doc of ideas but this is one of my ideas that come to mind.
