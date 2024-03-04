# MIDI

## Regarding crackling / "Crunchy audio"

So basically, MIDI in SS14 works like this:
We have x buffers of y length each. MIDI synthetizing/rendering occurs in another thread, on a loop. We fill as many buffers as there are available in each iteration. 
This means that there *will* always be some latency when using MIDI input.
OpenAL plays back the buffers in real time as long as there's one buffer filled with data.
But what happens if OpenAL plays back buffers much faster than we can fill with data?
The audio becomes crunchy.

## Custom instruments and you
Any soundfonts found in `Resources/MidiCustom` will be loaded automatically into new MIDI renderers. This means you can easily create your own custom instruments to be used in-game! Just remember *not* to use bank 0, as it is reserved for [General MIDI 1](https://en.wikipedia.org/wiki/General_MIDI).
Currently, we have a custom soundfont called `space-station-14.sf2`.
Ideally, you should add new instruments to it instead of making new soundfonts for adding single instruments.

### List of custom instruments

| Bank | Program |   Name    |
|:----:|:-------:|:---------:|
| 001  |   001   | Bike Horn |
| 001  |   002   | pAI Synth |
| 001  |   003   | Euphonium |


### Soundfont editing programs
- https://www.polyphone-soundfonts.com/
- http://www.swamiproject.org

## Soundfont loading behavior

Robust itself only ships a tiny built-in `fallback.sf2` soundfont, which is not suitable for playing back different instruments. Soundfonts are instead automatically loaded from standard locations in the operating system. This section will describe the exact process, for debugging purposes (and if you want to use a custom soundfont as a player).

Thanks to the underlying FluidSynth library, Robust can load soundfonts in `.sf2`, `.sf3` and `.dls` formats.

Soundfont loading happens in different stages. Soundfonts loaded in a later stage can replace instruments loaded from earlier soundfonts, if applicable.

### Stage 0: fallback soundfont

The `/Midi/fallback.sf2` soundfont, included in Robust, is loaded before everything else.

### Stage 1: operating system soundfonts

Robust will automatically try to load a soundfont from a standard location in the host operating system. The file paths are as such:

* Windows: `%SystemRoot%\system32\drivers\gm.dls`
* macOS: `/System/Library/Components/CoreAudio.component/Contents/Resources/gs_instruments.dls`
* Linux (all paths are tried, in order. note that you may need to install distro-specific packages for these to be available):
    * `/usr/share/soundfonts/default.sf2`
    * `/usr/share/soundfonts/default.dls`
    * `/usr/share/soundfonts/FluidR3_GM.sf2`
    * `/usr/share/soundfonts/FluidR3_GM2-2.sf2`
    * `/usr/share/soundfonts/freepats-general-midi.sf2`
    * `/usr/share/sounds/sf2/default.sf2`
    * `/usr/share/sounds/sf2/default.dls`
    * `/usr/share/sounds/sf2/FluidR3_GM.sf2`
    * `/usr/share/sounds/sf2/FluidR3_GM2-2.sf2`
    * `/usr/share/sounds/sf2/TimGM6mb.sf2`

### Stage 2: environment variable

If the `ROBUST_SOUNDFONT_OVERRIDE` environment variable is set, Robust will load it as a sound font as well.

### Stage 3: content soundfonts

Content can provide additional soundfonts to be loaded, by including them in the `/Audio/MidiCustom/` resource directory. They will be automatically loaded here.

### Stage 4: user sound fonts

Users can provide extra sound fonts in their [user data directory](user-data-directory.md), under the path `/soundfonts/`. All sound fonts in this directory (if it exists, it is not created by default) will be loaded.
