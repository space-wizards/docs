# Diegetic Statpanels (aka PDA Statpanels)

| Designers | Implemented | GitHub Links |
|---|---|---|
| ike709 |  :x: No | WYCI |
## Concept

Taking all of the benefits of SS13 statpanels without ruining immersion nor reviving verb panels.
### SS13 Statpanels

Statpanels in SS13 generally serve one of three functions:

1. The Status tab informs players with a round timer, station clock, escape shuttle status, etc.
2. Debug-related info tabs like the Master Controller tab.
3. Verb tabs like IC or OOC which are just lists of verbs the player can run. 

The second item is unrelated to the average player. The third item is, frankly, terrible UX.

This design document is focused on the first item: the Status tab. I believe that certain basic information should be conveyed to the player *almost* always. This includes most of the information conveyed by the SS13 Status statpanel as previously mentioned: round timer, current map, station time, etc.

The problem with the Status tab in SS13 is that, frankly, it's ugly and it ruins immersion. It's particularly bad on codebases that just use the default BYOND statpanels instead of replacing them with TGUI. So how can SS14 do it better?
## SS14 Statpanels

It's simple. SS14 already has a mechanic that conveys all of this information: PDAs. All we need to do is open the PDA UI in the statpanel location when a PDA is equipped in the PDA slot.

Now in no particular order I'm going to address various considerations (many optional) involving mechanics, features, balancing, etc. all subject to player and maintainer input.

### What if I lose my PDA?

This should hide the UI, naturally. But replacing a PDA should be made trivial. PDA vendors should be added to areas such as Arrivals and Dorms that can supply people with simple, no-program unpainted PDAs if theirs is ever lost or stolen.

### What if I don't want to use the PDA programs in the HUD's corner?

Moving the PDA from the PDA slot to in-hand should move the UI from the corner to the center of the screen, and then put it back in the corner when the PDA is put back in the PDA slot.

### What if I don't want to see this UI at all?

Like in SS13, we could simply allow people to resize chat and shrink the statpanel by dragging the splitter upwards.

### Isn't constant access to Programs a bit overpowered?

I personally think this is a non-issue since you can't interact with the game window and PDA window simultaneously, but I can see how others would disagree so I came up with some potential solutions anyways. These are all optional and in no particular order:

- **Lockscreen**
	The PDA is "locked" by default, and the lockscreen is simply the Home tab. To access Programs, the player must do something such as:
	- Wait for arbitrary short doafter to represent typing in a passcode or biometric scanning
	- Actually needing to know and enter a 4-character PIN code each time it locks (it locks after brief periods of inactivity)
- **Require In-Hand**
	  Require having the PDA in the player's active hand to use programs. This is my least favorite option.
- **Require Empty Hand**
	  Require the player's active hand to be empty if they want to interact with programs. Just give them a popup text if they try to click programs with something in their hand.

### Optional: Admin Tabs/Programs

Add support for tabs and/or programs that are tied to the player's mind (or something) rather than the actual PDA. This would make it easy to support admin tools like a server performance monitor, a tab listing the gamemode and all antags, etc.

### Optional: Map Tab

My biggest complaint with the maps that aren't ripped straight from SS13 is that I have no idea where I'm going. Map terminals are great when I come across them, but I think having the ability to constantly have a map of the station would be a huge quality-of-life improvement for new players. Nothing stops them from just opening up a screenshot of the map in their browser anyways.

### Optional: Diegetic Game Settings

This is one of the spicier ideas, but out-of-character menus like the guidebook or the game's audio settings could be moved to a PDA tab. A big problem is that we'd need an elegant way to make sure the player can still access these if they lose their PDA.

## UI Mockup

Just remove the close button from the top right, maybe tweak the border a bit. It'd also need to stay there all the time when a PDA is equipped. Here's a pic ([direct link](https://i.imgur.com/ppnXXaf.png))

<img src="https://i.imgur.com/ppnXXaf.png" />

## tl;dr
([Direct image link](https://i.imgur.com/ByUHHZu.png))

<img src="https://i.imgur.com/ByUHHZu.png" />
