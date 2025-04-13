# Body

I am the BodySystem, Container of Containers! Look upon my works, ye spessmen, and despair.

# Design

Body is the stucture which defines and controls the behaviour of many kinds of mobs. Each Body contains a set of entities inside itself - its body parts and organs, and these control what the Body actually does in-game.

## Body Composition

Bodies are built at runtime out of BodyPrototypes. These are specifications for how a given Body is structured. For example, a human has a BodyPrototype that defines that it has a human torso, a head, arms, legs, all the organs inside itself, and so on.

When a Body is spawned, the BodyPrototype is consulted. As such, when defining monsters and new species, a BodyPrototype ends up being defined somewhere.

Bodies do not by themselves make a creature alive. A BodyPrototype will still be used to spawn random dead corpses.

## Body Decomposition

See "Damage, Stunning, Rotting and Gibbing"

# Engineering

This section covers an overview of important bits of the current Body implementation

## Components

### BodyComponent

BodyComponent contains the data that's specifically scoped to a particular Body. It flags that an entity is a Body, and is used across the codebase to hunt down Bodies and find BodyParts and Organs that live inside then.

The Body contains a ProtoID of the BodyPrototype for this Body. The prototype is used to assemble the Body, and is set in YAML.

A Body has a ContainerSlot called RootContainer. This slot is for the Body's torso, the only required BodyPart a Body has.  

Otherwise the BodyComponent contains information about the number of legs a Body has and a HashSet of the legs of the Body. These two properties are here to control what happens when a Body loses an important number of legs.

### OrganComponent

OrganComponents denote that an entity is an Organ. Otherwise they just contain a reference to the body they're part of, if they currently are part of one at all (as organs can be just on the ground - such as when someone gets gibbed).

### BodyPartComponent

Despite BodyPart being far simpler than Organ in terms of gameplay impact, it actually is more complex at the component level. A BodyPart knows what body it's part of (if any), what type of BodyPart it is, if it's symmetrical, what children BodyPartSlots - not BodyParts - it is connected to, what children OrganPartSlots - not Organs - it is connected to, and if the BodyPart is considered vital.

#### Slots

A BodyPart's BodyPart and Organ Slots share an ID, the name of the slot. BodyPartSlots also have a BodyPartType - in theory, the type of BodyPart that can actually go into that slot.

#### Symmetry

This is an enum with three values - none, left and right. This has limited interactions; the most important is in HumanoidVisualLayersExtension, which itself is then actually referred to by BodySystem when attempting to visualize what an added BodyPart will look like on a humanoid's sprite.

#### Type

This is an enum of types of BodyPart - things like "Torso", "Arm" and "Leg". Outside of composing Bodies, this doesn't tend to have a lot of uses, although it matters a great deal when suiciding using a microwave, which will rip every head off of the Body and cook it inside the microwave.

### BrainComponent

A server-side organ component that just tags that an organ is a brain. This is used to allow a brain to be associated with a player's ghost, which is handy when the brain is pulled out of a mob's head and put in a borg. The brain itself does not track this association.

## Prototypes

### BodyPrototype

A BodyPrototype is the template for a Body when it spawns in the game. The Prototype models a Body pretty closely; it has a Root slot and a dictionary of BodyPrototypeSlots. These themselves reference the IDs of BodyPart entities and Organ entities that they hold.

## Systems

### SharedBodySystem

This is the shared code for Bodies. This covers constructing and destroying Bodies, involving orchestrating the Containers the Body uses, using the BodyPrototype of the Body to build the Body on spawn, and making sure the Body is correctly gibbed when hit by a shuttle.

As a partial class, it is split into several files.

#### SharedBodySystem.Body

This covers creating and destroying - via gibbing - Bodies. When instanitating an entity with a Body, the system will use the Body's referenced prototype and walk through its dictionary of BodyPrototypeSlots. This dictionary and its contents function as a node graph, and the BodyParts and Organs that the tree walk finds are instantiated and placed into the Body. Placing each BodyPart involves creating a nested tree of Containers; these Containers are directly edited to add or remove BodyParts or Organs.

