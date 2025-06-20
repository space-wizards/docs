# The Invisible War: Virology & Disease Rework [Goodwheatley, Unapproved]

Virology is a weird job. 

In a game about social interaction, their job is to work with diseases; something famous for not being great with crowds. The fact that both /tg/ and goon both missed the mark entirely with their Virologist content has led many to believe that Virology fundamentally can't work in SS14. But there's much more depth you can have with viruses than just adding chems until you get the good symptoms, and I hope to achieve that. Could disease content work without a dedicated Virologist job? Possibly, but I believe that just like how Atmospheric Technicians enhance atmos content, Virologists can improve the disease experience for everyone.

---

## The Problems

Before I outline my ideas, I like to include a segment explaining what issues I have with the previous system, so it's clear what I think needs to be fixed. ~~and I'm going to keep doing it until I'm banned from hackmd~~

To start, let's go through the basic flow of a legacy disease outbreak. The event rolls, announcement plays, and a few seconds later people start feeling sick and vomiting. Suddenly people swarm to med to gulp down spaceacillin, and the outbreak is cured at the cost of a few players who forgot about the cellular damage. A few players may decide to struggle through and hope the disease cures itself, so they just take the slowdown like a champ until the round ends.

This sucks.

### What's Wrong With That Hypothetical

**1. Chemistry is responsible for curing the outbreak**

:::info
Every single map has a section of medical for virology, with those machines and quarantine rooms that nobody ever uses. Why? Because they a) serve no purpose because people will memorize the specific cures for a specific disease and b) the specific cure doesn't even matter anyway because spaceacillin exists. Making it deal genetic damage was like slapping a Band-Aid on a gaping flesh wound; it just makes diseases more annoying to deal with without actually solving any of the fundamental problems of diseases. Instead of just punishing players who stuff spaceacillin down their throats, why not also stop and consider why they're doing that in the first place?
:::

**2. Spaceacillin exists**

:::info
A cure-all for almost every disease is a dumb idea, and yet spaceacillin's existence somehow is never questioned. It completely removes any nuance of treatment and makes chemistry the best treatment method for yet another piece of medical content.
:::

**3. Diseases are extremely simple**

:::info
The only disease that had stages was the monkey virus, and I don't think it even worked properly. The effects of diseases never changed, it never got worse, and for 90% of diseases it also never got better because they didn't cure automatically. 
:::

**4. You can just ignore diseases altogether**

:::info
The worst thing most diseases could do was be annoying, and once spaceacillin did genetic damage players decided they could live with annoying. What's the point of diseases if nobody's going to try and get cured because it doesn't actually pose any threat to their lives?
:::

**5. Disease spread is wacky**

:::info
Contamination doesn't exist, disease protection stats protect against all infection methods no matter what, and it doesn't even make sense half the time. If I'm wearing a bio suit, why should there be a chance I can get infected from close contact with infected patients? If I'm wearing internals, why can I be infected when someone coughs?
:::

**6. Nobody ever uses the virology room**

:::info
The quarantine rooms are irrelevant because bringing a patient into medical makes no sense when you can just feed them spaceacillin from the chem desk, and the machines are never used because a) everyone's memorized what symptoms are caused by which diseases and b) making vaccines is aggravatingly slow for the incredibly middling payoff of being able to inoculate someone who isn't infected.
:::

**7. The announcement**

:::info
If you're just going to instantly tell the entire station that there's a disease outbreak, then everyone knows they have to head to medical if they cough and the outbreak is cured. Diseases should be stealthy in the first few minutes they exist-this gives it time to spread, and doesn't make solving the outbreak as clear-cut.
:::

These issues can be summed up in three words: **Diseases aren't impactful.** I aim for this design doc to outline a plan to fix that.

---

## Outbreak

To begin, each virus has a unique variation of attributes (Immune Resistance, Stage Speed, Transmission, Stealth, Severity), and symptoms when they come into existence. They also have a unique genetic code, which handles how the virus will mutate and evolve as it spreads. More dangerous viruses will have more complicated genetic codes. As the virus infects new hosts, each new virus that's infected a host can randomly mutate changes to its genetic code, creating new traits. If this mutation is beneficial and spreads to new hosts, it now becomes a new strain of the initial virus. 

