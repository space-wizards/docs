# Scripting Tutorial

Ever see those admins who spectate then immediately shorten or grow, get colored, and starts flying around real fast, all at the same time? We’re learning how to script, baby. 

A script is a series of commands that you tell the game to run. You can add as many commands as you want. There are multiple use cases for scripts, and are amazing for automating tasks that don’t require editing in-between uses.

To get started, type %appdata% in your search bar and scroll down to find Space Station 14. In case you’re already lost, the directory’s location is \AppData\Roaming\Space Station 14\data. If you’re not on windows, you’ll have to find that folder yourself. Anyways, open the data folder, and create a text file (.txt). Literally any name works, but you’ll be typing that name in the console, so make sure you can recognize it. You can make as many scripts as you want. Put your script in that file. Once you have every command you want in your script, run exec with the /filename to run your script. exec has autocomplete.

## Examples
### Basic aGhost Script
This script relies on toolshed to fill in the entity’s ID by running “self” first. Here’s nikthechampiongr’s “generic username agnostic script”:

> self not prototyped AdminObserver do "aghost"
> self do "vvwrite entity/$ID/MovementSpeedModifier/BaseSprintSpeed 25"
> self do "vvwrite entity/$ID/MovementSpeedModifier/BaseWalkSpeed 6"
> self do "vvwrite entity/$ID/Description \"GHOST GANG!\""
> self do "vvwrite entity/$ID/Eye/VisibilityMask 7"
> self do "vvwrite entity/$ID/Ghost/color '#4D7AFF'"
> self do "addcomp $ID ShowCriminalRecordIcons"
> self do "addcomp $ID ShowJobIcons"
> self do "addcomp $ID ShowMindShieldIcons"
> self do "addcomp $ID ShowSyndicateIcons"

### Entity Itemization
Here is a script by aquif that itemizes a marked entity (which you need to mark by right-clicking an entity > admin > mark):

> marked comp:ensure Item
> marked comp:ensure MultiHandedItem
> marked comp:ensure CanEscapeInventory

For this script, you should be adding an entity size. This command changes based on what kind of inventory your server has:

Size for list inventory servers: > marked do "vvwrite /entity/$ID/Item/Size 120"
Size for grid inventory servers: > marked do "vvwrite /entity/$ID/Item/Size Normal" for a 2x2 tiled item, or use Ginormous to be too big for bags. Inspect the item component of other items for more sizes.

### Make All Ghosts Rainbow

This is a singular command, however making it into a script has us write a lot less words than writing the whole command (ex: exec /RGBALL.txt)

> entities with Ghost comp:ensure RgbLightController comp:ensure PointLight do "vvwrite /entity/$ID/PointLight/Energy 0"