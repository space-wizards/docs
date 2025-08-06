# Vulpkanin Species

| Designers | Implemented   | GitHub Links                                                                      |
|---|---------------|-----------------------------------------------------------------------------------|
| ScarKy0 | :x: Partially | [Implementation PR](https://github.com/space-wizards/space-station-14/pull/37539) |

## Overview

This proposal plans to add a new "Vulpkanin" species as a playable roundstart species.
They are meant to be a species of humanoid canine-like beings, mainly oriented around their customizability and unique abilities or traits.

## Background

Vulpkanin are one of the fan favourites on many downstream projects, as well as plenty popular in Space Station 13.
Their addition to the upstream was brought up many times, which was always happily welcomed as long as there is a valid design document.
Additionally, Vulpkanin were rated very positively by players during their [temporary release during the 2025 April Fools event.](https://github.com/space-wizards/space-station-14/pull/35395) Meaning this species was tested and was already shown to be very fun to play as.
However, this document is meant to also expand on the initial implementation to make them stand out in their own way from the other species available.

## Design

Vulpkanin by design are supposed to be able to stand in for any canine-like species with few defining traits of their own, without providing any major changes to the experience.
The main things that need to be brought up here are their customizability and defining features.

### Customizability

Vulpkanin, as stated previously, aren't meant to only represent a single canid. Rather instead focusing on being able to fit into several canine-like races by selecting from many diffrent markings. This includes things like ear shapes, tails and fur patterns.
The idea is that the player is able to mix and match those options to create many unique looking canine characters, which could include foxes, jackals, wolves and so on without the need create any additional sub-species with similiar traits.

### Defining Features

#### Cold Resistance

Due to their fur, Vulpkanin are naturally more resistant to colder climates. This allows them to natively resist cold damage, but also grants heat insulation (which works in a similiar way to winter clothing, with weaker properties).
Naturally, due to heating up faster, they are also weaker to heat, making fire and laser weaponry deadlier as well as difficulty to use things such as cryo-medicine.

#### Sniffing

With their sensitive noses, Vulpkanin are able to sniff reagents to identify what they are. The effect is meant to similiar to how Chemical Analysis Goggles do it, perhaps tweaked to set them apart if that is neccessary.

#### Leap

Mainly intended as a flavor ability, Vulpkanin will have an ability to leap a short distance, being knocked to the ground upon collision with a player or a wall.
The intent is for this ability to be the "defining trait" of the species. It is not intended to be used for combat or ease of traversal, and will therefore need to be balanced as such.
Instead, the plan is to introduce something allowing for silly situations or roleplay. For example, getting scared and jumping into a wall before falling to the ground, or leaping at a friend only to trip in front of them.

#### Melee

Naturally, canines have sharp claws and teeth. Vulpkanin will deal a mix of slash and pierce with their melee attacks. This leads to increased bleed from their attacks, however causes them to be weaker against targets who are resistant to both.

#### Colorblindness

While not a trait directly tied to Vulpkanin, they could make for a nice way to add traits for colorblindness, such as Deutranopia (which is how dogs see in real life). **This is not meant to be permanently tied to the species, instead a selectable trait in the menu.**

#### Unique Sounds

Many species currently have unique sounds and emotes. Most notably tail thumps and chitters. Vulpkanin would get canine-like sounds, such as barks, howls and whines. These, of course, would be also tied to unique emotes in the emote wheel.

#### Messy Drinking

Dogs tend to spill water everywhere when they drink, which makes for a very funny feature to add to this species. It should not cause active difficulties drinking, but remain as a silly bit of flavor.

## Why Vulpkanin?

With their pointed ears and big tails, Vulpkanin are visually distinct from every other species while also being quite taller.
They introduce several updates to existing systems to allow them to work directly on entities, as well as few new ones to allow for messy drinking or future traits such as colorblindness.

Currently the game lacks diversity in species, which has been brought up by players many times.
Introduction of Vulpkanin is not meant to be a game-changing additon, instead focusing on simple differances that allow them to stand out in their own way, giving players an additional choice they are able to pick for more variety in gameplay or simply because of their unique appearance.
A very good reason is the fact Vulps have been tested both on Wizden servers as well as in downstream projects. Their positive reception shows that they would make a good fit for upstream, with a few tweaks.