New strains are what you want to avoid in an outbreak; existing cures aren't as effective against them since their genetic code has been altered, and cures work based off of genetic codes. To make things even more difficult, cures based off virus strains are less effective than cures made with the virus itself. The more a virus mutates, the harder it becomes to stop. This forces medbay to react when there's an outbreak and encourages the Virologist to track down the initial infected; leading to hopefully a fun segment of detective gameplay as you track the spread back to its source.

On the other hand, viruses will grow more dangerous the longer they infect you. If a virus is in your body for a significant amount of time, its symptoms can be upgraded into more dangerous versions of themselves as the virus progresses through stages of infection. The evolved version of the symptom is related to what the original did; Coughing can evolve into Vomiting, but not Heart Attack. When a virus evolves is based on its Stage Speed and what the symptoms evolve into is based on its genetic code. This mechanic makes viruses actually deadly, forcing players to seek treatment and putting pressure on medbay to cure them before it's too late.

The two avenues of virus evolution makes outbreaks dynamic, and forces Virologists to weigh their options in an emergency. Do they spend time tracking down Patient 0 and try and cut the virus off at its head, or do they do damage control and try and treat patients so the virus can't mutate and evolve?

:::success
This outlined model for virus evolution fixes Issues 3 (diseases are now more complex) and 4 (diseases can be lethal), and partially fixes 1 (the analyzer machine is now useful for seeing details on what the symptoms are) and 6 (There's a good reason to quarantine so the virus can't spread).
:::

---

## Transmission 

So, now that how the virus works has been established, how does it spread? Unlike the other mechanics described in this document, which are of my own design, this part takes direct insipration from disease mechanics in another game; Oxygen Not Included.

Viruses are transmitted through **Germs**. Germs can cover items, mix with liquids, or float with gases; the method the germs are most effective at transmitting with varies between viruses. 

Germs also have pressure and temperature tolerances, and interact with different materials-for example, high temperatures can kill germs, and space cleaner can kill them if their Immune Resistance is low enough. 

Germs naturally die out when the conditions are not favorable. The conditions differ for each germ depending on how the virus has evolved, but radiation is generally very effective at killing germs.

Each phase of matter has a different upper limit on germs per entity (tile, item etc.). This limit is multiplied by the entity's mass. Once that limit is reached, the germs become "Overpopulated" and start dying out at a speed dependent on degree of overpopulation.

Fluids (gases and liquids) constantly exchange germs with fluids of the same phase nearby. Gases and liquids do not exchange germs with each other directly. Solid tiles do not exchange germs, but a solid tile on which germs multiply will infect direct neighbors.

Players will exchange germs with objects and items by interacting with them. Germs on someone's skin are not dangerous yet, unless the virus has evolved to transmit through touch. They may be removed from the player by usage of a sink (hands only) or shower (all exposed skin if liquid, entire body if gas and hardsuit isn't equipped). This will transfer the germs mostly into the liquid used by the object and partly onto the object itself.

Germs can reside on a player or in the player. Germs on a player do not cause any direct harm. Only germs in a player can cause viral infections. There are four ways for a player to become infected: Ingestion, Inhalation, Contact, Transfusion.

Ingestion is triggered when the player eats or drinks something that has germs on it. Inhalation is triggered when the player breathes in gas with germs in it. Contact triggers when infected material makes contact with exposed skin, and Transfusion triggers when infected blood is introduced into a player's bloodstream. 

Inhalation, and Contact can each be blocked by wearing proper PPE, but Ingestion and Transfusion have no PPE that protects against them. Infection through Ingestion can possibly be fought off with a strong immune system, but Transfusion is unavoidable.

If they fail to fight off the virus, the player suffers from its symptoms until they recover after some time (if the virus has a sufficiently low danger or the player has a strong immune response), die, or be cured of the virus by taking the appropriate care and medicine. If they succeed in fighting off the infection, they become immune to that virus and any similar strains, and their blood begins producing antibodies.

Janitors play an important part in outbreaks due to germs, as safely disposing of infected dead bodies and cleaning surfaces not only prevents immediate infection but will breed the virus to become more mild in future generations, as viruses that evolve to become lethal will be unable to spread further. A dead body can't infect more people if it's properly handled.

### Immune Response

