# Admin Cookbook

## Delete PA & Singularity Generator
```
    entities named "PA .*" do delete $ID
    deleteewi SingularityGenerator
```
## Add power to the station permanently
`Admin menu -> objects -> select grids in dropdown -> right click the station -> tricks -> click the battery with the ∞`
## Uncurse all lockers
`entities with CursedEntityStorage do rmcomp $ID CursedEntityStorage; addcomp $ID EntityStorage`
## Remove all ghostroles
`entities with GhostTakeoverAvailable do rmcomp $ID GhostTakeoverAvailable; rmcomp $ID Mind`
## Clean up assorted body parts
`entities with MapGrid children with BodyPart do delete $ID`
## Disarm the station's potassium supply
`entities hasreagent Potassium do delete $ID`
## Remove all of a specific character's insulated gloves
`entities with Mind named "NAME GOES HERE" rchildren named "insulated gloves" do delete $ID`

# Ghost Roles
## Sentient vendors
`entities with Advertise do makeghostrole $ID "$NAME" "You're a vending machine, use your speaker to annoy people."; rmcomp $ID Advertise`
## Sentient soap
`entities with Slippery prototyped SoapOmega do makeghostrole $ID "$NAME" "You're a bar of soap. Slip absolutely everyone."; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Please don't
`entities with Item do makeghostrole $ID "$NAME" "You're a random, talking item. What the fuck?"; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Your heart would like a word.
`entities with Mechanism do makeghostrole $ID "$NAME" "You are some unfortunate soul's $NAME"`
## Ghostularity
`entities with Singularity do makeghostrole $ID "Singularity" "FUCK"; addcomp $ID MobState; addcomp $ID MovementIgnoreGravity; addcomp $ID PlayerInputMover; addcomp $ID PlayerMobMover`

# Probably make everyone unhappy
## Cursed locker abuse
### Cursed lockers
`entities with EntityStorage named ".*closet$|^.*locker" do rmcomp $ID EntityStorage; addcomp $ID CursedEntityStorage`
### Haunted lockers
`entities with EntityStorage named ".*closet$|^.*locker" do rmcomp $ID EntityStorage; addcomp $ID CursedEntityStorage; makeghostrole $ID "$NAME" "You're a haunted locker. Consume people."; addcomp $ID MobState; addcomp $ID PlayerMobMover; addcomp $ID PlayerInputMover`
## Mess with station access
### All Access Day
`entities with AccessReader do rmcomp $ID AccessReader`
### All access bridge on Saltern
`entities with Airlock named "Bridge" near 6 with Airlock do rmcomp $ID AccessReader`
## Swap around jobs/outfits
### Clown Day
`entities with Mind prototyped MobHuman do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### Clownitis
`entities with Clumsy near 1 with Body prototyped MobHuman not with Clumsy do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### All but two of us are clowns, who is it
`entities with Mind alive prototyped MobHuman not with Clumsy not select 2 do setoutfit $ID ClownGear; addcomp $ID Clumsy`
### Mime Day
`entities with Mind prototyped MobHuman do setoutfit $ID MimeGear; rmcomp $ID Speech`
## Containers
### Remove someone's lungs
`entities with Body prototyped MobHuman named "NAME GOES HERE" rchildren named "lungs" do delete $ID`
or to drop them on the floor:
`entities with Body prototyped MobHuman named "NAME GOES HERE" rchildren named "lungs" do rmmechanism $ID`
## Mess with station structure
### Make the station see-through
`entities named ".*wall" do spawn ReinforcedWindow $ID; spawn Grille $ID; spawn CableApcExtension $ID; delete $ID`
### Electric Avenue
`entities named ".*wall" do spawn spawn Grille $ID; spawn CableApcExtension $ID`

# Make everyone unhappy
## Summon God
`entities with Body prototyped MobHuman alive select 1 do addcomp $ID Singularity; addcomp $ID MovementIgnoreGravity; godmode $ID`
## bang
`entities with MapGrid rchildren do explode $WX $WY 1 1 1 1`
## bang, but funnier
`entities with MapGrid children with Item not anchored do addcomp $ID RoguePointingArrow`