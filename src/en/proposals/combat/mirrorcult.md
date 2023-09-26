# Combat Rework [mirrorcult, Unapproved(?)]

The goals of this rework:
- Remove the disarm toggle. It's jank as fuck, the only modal interaction should be with combat mode.
- Make it harder to accidentally be in combat mode by introducing an optional 'hold to activate' keybind.
- Introduce more variety to combat mode interactions--alternative interactions (which disarm will be one of)
- Make wideattacks more useful and the 'default'. Reduce the distinction between wideattacks and clickattacks somewhat. Also nerf wideattacks slightly.

To that end:

## More Modality / More Obvious

Less interactions in combat mode should work. Things like:
- activate in world
- examining (this also allows for walking while attacking which is nice)
- maybe even context menu? 

This keeps the modal distinction obvious and makes it harder to miss. It also allows for other combat-mode-specific interactions to be placed on keys that used to just be normal things, which makes the distinction even more obvious. Ideally combat has its own separate input context entirely.

A more modal combat mode allows for significantly more complex and varied combat, as opposed to just a clickfest (see alt combat interactions below).

## Hold to Activate

A button/key should be introduced where, while held, combat mode is active, and normal control is returned when the button is released.

This is separate from a toggle keybind, which will still exist, as it's quite useful and most people will want it anyway.

A 'hold' keybind is, in my opinion, far more intuitive, and it makes it essentially impossible to ever accidentally be in combat mode. Depending on its placement, it can potentially work as a psychological parallel with common keybinds in other games

Some proposed defaults for this keybind:

### Right click 
Press to view context menu, hold to enter combat mode

Pros:
- Intuitive parallel with the ADS key in most games (suggested by Rane)
- Easy to access, and common enough that it'll be useful to access

Cons:
- Slightly jank implementation with context menu
- Uses up a valuable keybind slot


### Spacebar

Pros:
- Already used as a key for combat now, so its easy for people used to that
- Also easy to access-thumb on the left hand

Cons:
- **Can't alt+click and press spacebar at the same time**

## Alternative Combat Interactions

Alt+click while in combat mode will perform an alternative combat interaction.

Alt combat interactions will include things like:
- Disarming (alt while unarmed)
- Special moves for melee weapons (slow swipes rather than stabs?)
- Blocking/parrying with sabres
- Alternative fire for guns (grenade launcher attachment?)

These are pretty intuitive and add a lot more variety to combat while keeping it relatively simple.

## Wideattack / Clickattack Rework

- Remove the spacebar key for wideattacks.
- Clicking on an entity directly in combat mode performs a click attack.
- Clicking not on an entity in combat mode performs a wide attack in that direction.

This still leaves a distinction between wideattacks/clickattacks, and also makes it much easier to hit or threaten people by just clicking on them (since even if it misses it'll do a wideattack). Less keys to have the same functionality is also always nicer, and spacebar was weird enough that a lot of people didn't even know wideattacks existed.