Being infected with a virus doesn't mean you're instantly doomed. For a few minutes, your immune system will begin reacting to the virus, and who wins determines if you start having symptoms or not, and if the virus is able to continue to spread. Immune strength depends on several factors, including the virus' Immune Resistance, whether or not you've had previous viruses, how much medicine you've taken, and if you've been cloned or not. If your immune system succeeds, you fight off the virus and become immune. If it ends in a draw, you become a asymptomatic carrier-you have the virus in your bloodstream, but it doesn't harm you.

:::success
This outlined model for transmission fixes Issue 5 (Proper PPE actually makes a difference in preventing infection, and disease spread not only makes sense but has much more depth than the previous system) and 7 (no announcement when an outbreak begins, only when it becomes widespread)
:::

---

## First, Do No Harm

Home stretch, this section talks about the Virologist and what they do to cure viruses. There are 2 methods for curing viruses: producing cures and administering antibiotics.

### Cure Production

Back in the Outbreak section I mentioned cures work based off of genetic codes, and this goes more into depth about how cures are made and how they work. Cures are a reverse-engineered version of the virus designed to neutralize it and make players immune to the virus. Giving it to an infected person will slowly kill the virus if it's effective enough, giving it to a non-infected person massively increases the chance that their immune system will fight off the virus if they're infected. Cures are produced through the Pandemic machine by either taking a sample of the virus and analyzing it, or taking a sample of the antibodies produced by an immune player. Once you do that, you can infinitely produce cures based on the analyzed sample. The cure is more effective if you take blood from an inital infected or an immune. This encourages Virologists to go and hunt down those players, so the outbreak can be cured faster.

### Antibiotics

If everything's already gone to hell and everyone's infected, there's an alternative to hunting down the virus and producing cures. Instead of spaceacillin, which would be removed/reworked, special antibiotic chems can affect the stat values of the virus, and if you administer the right combination of antibiotics, you can kill it entirely. This is risky though, as not only does the right combination depend on the virus' genetic code, giving too much of an antibiotic can not only make the virus *stronger*, but also completely immune to certain medicines. Antibiotics can also have significant side effects on a player, so it's very likely you do more harm than good.

### Virologist Equipment

Besides the biosuits and other standard equipment found in every virology room, Virologists also get a special virus analyzer that gives more detailed, but still vague, information on a virus someone is infected with. Health analyzers simply say if the target is infected or not, while the Delta Diagnoser gives complete information on the virus. Virologists also have a box of Virus Stickers (put it on someone and when they're infected with something the sticker will glow red, and using a Virus Analyzer on it gives detailed information on the virus. This doesn't work retroactively, and the sticker can fall off when changing clothes.), and a Penlite Holoprojector that can set up barriers that block people who have a virus from walking through them. If a virus has a high enough Stealth value, the barrier can miss it and allow the person through regardless. Finally, they can get a Vaccine Gun from the medical techfab once Science researches it, which accepts cures as ammunition and lets them be fired and injected from a distance.

:::success
The outlined method for curing viruses fixes Issues 1 (the cure production machine is useful now), 2 (spaceacillin is gone), and 6 (vaccines are more useful, somebody works in virology)
:::

---

Draft Notes:

- Virologist focuses more on curing and researching viruses rather than making them
- During an outbreak, tracking down Patient 0 allows you to get a bonus from CentCom and mass-produce cures
- If you can't track down Patient 0, accurately reporting symptoms and mutations in the virus builds the amount of information on it, once you have enough info you can start producing cures.
- As the virus mutates by spreading from person to person or simply existing long enough, these cures will become less effective, requiring you to stay on top of the virus's spread and accurately report new mutations to ensure that new cures stay effective.
- Certain special chemicals can affect the health of the virus, and specific combos can kill it altogether. These chems will have significant side effects, and prolonged use can possibly make the virus immune to the chem altogether.
- Asymptomatic carriers, virus mutates as it spreads
- Players can fight off the virus and become immune through random chance, analyzing an immune person's blood helps to improve the cure's effectiveness + protects against viruses with similar effects
- Simulated immune system, having prolonged symptoms weakens your immune response and makes future viruses more dangerous without proper treatment
- Code Vermillion (new alert level that orders the station crew to quarantine. Violet Alert but more important/urgent)

Discussion Notes:
