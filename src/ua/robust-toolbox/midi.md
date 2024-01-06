# MIDI

### Regarding crackling / "Crunchy audio"

So basically, MIDI in SS14 works like this:
We have x buffers of y length each. MIDI synthetizing/rendering occurs in another thread, on a loop. We fill as many buffers as there are available in each iteration. 
This means that there *will* always be some latency when using MIDI input.
OpenAL plays back the buffers in real time as long as there's one buffer filled with data.
But what happens if OpenAL plays back buffers much faster than we can fill with data?
The audio becomes crunchy.

------------

### Custom instruments and you
Any soundfonts found in `Resources/MidiCustom` will be loaded automatically into new MIDI renderers. This means you can easily create your own custom instruments to be used in-game! Just remember *not* to use bank 0, as it is reserved for [General MIDI 1](https://en.wikipedia.org/wiki/General_MIDI).
Currently, we have a custom soundfont called `space-station-14.sf2`.
Ideally, you should add new instruments to it instead of making new soundfonts for adding single instruments.

#### List of custom instruments

| Bank | Program |   Name    |
|:----:|:-------:|:---------:|
| 001  |   001   | Bike Horn |
| 001  |   002   | pAI Synth |
| 001  |   003   | Euphonium |


#### Soundfont editing programs
- https://www.polyphone-soundfonts.com/
- http://www.swamiproject.org