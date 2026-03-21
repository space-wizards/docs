# HOW TO CONVERT A SPECIES TO NUBODY

by mqole

```admonish info
This is an unofficial and incomplete guide. It will be updated and replaced with an official doc in the future.
```

All of these are guesstimates based on reverse-engineering nubody. if its wrong, its because I don't understand how nubody works.

NOTE: when i say Species in an entity name (eg AppearanceSpecies, MobSpecies) i am expecting this to be replaced with the actual name of the species (eg AppearanceDwarf, MobDwarf).

## QUICK CHECKLIST

Body/Species/species.yml should contain:

- [] MarkingsGroup
- [] AppearanceSpecies, modified from Body/Prototypes/species.yml
- [] MobSpecies, modified from Entities/Mobs/Species/species.yml
- [] External organs (formerly 'parts'), modified from Body/Organs/species.yml
- [] Internal organs, modified from Body/Parts/species.yml

You can then delete all the files you moved stuff out of:

- [] Body/Prototypes/species.yml
- [] Entities/Mobs/Species/species.yml
- [] Body/Organs/species.yml
- [] Body/Parts/species.yml

Species/species.yml should contain:

- [] Species. thats it

When modifying Species/species.yml, you should:

- [] Remove species `sprites`
- [] Remove species `markingLimits`
- [] Replace `dollPrototype` `MobSpeciesDummy` entity to `AppearanceSpecies` entity
- [] Delete `speciesBaseSprites`
- [] Delete `humanoidBaseSprite`s
- [] Cut out `markingPoints`, paste at the top of Body/Species/species.yml. This is our new MarkingsGroup

To update markings:

- [] Delete `markingCategory`
- [] Delete `followSkinColor`
- [] Rename `speciesRestriction` to `groupWhitelist`.

## Markings

This inherits from the `Undergarments` markingsGroup and defines the limits for what markings a species can have. numerical limits, bool requiremments, and default markings have more or less the same syntax as the previous `MarkingPoints`- just replace the humanoid visual layers with `enum.HumanoidVisualLayers.`whatever, and change `points` to `limit`.

You will need to seperate out arms and legs to LArm RArm etc etc. The limits on these got halved to compensate. I'm not sure how to handle species that use a single marking to modify both arms or legs at once unfortunately.

## Species appearance

Best I can tell this replaces the system connecting body parts to each other. This entity shouldinherit `BaseSpeciesAppearance`, and contain info about `InventoryComponent`, `InitialBodyComponent`, and `HumanoidProfile`.

`InitialBodyComponent`'s `organs` field has a dictionary of organ types corresponding to the mob's internal or external organs. If you need to define a new organ type, you can do that somewhere in a seperate yml file, much like the previous system.

`HumanoidProfile` is the replacement for `HumanoidAppearance`. Just change the name and call it a day

## The actual mob

Should inherit `BaseSpeciesMobOrganic` and the relevant species appearance. Everything on the old mob goes here, minus whatever you moved onto the appearance. Make sure you get rid of `InventoryComponent` specifically.

## Organs

So parts are also organs now. We're calling parts 'external organs' as opposed to the existing organs, which we call 'internal organs'.

You will need:

- [] OrganSpecies, inheriting OrganBase, with a species suffix
- [] OrganSpeciesMetabolizer, with MetabolizerComponent. You might not need this.
- [] OrganSpeciesInternal(brain, eyes, etc), inheriting OrganSpecies, sprite path to organs.rsi
- [] OrganSpeciesExternal (head, foot, etc), inheriting OrganSpecies, sprite path to parts.rsi
- [] OrganSpeciesVisual, inheriting OrganSpecies, with `VisualOrganComponent` and `VisualOrganMarkingsComponent`.

All organs (internal and external) you make should inherit either OrganSpeciesExternal orOrganSpeciesInternal depending on what you need, and also inherit the base organ for whatever is needed (OrganBaseFootLeft, OrganBaseAppendix, etc, follow that syntax). Put whatever components you need on these like you would for previous organs.

If you have a unique stomach, that should inherit OrganSpeciesMetabolizer. If you're just using an existing stomach, you don't need to make a new OrganSpeciesMetabolizer, just inherit one from whatever species you're using the metabolism group of.

OrganSpeciesVisual should have its `VisualOrganComponent` point to the parts.rsi, and its `VisualOrganMarkings` point to our earlier created marking group (can be 'None`). Eyes (and other internal organs that affect markings if you have them, I guess) should also inherit OrganSpeciesVisual. 

## Markings

You can just delete `markingCategory` and `followSkinColor`, and rename `speciesRestriction` to `groupWhitelist` and you should be okay. Unfortunately there's nothing upstream with custom visual layers so I'm at a loss there.

## Custom layering orders

dont ask me bro i barely undertsand that shit
