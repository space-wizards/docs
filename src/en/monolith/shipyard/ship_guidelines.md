Ship Guidelines
===============

**Preface: Recommendations**

Do not start your mapping journey with a large vessel/important POI! It will only waste you and maintainer’s time, embark on large projects at your own risk - Make sure you have a solid understanding of mapping requirements and methods! 
It is not maintainer responsibility to fix your PR!

Before beginning to actually map a ship, make sure you already have an understanding of what you wish to make, and whether it is something that players want or will use. 
If there are five different cargo ships, don’t make another cargo ship, unless you’re trying to replace an existing one! (Look in the Ship Roster section for pre-existing ships!)

**Fundamental Requirements**
*Communications/Control*

* Holopad (one with ship prefix, rogue ships use the ship antag prefix)
* Fax machine (same prefix usage as above)
* Station Records computer
* Shuttle console
* Engineering/Atmos
* Functioning Atmospherics (Linked Air Alarms/Firelocks/Vents/Sensors, waste management)
    - Make sure source atmos cans are “Oxygen” and “Nitrogen” connected to a mixer (21% oxygen, 79% nitrogen), and are accessible for portable tank refilling
    - Also make sure pipe networks are colored! (View atmos network example for commands)
* Functional Power generation/networking
    - Do not place wires underneath walls! (Save for necessary times such as APCs)
* Fire Extinguisher cabinet (Filled)
* Internals cabinet/Suit storage (Filled)
* Defibrillator cabinet (Filled)
* Directional fans under external airlocks
* Airlock intermediate space (Airlock doors should bolt each other when the opposite door is open!)
* Exterior walls should be “reinforced” (plasteel) walls
* Exterior doors should either be docks or “external” airlocks
* SMES (advanced is fine)
* Fueled generator (Solars are also fine. No singularity/tesla!)
    -  AMEs and other power sources should be used as weakpoints, do note their volatility!
* At least one substation, consider multiple for large ships
* APCs for each room (multiple for powering shields if applicable)
* Mini gravity generator
* Gyroscope(s)
* Wall fuel locker/rack with fuel for your power source of choice
* Thrusters in all four directions (Large thrusters should be used only for primary thrust, not as maneuvering thrusters -> small thrusters are still relevant for capital ships!)

*Meta*
* Warp Point (for ghost spectator reasons)
* Latejoin spawn point - Keep in a crew/habitable area!
* RoofComponent on your grid (done via F7 objects menu, same way you add BecomesStation. Add the roof enabled/disabled markers to all tiles you want to not be affected by planet lighting (such as desert planet).)
* BecomesStation component
* Vacuum fix markers on all tiles that will be spaced! This includes diagonals.

**Economy Functionality Requirements**

*Medical:*
* Medical bed
* Stasis bed
* Recharger (for defibrillator)
* Filled medicine cabinet
* Surgery supplies (medium and above)
* Freezer (walk in or container, medium and above)
* Crew monitoring console
* Crew monitoring server (medium and above)
* Medical techfab
* Bank ATM (Withdraw, normal kind for large enough vessels)

*Chemistry:*
* Sink (one with water)
* Drain
* Filled chemistry locker
* Hotplate
* Electrolysis machine
* Centrifuge
* Reagent grinder
* Chemical dispenser (filled)
* Chemmaster

*Salvage:*
* Ore processor (for a faction mining ship, this can be industrial)
* Cargo/EVA bay to space (blast doors or external airlock)
* Filled salvage specialist locker
* Salvage suit storage (salv hardsuit, salv EVA, mining hardsuit)
* Ore box/Construction box (optional)
* Salvage techfab (optional)

*Cargo:*
* Large empty cargo bay(s) with easy access to docks (Optional: With conveyor belts)
* 5 wide dock with flaps (See standard cargo dock, look at other cargo ships/trade docks)
* Autolathe (optional)

*Xenoarch (arti science)*
* Analysis console
* Analysis pad
* Dedicated artifact chamber, with a directional fan dividing it from main atmos - should have a blast door to space toggleable from outside
* R&D server (Ideally far from arti chamber)
* R&D console
* RD suit storage
* RD locker
* Autolathe
* Protolathe
* Circuit imprinter
* Arti chamber is permitted to use plastitanium walls/windows, even if it is a civilian vessel

*Advanced medical:*
* Biofabricator
* Cloning pod
* Medical scanner
* Cloning computer
* Biomass recycler, in a morgue
* Morgue with a drain
* Cryopod setup (Guidebook layout works, make sure whatever you use works!)

