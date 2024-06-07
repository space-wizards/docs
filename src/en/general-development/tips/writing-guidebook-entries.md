# Writing Guidebook Entries

The guidebook is a powerful tool for communicating more obscure in-game information to players without forcing them to travel to an external wiki. Moving forward, most information should be moved from the wiki to the guidebook in some form.

This guide explains how to write a guidebook entry and set it up in game as well as provides helpful tips for creating good quality entries. Afterwards, if you want to learn how to make a pull request for your new entry, check out [Git for the SS14 Developer](../setting-up/git-for-the-ss14-developer.md).

## Writing Guides

Guide entries are made of two parts, an `.xml` file for the contents of the guide and the YAML prototype which defines its metadata. 

We will first go over the `.xml` file, which makes up the actual content of the guide.

All guide entries are stored in the `/Resources/ServerInfo/Guidebook/` path in the main repository. 

The file structure of the guides themselves should roughly correspond to the structure of the entries themselves, though this is not required. The most important aspect is just making sure the files are roughly organized.

The entries themselves are essentially plain text files with some additional tags that are used for styling. The only part of an entry that is required is the `<Document>` tag.

``````admonish example title="Minimal Entry Example" collapsible=true
Thus, the simplest Guidebook Entry would be:

```xml
<Document>
</Document>
```
``````

### Guidebook Writing Best Practices

1. **Keep titles clear and concise**. Players don’t want to search around for what they need.
2. **Use boxes, embedded entities, and text colors to give entries visual interest**.
    - A commonly used color for emphasis is #a4885c, which is a goldish-brown.
3. **Refrain from including specific advice and “meta” strategies**. The guide should be an impartial source of information.
4. **Keep entries short. You can always add child entries if you want to elaborate more on the topic**.
5. **Articles should be written in a neutral tone**.
6. **Encourage interacting with the guide**.
    - If your embedded entities support it, suggesting that the player examines the entity to learn more is a helpful way of communicating information and teaching players.    

``````admonish example title="Completed Entry Example" collapsible=true

A completed Guidebook entry should look something like this:

```xml
<Document>
# Diona

<Box>
    <GuideEntityEmbed Entity="MobDiona" Caption=""/>
</Box>

They can't wear shoes, but are not slowed by Kudzu.
They get hungry and thirsty slower.
Their "blood" is normal water and can't be metabolised from Iron.
Being plants, Weed Killer poisons them, while Robust Harvest heals them (but not without risk when overused!)

They take [color=#1e90ff]30% less Blunt damage and 20% less Slash damage[/color];
but [color=#ffa500]50% more Heat damage, 20% more Shock damage, and they can easily
catch on fire when receiving enough Heat damage from *any* source.[/color]

## Make Like A Tree And Leave

<Box>
    <GuideEntityEmbed Entity="FloraTree06" Caption=""/>
</Box>

Being exposed to too much Robust Harvest will cause a Diona to grow out of control, turning into an immobile tree (dropping all their equipment).
Cutting down the tree will "restore" the Diona to their mobile state.

## Diona Nymphs

<Box>
    <GuideEntityEmbed Entity="MobDionaNymph" Caption=""/>
    <GuideEntityEmbed Entity="MobDionaNymph" Caption=""/>
    <GuideEntityEmbed Entity="MobDionaNymph" Caption=""/>
</Box>
After death, a Diona can voluntarily destroy their own body, releasing their "internal organs" as three Nymphs,
with the player taking control of the Brain Nymph.
It can talk but has no hands or inventory, and can't do much.

After 10 minutes, a Nymph can reform into a whole Diona. This will be a new randomised body with a random name,
and there will be little to no evidence beyond their word about who they were before.

</Document>
```
Source: [`/Resources/ServerInfo/Guidebook/Mobs/Diona.xml`](https://github.com/space-wizards/space-station-14/blob/9d2b4ed3b22e548f02aeee7caa855b65b37dda24/Resources/ServerInfo/Guidebook/Mobs/Diona.xml)

``````

## Guidebook Markup

Any text written in the bounds of the tag will be displayed plainly on the guide. 

But, if you write a guide with only plain text, you will write an incredibly boring guide that will make anyone's eyes glaze over.

To alleviate everyone's oncoming death, consider using the (small) variety of markdown tags that are supported:

1. `#` Makes a title
2. `##` Makes a heading
3. `-` Creates a list entry
4. `[color=hex][/color]` Colors the text inside the tags with the specified hex color.

### Extra Guidebook Controls

These are custom "controls" (or, ui elements) that can be used to add unique visuals or behavior to a guide. 

Some are more useful than others, but consider using some or all of them to add more visual interest and more specific information to a guide:

```admonish note
The API docs were intentionally removed from this section as the Guidebook has been changed pretty frequently lately and including possibly outdated API docs doesn't sound like a good idea. 
```

1. `<Box>` center-justifies its content.
2. `<CommandButton>` embeds a button in the guidebook, with clicking it executing a command. This is primarily for executing commands that open up more menus.
3. `<GuideEntityEmbed>` embeds in-game prototypes into the guide, which may include being able to interact or examine them. This is usually used to embed a sprite or an image in the guide.
4. `<GuideReagentEmbed>` embeds a small descriptive box about a reagent.
5. `<GuideReagentGroupEmbed>` embeds a group of reagents, allowing for a whole category to be listed without manually updating the guidebook.


## Creating Entries

Now that you’ve created a file with all of your content, you need to make an entry for it to display in game. 

Entries are prototypes found in the `/Resources/Prototypes/Guidebook/` directory. Like before, try to group guides and their children together so that they can be easily found.

Each entry consists of a single prototype with a few different variables you can set.

``````admonish example title="YAML Prototype Example" collapsible=true

Here is the respective YAML prototype for the previous example: 
```yaml
- type: guideEntry
  id: Species
  name: guide-entry-species
  text: "/ServerInfo/Guidebook/Mobs/Species.xml"
  children:
    - Arachnid
    - Diona
    - Dwarf
    - Human
    - Moth
    - Reptilian
    - SlimePerson

- type: guideEntry
  id: Diona
  name: species-name-diona
  text: "/ServerInfo/Guidebook/Mobs/Diona.xml"
```

Source: [`/Resources/Prototypes/Guidebook/species.yml#L1-L22`](https://github.com/space-wizards/space-station-14/blob/9d2b4ed3b22e548f02aeee7caa855b65b37dda24/Resources/Prototypes/Guidebook/species.yml#L1-L22)
``````
To make sure that it appears in the guidebook, you’ll need to also add it as the child to another entry 
- In the previous example, it is a child of `ss14.yml`, the root Guidebook entry.

```admonish tip "Emo's tip"
Now that you have written your entry created the prototype, you can now open up the guidebook and view it.

Guide entries support hot-reloading, which means that you can modify the file while your local server is running, close the guidebook, reopen it, and see your changes.
```

The API is actually pretty simple, and here it is:

- `id`: This is simply a unique prototype Id. Just make sure it roughly corresponds to your guide’s name.
- `name`: This is a the name which appears in the file view sidebar of the guidebook. Importantly, it’s a locale string, which is used for translation. It’s also the only part of a guide entry that needs to have a locale string.  
    You can learn more about localization in the [localization guide](../common-tasks/localization.md).
- `text`: This is just a file path to the entry, starting from the `/Resources/` directory.
- `priority`: This is a numeric value for sorting top-level guides. Higher values will appear first. If they are not a top-level guide, then they are sorted by the order of their children.
- `children`: This is a list of all other guide entries that appear below this one in the guide sidebar. The items in this list must correspond to the `id`s of other guide entries.

## Further In-Game Integrations

Guidebooks are only useful if people actually _see_ them. 

One such way that we can force it into the faces of people is through the `?` (question mark) box that appears when someone examines an entity.

This is done via the `GuideHelp` component, which you can include in your entity to reference the guidebook.

``````admonish example title="GuideHelp Example" collapsible=true

An example with the `GuideHelp` component:

```yaml
- type: entity
  parent: BaseItem
  id: LogProbeCartridge
  name: LogProbe cartridge
  description: A program for getting access logs from devices
  components:
    - type: Sprite
      sprite: Objects/Devices/cartridge.rsi
      state: cart-log
      # ... truncated ...

    # Add this:
    - type: GuideHelp
      guides:
        - Forensics
```

Source: [`/Resources/Prototypes/Entities/Objects/Devices/cartridges.yml#L73-L95`](https://github.com/space-wizards/space-station-14/blob/9d2b4ed3b22e548f02aeee7caa855b65b37dda24/Resources/Prototypes/Entities/Objects/Devices/cartridges.yml#L73-L95)

``````