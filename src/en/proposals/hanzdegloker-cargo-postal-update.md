# Cargo Postal Update

Your title should convey the basic jist of your proposed changes. It should be short because the text will be linked in the sidebar.

| Designers | Implemented | GitHub Links |
|---|---|---|
| Hanzdegloker | :x: No | TBD |

## Overview

This update shoots to add postal elements to the game alla la letters, packages and such. Giving the role of deliverying such postal stuff
to the cargo techs to try and give them more stuff to do. Not to mention a new event which should occur at least thrice, maybe four times
during an event where random packages and letters will spawn on the trade station with random recipients and contents. This not only gives 
something for cargo techs to do, it invites a neat sense of randomness. Perhaps grandama sent you a cookie! or an unknown malfactor sent you a
KNIFE!

## Background

https://github.com/space-wizards/docs/pull/141

I was previously enthralled with the idea of a courier to push fourth this new system of letters and packages. Although seeing the state of 
the cargotech instead I shall try and implement the systems into them. There is already a precedent, with mail rooms (some even without mail
chutes!) existing on maps connected right to cargo. Of course also only already accessabily by cargotechs and above, it works out! Now what if 
we truly fleshed out these mail rooms and mail in general to allow for rp oppertunities, more varied rounds and for a lack of a better term more 
work for the cargo techs outside of their usual schtick.

## New items / events

Envelope / Letters: An Envelope is a small storage item with a L grid of single boxes meaning up to 3 papers can be contained. Paper and small items 
within reason can be stored within letters ie. a screwdriver, a pen, some money, etc. They can be sealed which promps writing a "To" and a "From". 
Once sealed an envelope becomes a letter. Letters can be stamped, no long opened and appear as a "Sealed Letter" displaying the "To" and "From". They can be opened 
in which the player rips the letter opened turning it to a trash item and allowing for the items to be retreived out of it. It cannot be stamped post
opening although the "To" and "From" can still be checked. An letter / envelope itself takes up 1x2 space in a player's inventory. The reasoning for the L shape
in single boxes is to allow for a small item that is 2x1 such as a screwdriver to be sent alongside a paper without leaving enough room to say, store 2 screwdrivers,
lest we allow it to become a nested form of storage. This still allows for a very common letter bound gift, a nice letter (1x) and some money from grandma (1x2)

Packages: Uses the exact same system as described previously, you get an empty package and put what you'd like to send inside. Seal it, prompted for a "To"
and a "From", and then it becomes trash once opened. The package takes up 3x3 in your inventory, as well itself having a 3x3 storage just like the emergency 
survivial kit. Packages have no limit on the type of items that can be contained, and will be the goto for sending a gift or important item. The package like the 
letter can be stamped once sealed, but not after opening. Likewise you can still read the "To" and "From" once opened. I will note this here also the letter / envelope
can be burnt as well as the package.

Mail Dropbox: A "mail dropbox: is a new wall mounted machine that takes in letters and packages only. Simply interacting with it while holding either will insert it and
send it on it's way. The letter and or package is immediately sent to the "mail drop box output" which spits it out, the output is also wall mounted. This allows for players
to easily drop off packags and or letters that need to be sent over at cargo, less they clog up the sometimes already long line of people who want steel. The mail dropbox output
should be over a table so the contents can neatly fall ontop of it and be processed by cargo techs, delivering them as they see fit.

Mail Shipment Event: Now this is some real fun right here, the Mail Shipment Event. At a randomized interval, which should total to around 2-3 times per shift. Mail shipments shall
appear on the trade station for cargo techs to grab and bring to the station proper and deliver. These shipments will be 1/3 letters 2/3 packages roughly, and be assigned randomly to
anybody on the station so long as they are not catatonic or SSD. Yes this means dead people with a soul can get mail! Yes it is intended! Mail takes a while and who are they to know
they perished? The no SSD or Catatonic fellas (disconected) means we can at least avoid a cargo tech meekly placing a letter on an unmoving persons. The dead can collect their mail
once they are revivied though! Now for the contents! Letters can range from just a paper or advertisement, a paper and a little something something not too crazy or perhaps some cold
hard cash! Packages have a much wider range of items, from the mundane and worthless to extremely rare and useful! These letters and packages would be labeled as from random people
ie. Grandma, Centcomm, Billy Bob, etc. Each Mail Shipment would come as an alert to the whole station, and the box itself would be cargo tech locked. The shipment would contain the 
ratio perviously discussed of 1/3 letters to 2/3 packages and there should be mail for roughly 6-9 people. 

## Admin Usage

Ever saw the saddest syndicate the world over and wanted to give a helping hand? and or just wanted to spicen up a round? But then issue arrises of "I can't just spawn stuff and give
it to them". Well now with the Mail Shipment event you too can foribly set a custom package to arrive in the next Mail Shipment to perhaps give susie that lizardplushie she's always wanted.
Of course you could wait patiently ORRRR hit the command to immediatly summon a Mail Shipment Event in which your custom admin care package shall be delivered with. This allows for in game
gifting of key items for special events or whatever reason really. Between this and mysterious letters, who knows what fun shenanigans you could get up too!