Gibbing is handled somewhat similarly, by walking the tree of BodyParts inside the Body and spawning items for each Organ. This uses the GibbingSystem to do the actual gibbing work.

One final thing the Body does in this file is allow anything with a Body to drag other entities around.

#### SharedBodySystem.Parts

This partial class manages the adding and removing of BodyParts from a Body. When adding or removing BodyParts, the actual work of doing so is to directly done via manipulating the Containers that the BodyPart has been added or removed to; SharedBodySystem just listens for container events and translates them into Body behaviour.

Of note, inserting a BodyPart always requires a BodyPartSlot to exist on the BodyPart to be inserted into that matches the ID of the slot and the type of the BodyPart. For example, a BodyPart might have a slot for a Tail BodyPartType called "tail".

The other role of this partial class is to provide an API for getting BodyParts and Organs from Bodies without needing to dive through Containers.

#### SharedBodySystem.Organs

This file is concerned with adding and removing Organs from Bodies. Of note, inserting an Organ always requires an OrganSlot to exist for that Organ; the OrganSlot being defined as an ID string. For example, this means that a BodyPart needs to have a "heart" slot for an Organ to be inserted into its "heart" slot. 

#### ServerBodySystem

The server implementation of SharedBodySystem overrides a small amount of its shared parent's behaviour. It's this system that allows a ghost to eject themselves from a dead body on a movement input, and properly handles instantiating gibbed organs (preventing spawning them for a mob that is actually in the process of being deleted, for example).

### BrainSystem

The BrainComponent is a simple component that flags that an Organ is a brain. Likewise, its behaviour in its server-side system is simple - when the brain is added or removed from a Body, it handles moving the associated mind of the brain (which will always have a MindContainer, as this code demands) from the old entity to the new one. An obvious place this is used is when a person is gibbed - their mind is tranferred from the gibbed body to the brain - and then when that brain is put into a borg - the mind is first translated into a MMI and then the borg entity.

Entertainingly, anything with a BrainComponent is not allowed to point at anything.

## YAML

Body YAML is held in the Resources/Prototypes/Body folder. In the Prototypes folder is BodyPrototypes for many humanoid species, both roundstart and gimmick. It also covers, in the Animal and Specific subfolders, some BodyPrototypes for animals like mice, mothroaches and cows.

An example of a human's BodyPrototype is:

```yaml
- type: body
  id: Human
  name: "human"
  root: torso
  slots:
    head:
      part: HeadHuman
      connections:
      - torso
      organs:
        brain: OrganHumanBrain
        eyes: OrganHumanEyes
    torso:
      part: TorsoHuman
      connections:
      - right_arm
      - left_arm
      - right_leg
      - left_leg
      organs:
        heart: OrganHumanHeart
        lungs: OrganHumanLungs
        stomach: OrganHumanStomach
        liver: OrganHumanLiver
        kidneys: OrganHumanKidneys
    right_arm:
      part: RightArmHuman
      connections:
      - right_hand
    left_arm:
      part: LeftArmHuman
      connections:
      - left_hand
    right_hand:
      part: RightHandHuman
    left_hand:
      part: LeftHandHuman
    right_leg:
      part: RightLegHuman
      connections:
      - right_foot
    left_leg:
      part: LeftLegHuman
      connections:
      - left_foot
    right_foot:
      part: RightFootHuman
    left_foot:
      part: LeftFootHuman
```

Whereas the ultra-simple mothroach's prototype is:

```yaml
- type: body
  id: Mothroach
  name: "mothroach"
  root: torso
  slots:
    torso:
      part: TorsoAnimal
      organs:
        lungs: OrganAnimalLungs
        stomach: OrganMothStomach
        liver: OrganAnimalLiver
        heart: OrganAnimalHeart
        kidneys: OrganAnimalKidneys
```

The Parts folder contains body parts for various species. For example, a human head is defined as such:

```yaml
- type: entity
  id: HeadHuman
  name: "human head"
  parent: [PartHuman, BaseHead]
  components:
  - type: Sprite
    sprite: Mobs/Species/Human/parts.rsi
    state: "head_m"
  - type: Extractable
    juiceSolution:
      reagents:
      - ReagentId: Fat
        Quantity: 5
      - ReagentId: Blood
        Quantity: 10
```