*Kitchen:*
* Electric range
* Freezer (any kind)
* Reagent grinder
* Electric grill
* Deep fryer
* Microwave
* Food-o-mat
* Drain
* Chef closet
* Chefvend
* Plasteel Chef vender
* If you have a walk in freezer, put a meat spike in it (and a freezer container)

**Combat Requirements**
*All Vessels*
* Gunnery server depending on armament
* Gunnery console, same orientation as Shuttle Console
* Weapons relevant to shuttle archetype
    -  Be judicial with use of heavy weapons (e.g Torpedoes, Charon, Cyrexa, etc) - Don’t map on light or civilian vessels!
    -  All shuttles should have some kind of armament. For civ ships, a couple L85s is fine.
* Do Not Over-supply ships - keep personnel armament to a minimum, and at most provide basic equipment - players can kit out their ships themselves! (An example is a beanbag kammerer, or a MK-58.)
*Factions/PMC*
* Dedicated combat ships are more lenient in terms of weapon limitations. However, make sure they fulfill a specific niche in combat. Combat ships should also have some kind of “economy” purpose for downtime - cargo bays, small R&D, chemistry, anything so long as it does not outvalue a vessel dedicated to such economy.

**General Guidelines**
*Appearance*
* Ships should look good, both on the outside and in the inside
    -  This can be achieved with decals, good hull profiling, greeble, among other things. 
    -  If you make a ship (especially as a replacement for an existing vessel), it must look better and fit the setting. (Put effort in with making decals! Good decals define a stellar vessel and make a bad one good!)
* Vessels should follow design standards for whatever faction they belong to!
    -  For the TSF: Ships should be strong, well armed, and embrace the miltech vibe of the Federation. Inside, they should feel like they were made by a modern military - but like a military, feel built to function, not form, leading to cramped and mechanical insides. More public/important areas can be made prettier (e.g bridge, dorms, etc)
    -  For the PDV: Ships should be moderately armed, and should embrace the vibe of “ancient design made more modern.” After all, the Dynasty has many ancient blueprints. To this end, vessels should feel practical but old - cramped miltech like the TSF, but with more rust/debris/decay and inconvenient layouts.
    -  Mercenary vessels are not as limited in style, but whatever theme you choose for your vessel, it should remain consistent across the hull and be coherent - it should still look good!
* Remember to put tiling underneath your doors, and keep all floors under walls as plating (not lattice)!

*Identification, Cost, and other Yaml changes*
* Ship naming nomenclature: (Author) (Name) (Type)-{1}
    -  Author: Only usually seen on shipyard consoles, it has its own field in yaml. Put in whatever combination of three or four letters in, keep this consistent across ships you make! It is used to identify who made what ships (e.g Onezero0 uses SHM, John mcMapper uses JCM, etc. Don’t use the same ID as someone else!)
    -  Name: Up to contributor discretion. Make it fitting, unique, and appropriate.
    -  Type: CIV (Civilian/medical vessels), MIL (well-armed specific combat ships accessible to mercs), TSF (TSF-exclusive vessels), EXP (Expeditionary vessels, general Merc ships), PDV (Dynasty-exclusive vessels) 
	-  {1} is the space where an identification code for a ship is put in the name, keep this at the end
* Cost: Use the appraisegrid command for base price, and mark up depending on effectiveness/tech/robustness of the vessel (usually ~20% at minimum, more for combat vessels)

*Functionality*
* FTL drives are recommended for most ships, though be judicial in your use of more advanced variants (such as CTLA-25s, CTLA-50, etc)
* Shields are in an interesting place - keep their effects in mind, and if you have one, make sure it has enough power! Power supply = shield durability, and they are mostly limited by APC capacity. Be careful.


**Examples** (TBD)
Frontier Image credits:
arimah (discord)
alkheemist (discord)


Figure 1: Decaled/Un-decaled room (Note the usage of catwalks!)


Figure 2: Frontier Engineering power network example


Figure 3: Frontier Atmos network example


Figure 4: Do not place diagonals together like this! Players can see right through them, and they are generally quite janky.


Figure 5: Blast doors over diagonals work, but are really ugly. Do not do this! (Also make sure blast doors are perpendicular to the direction of the window.)


Figure 6: More lack of decals + Example of bad FTL/full-tile component placement, keep it sandwiched between other tiles instead (e.g walls, directional windows
