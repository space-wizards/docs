# Botany Rework [EmoGarbage404, Unapproved]

Plant entities, location-based cross pollination, new mutations, and the murder of SeedData.

<table>
  <tr>
   <td>Designer(s)
   </td>
   <td> EmoGarbage404
   </td>
  </tr>
  <tr>
   <td>Discord/Forum Thread
   </td>
   <td> https://discord.com/channels/310555209753690112/1115812839773446204
   </td>
  </tr>
  <tr>
   <td>Github PR/Draft
   </td>
   <td>TBD
   </td>
  </tr>
</table>


# Overview:
Plants mutations will no longer be random value swaps done via swabs. In the new system, adjacent plants will have the ability to cross-pollinate and balance out their instability, potency, and yield. High enough instability values will also enable plants to share mutations. The mutations a plant can share are based on the plant itself. Not all plants can share every mutation and the one you get from a plant out of it's pool of available ones is random.

# Goals:
- Encourage high-level botanist gameplay to make use of many varieties of plants
- Add more systems of plant mutation interaction than simple pouring chemicals and swabbing.
- Reduce the complexity of adding new traits so they can be more easily added in the future.
- Cull most information from SeedData
- Make plants and mutations entities to allow shared component-based code
- Move logic from plant holders to the plants themselves
- Make plant metabolism effects shared with regular chemical effects.

# Player Experience/Gameplay:
Botanists will have to balance how their plants are laid out as well as which ones are grown in order to create unstable plants able to mutate, while keeping them surrounded by plants with beneficial mutations. This will add a medium-difficulty depth to botany which will revolve around the orientation and positioning of different types of plants, as opposed to the high depth system currently in place in which deep knowledge of how traits are randomly accumulated is the only requirement.

# Components:
The biggest change will be plant entities: instead of being `SeedData` classes stored in a `PlantHolderComponent`, plants will just be entities stored in a container. Because of this, most of the logic of plants can just be atomized into components rather than just kept in `SeedData`. This means things like plant pressure thresholds can just be in `BarotraumaComponent` and things like plant chem effects can just be normal chem metabolism.

Most of this will be done through embedding various events in the logic of plants so that components can hook into these and modify values when necessary. This also means that, since the majority of plants shared somewhat similar values, there can be a set of shared plant parents that reduce the need to repeat yaml values.

Mutations will also hook into the beforementioned new events. These will be entities stored on the plant itself. Instead of simply modifying logic with boolean flags, they will instead simply be relayed botany-related events, allowing them to more cleanly modify the values. 

# Inspirations:
The cross-pollination is pretty directly based on /tg/. Plants having inherent traits is also based off of /tg/, however they also have additional stat mutations that I don't want to use. 
