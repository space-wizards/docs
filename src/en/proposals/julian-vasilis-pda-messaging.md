## PDA Messaging

| Designers | Implemented | GitHub Links |
|---|---|---|
| Julian & VasilisThePikachu |  :x: No | TBD |

*(Taken by [Julian doc](https://hackmd.io/iu2yK9bcQb-veuCOLl-FYw?both#Optional-Channels-and-Department-based-Channels) in hackmd and modified a lil. Mostly replacing "email" to "message", "Email address" to "user/user id" and adding some of my own twists. Julian was fine with this if i understood correctly (i was in vc with em))*

*(This is mostly taken from how PDA messages work in ss13)*
Allows sending messages to others using PDAs

### What this adds and why
Simple, Messaging via the PDA!
Messaging someone via the PDA should be made when you need to get the attention of a special someone. Example as HoS you want to ask detective to come over to investigate an item. It's easier to get their attention cause of their PDA vibrating then hoping they are monitoring their channel. Another usage is the heads planning Captain a suprise birthday party. Something like that would require all heads getting together in one place.

This is **not** a replacement to the radio channel. Theres no "common" channel, it would be easier to spoof being someone (just need their id), past messages on that same id can easily be exposed and its far more cumbersome to message someone over PDA then just using the radio.

### Message storage
Messages are stored on a server most likely will be stored in telecoms. There can be one server per station, others on the same station won't be used unless the first one loses power or gets destroyed.

*Optional* The active server synchronises itself with all of the inactive servers on the same station (This happens inside the system directly, no device networking here).

### One active / Multiple inactive server model

(This talks about some refactor stuff and Julian told me they forgot to paste the link, im keeping it to be safe in case its actually useful.)

The one active / multiple inactive server model uses the system that will get refactored into its own system from the crew monitoring server [link text]() 

The messaging client system will use the `GetActiveServer` method of the message server system to retrieve the active server if the client doesn't have a server set yet or that server timed out. *This is also from the system that gets refactored out.*

### Sending and receiving messages

When sending a message to someone via the program the PDA sends the message together with an 'user id' to the server and the server will send the message to the target device. Of course there will be a character limit (say... 100 characters?)

When a PDA recieves a message it plays the PDAs ringtone and vibrates, showing the sent message on the chat. This message can also be viewed on the PDA via a program.

Notifications can be disabled if desired.

This user id could be generated into the ID card so that if you get a new PDA your messages are kept as long as you are using the same ID card. Late joiners will get assigned a uid when they arrive on the station. Potencially HoP or RD can move your UID to the a new ID card with the ID comnputer rendering the old ID card useless. This can also prevent powergaming by someone changing their UID to see others messages.

This UID will receive messages for as long as it is in the station and in a PDA.

If its not in station the messages can either fail to send or be added in a queue to be sent when it reenters the station.

Since the UID is stored on the ID. That means that if you manage to get your hands on someones ID you can chat as them and potencially (if added) read their messages.

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


### Concerns
When initially asked about this I was met with some concerns. This section is to address them

Discord discussion start: https://discord.com/channels/310555209753690112/310555209753690112/1160244698112327830

##### Why PDA messaging over plain radio? Would this upset radio balance and reduce coms over radio?
First of all why:
If you play the game you can quickly realise how getting someone's attention god forbid multiple, can be... not an easy task to say the least. You either are lucky and the person you want is just so happening to be monitoring the chatbox or they are busy and not paying attention. In the end missing your message until you resend it or try to look with them. This is just not fun and is just annoying. PDA messaging can solve this.

As to if it will upset radio balance: Highly unlikely it will be. Mostly cause:
1. PDA messaging wont let you get the attention of multiple people at once (common). PDA messaging can reach one person at the time (unless we get department groups but even then). You will have to jump through a lot of hoops if you JUST wanna use messaging. Radio is easier and faster to talk into and gets to multiple people at once.
2. Sending a PDA message is more of a chore then just using the radio channel, PDA messaging will at least need a minimum of 6 steps to open the PDA, go to the app section, start the app, find the person, write the message and send. And if you keep the chatbox on it would just take up a good chunk of your screen. Or you could just do ":c Captain hamlet ate uranium"
3. Messages are stored and logged. Someone steals caps PDA? Well now all of their messages are up on display. With radio unless they had command channel already they would never learn of any past messages. If two syndies decide to use PDA messaging rd can just grab their chatlogs. Same with syndies using it to communite with others.
4. PDA messaging has a pretty small character limit, if you wanna say something long radio is the place.

May be the wrong section but admins can also use this to act as "Central Command" so instead of having to subtile message someone they can just send a message to their PDA.

##### It reduces everyone else's situational awareness since people can't see all radio messages anymore.
I highly disagree, I doupt it will reduce situational awareness more then it already is. I have already went over how someone monitoring the radio channel for messages directed to them is already a chore. PDA messaging names can easily be changed by using someone elses ID therefore its a good idea to not go to maints like they told you to and instead show the message to security.

##### Why not use fax?
Is this really a question? First of all not everyone has a fax, second you have to be close to hear it go off printing. And unless you check your fax periodicly for new faxes messages can be missed. And even if you do check it its probably boykisser ASCII spammed 10 times. Also why are we using *faxes* in 2563 or whatever year SS14 takes year in.

These were all the conserns I could find from discord.