BodyParts inherit from multiple parents; in this case, PartHuman, which itself inherits from BaseItem and BasePart, and BaseHead, which inherits from BasePart, but these inheritance trees do not impart much gameplay differences, and BodyParts are rarely, if ever, seen outside the host Body.

In the Organs folder are the many organs that make up spessmen species. For example, humans lungs are defined as follows:

```yaml
- type: entity
  id: OrganHumanLungs
  parent: BaseHumanOrgan
  name: lungs
  description: "Filters oxygen from an atmosphere, which is then sent into the bloodstream to be used as an electron carrier."
  components:
  - type: Sprite
    layers:
      - state: lung-l
      - state: lung-r
  - type: Item
    size: Small
    heldPrefix: lungs
  - type: Lung
  - type: Metabolizer
    removeEmpty: true
    solutionOnBody: false
    solution: "Lung"
    metabolizerTypes: [ Human ]
    groups:
    - id: Gas
      rateModifier: 100.0
  - type: SolutionContainerManager
    solutions:
      organ:
        reagents:
        - ReagentId: Nutriment
          Quantity: 10
      Lung:
        maxVol: 100.0
        canReact: false
      food:
        maxVol: 5
        reagents:
        - ReagentId: UncookedAnimalProteins
          Quantity: 5
```

Because Organs are "do-er" entities, they have lots more components on them than other Body entities.

Of note here, the lungs have two important components that make them work as lungs - LungComponent and a MetabolizerComponent. The Metabolizer is there to metabolize Human-typed chemicals into the Body from the "Lung" SolutionsContainer, but the LungComponent is actually doing the work of being lungs.

Another example is the human stomach:

```yaml
- type: entity
  id: OrganHumanStomach
  parent: BaseHumanOrgan
  name: stomach
  description: "Gross. This is hard to stomach."
  components:
  - type: Sprite
    state: stomach
  - type: Item
    size: Small
    heldPrefix: stomach
  - type: SolutionContainerManager
    solutions:
      stomach:
        maxVol: 50
      food:
        maxVol: 5
        reagents:
        - ReagentId: UncookedAnimalProteins
          Quantity: 5
  - type: Stomach
  - type: Metabolizer
    maxReagents: 3
    metabolizerTypes: [Human]
    groups:
    - id: Food
    - id: Drink
```

This has a StomachComponent - which does the work of being a stomach - and a Metabolizer that metabolizes human-typed food and drink chemicals. 

Other human organs metabolize other chemicals - the liver metabolizes alcohol, the heart metabolizes medicine, poison and narcotics, and so on.

Note that there's often not a string specifying where the effects of the metabolizer are coming from. By default, metabolizers pull from the default name of the chemstream of the mob's BloodstreamComponent - "chemicals". The stomach will put things into the chemstream.

Metabolism is handled via marking a chemical as part of a metabolism group. An example groups is Poison:

```yaml
- type: metabolismGroup
  id: Poison
  name: metabolism-group-poison
```

and likewise an example type of metaboliser is Human:

```yaml
- type: metabolizerType
  id: Human
  name: metabolizer-type-human
```

These together determine how metabolism works for a particular chemical on a particular organ.

An example metabolism group is then Robust Harvest, which is marked as having the following metabolisms:

```yaml
  metabolisms:
    Poison:
      effects:
      - !type:HealthChange
        damage:
          types:
            Poison: -2
            Blunt: -3
            Slash: -3
            Piercing: -3
        conditions:
        - !type:OrganType
          type: Plant
      - !type:HealthChange
        conditions:
        - !type:OrganType
          type: Plant
        - !type:ReagentThreshold
          min: 30
        damage:
          types:
            Asphyxiation: 1
            Heat: 2
            Poison: 1
    Medicine:
      effects:
      - !type:Polymorph
        prototype: TreeMorph
        conditions:
          - !type:OrganType
            type: Plant
          - !type:ReagentThreshold
            min: 80
```

This chemical is both a poison and a medicine. But because it only affects plant organs, a human could chug a jug of it and it'd do nothing.