# Feature Design: plant genetics

<table>
  <tr>
   <td>Designer
   </td>
   <td>deltanedas
   </td>
  </tr>
  <tr>
   <td>Discord/Forum Thread
   </td>
      <td>TBD
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

A new CRISPR-like machine for modifying genomes of plants.
Has a hex editor-like UI where you can seek to a position and it shows a certain number of bases.
From there you can make modifications e.g. swapping out an A at index 38 for a T. Once you are happy and think your modifications won't kill the plant, create your new seed and plant it.
Since genome layouts are randomized roundstart this would be no better than current mutagen roulette of just hoping it gets a good trait and doesnt make the plant useless.

To solve gene roulette, the second part of this would be experimentation.
Get 2 identical seeds with clippers then mutate one a little using unstable mutagen.
Either the same machine from the start or a separate one can then analyze them and check what genes (bits) are different.
After a little bit of time it either picks a single random bit, or multiple of them, and tells the player what gene name is at that bit. If the gene has multiple bits it will take some investigation to see which bit it is but that's trivial for yield/potency which can be seen just by clipping it.
Essentially you keep experimenting on plants to figure out the index of every gene, and tada youve mapped the plant genome and can make gmos with ease for the rest of the round.

# Goals:
Promote interdepartment stuff by requiring biomass for gene editing:
- Means there is some cost to minmaxing a plant so you might just have to settle for the important traits
- If there is no med staff / no bodies to juice you can still grow plants as normal
- There was some ideas about being able to reclaim biomass from plants so you could use that to kickstart it.
- Salvage can find biomass on expeditions as a large but irregular source, assuming med doesn't get to it first.

# Gameplay:
The gene editing would primarily be a window like a hex editor, set a position to seek to and then itll show up to X bases.
You can modify a base by just typing A C G or T. they map to 00 01 10 and 11 respectively in binary, so for every 2 bits you get a single base.
From there the player can feed it biomass and print out a fancy new seed with a cost of say 1 biomass per bit modified.

Unstable mutagen would randomly flip bits so you could get an increase of 8 to yield or a decrease of 1 to potency, depends on which bit it flips in an int.

Pollen swabbing, if it still exists, would swap entire gene values rather than operate on a random bit basis.

This might have botanists split up between growing plants for chef and focusing on mapping the genome to get gamer seeds which is cool.

Additionally, instead of the current mutation of a viable bool, a system would be in place where there are bits that set unreasonable pressure temperature or light requirements to grow.
If a plant suddenly requires being grown in space or a fire you are unlikely to try, but it's still possible if you are extremely determined.

# Components:
Plant entities would both have GenomeComponent and its own component for handling swabbing/crossbreeding along with copying genes from parent when clipping.

Since only bools and ints can be stored in genomes, chemicals would still need to be in solution container component and mutated manually similar to how its done currently with SeedData chemicals.

# Inspirations:

- life

# Requirements:

Depends on a rework of botany to have plants be ECS.
