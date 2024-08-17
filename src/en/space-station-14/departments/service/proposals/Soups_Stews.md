# Soups & Stews

| Designers | Implemented | GitHub Links |
|---|---|---|
| Moomoobeef | :x: | TBD |

## Overview

I want to add a system for chefs to make custom soups/stews, inspired by the [evolved cooking recipes of project zomboid](https://pzwiki.net/wiki/Cooking_(crafting)#Evolved_recipes). Pots, lids, and bowls will be added and chefs will be able to use these to make soups or to make stews with whatever ingredients they want to. After choosing their ingredients and cooking they will ladle the resultant into bowls for consumption.

## Background

Right now cooking is getting a lot of (exciting) additions, and this is an idea that has been kicking around my head for probably over a year. Seeing others making cooking PRs has given me the inspiration to finally make this doc. Similar to the current custom burgers system chefs will be able to add (almost) anything they want to a pot and turn it into a soup or a stew, and the ingredients they choose will affect the finished project. 

## Nitty Gritty

I'm intending to have custom layer sprites for different ingredients (for example, visible orange stuff for carrots, small peices of meat for the various meats etc.) and also have the color of the liquid behind the layer sprites change based on what is in it (so you could add hot sauce for a more reddish (and tasty :)) soup).

Chefs will have cooking pots to make their soups/stews in, and they can choose to put a lid on and cook it at low heat (on the grill) to make a stew, or lid off and cook it to make a soup. (difference will probably be pretty minimal/cosmetic, but it's neat for immersion. This could be cut if its too much work though) Afterward chefs will fill bowls, and depending on what is in the soup/stew it should look very different between one recipe and
