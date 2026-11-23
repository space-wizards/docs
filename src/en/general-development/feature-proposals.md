# Feature Proposals

If you are considering adding or reworking some major component of the game it's recommended that you submit a proposal before you actually start coding whatever it is you want to do. Pinning down exactly how your feature should work to mesh well with the rest of the game will save you a lot of headaches rewriting your PR for the ~~1st2nd4th~~ 7th time before it gets merged. It also gives you a pathway to playtesting your changes in an early stage, giving you a better understanding of how your feature will work in the game.

## How do I make a proposal?

1. Make a copy of the design proposal template located at `src/en/templates/proposal.md`.
   
3. Read through [SS14's Core Design Documentation](../space-station-14/core-design.md) (for gameplay-related proposals).

4. Write your proposal (see [guide to editing docs](../meta/guide-to-editing-docs.md)).

5. When you are ready for your proposal to be reviewed, make a pull request.

6. Your proposal is approved when a maintainer gives it the proposal approval label. This is a green light for you and your collaborators to work with the approving maintainer to implement it as a playtest (described below).

7. If the playtest goes well, the maintainer will give feedback on any changes you need to make. At this point, you update your proposal with implementation details to help give an understanding of how the feature will be added. If the maintainer gives the implementation approval label, you're off to making proper PRs!

8. As you get your feature's code merged into the game, you update your document based on any design changes that happen during implementation. 

10. Once the feature is fully implemented, the maintainer gives a final approval and merges your design doc into the repository, along with a link in the side bar. Feature complete! *Note to maintainers: edit `src/SUMMARY.md`*

``` admonish tip "Unfinished Proposals"
If you don't think that your proposal is ready for maintainer scrutiny, but still want feedback on it you can PR it as a draft. Drafts are less likely to attract people looking to get down to brass tacks, but still let people comment and give advice.
```

## No, as in what is a design doc?

A design document is a high level summary of whatever you're proposing to add to the game. They basically serve to get nebulous ideas down on paper so it's easier to see how exactly those ideas will mesh with the rest of the project. They generally have a few parts.

When submitting a design, we ask that you start with a proposal document. Ideas always change during development as players test your feature and developers implement it, so in a proposal document we are looking for the following:

1. Why the feature is good to have in the game. This is the most important part! Are you adding something new or fixing an existing problem? Something being "cool" is a good starting point, but you need to show that you've considered how your feature works alongside other features and content. Describe why your feature is something that will benefit the game long-term, how it fits with the game's design pillars, and how it will work with the game overall.
2. A high-level summary of what the feature actually is. What are the players expected to do with your feature, what is its goals for the game and the players, what are the mechanics and aesthetics? You want to cover what the player will be doing, and also what the player should be feeling when interacting with your feature.
3. Who will be implementing the feature. We find that the best features have someone who can help push the actual implementation through. If you yourself don't have the programming skills required, talk about your ideas with the community! Get people excited! Space Station 14 is also a great opportunity to [learn some basic coding](../general-development/setup/howdoicode.md), and you can implement a lot with very simple code. 
4. How your feature should be tested. A key step in the design doc process is to get a quick-and-dirty version of your feature into the hands of players. That's a great way to find out if your feature has any hidden flaws that need to be worked on. Briefly describe how your feature should be playtested, based on the criteria below.

``` admonish warning "Don't"
- Include pseudocode level descriptions of how your feature works. That's for after the proposal has been accepted and you're actually implementing the thing.
- Specify numerical amounts for every item, field, or mechanic. That's for eventual balance bikeshedding; for example it's enough to say that a disease will have one, several, or many symptoms.
- Forget to include how players should interact with your features. SS14 is a multiplayer game and how the players engage with your mechanics is more important than the specific mechanics they engage with.
- Write an entire, actual FSD or SRS. It's not and will never be required as it constitutes egregious overkill for a project of our size and structure.
```

``` admonish tip "Design Principles"
If you want to improve your chances, it's recommended that you read the [SS14 Core Design Documentation](/src/en/space-station-14/core-design.md) document to get a high-level overview before you start writing, as it'll provide context for why things are the way they are.
```

## Does my idea really need a design doc?

It depends on the scale, and pervasiveness of whatever you're thinking of proposing. If it's something like adding a single gun or a couple simple plants it probably won't. On the other hand if you are adding an entire subdepartment ala anomalies/xenoarchaeology, or something on the order of reworking the entirety of botany or chemistry it certainly will.

A good rule of thumb if the new feature or rework you have in mind would require adding or reworking a page of the guidebook or one of the feature docs on this site then it probably needs a design doc. Same if the proposal could be accurately described as 'reworking the entirety of X'.

## What happens after I submit the proposal doc?

A maintainer will have to review your document and determine if it is an idea worth testing. If there is an area specialist, such as a workgroup, the maintainer is expected to reach out to them for expert opinion. Not everything passes this bar! Sometimes an idea is not developed enough, or has overlap with an existing feature. Don't be discouraged if it happens, an idea can be good but simply not be the right fit for this game. 

If the maintainer approves the proposal, they will assign a proposal approval label. You are then free to start working on the playtest implementation of your feature. If necessary, the maintainer can help set up a workgroup space for you on our Discord server so you can bring in any fellow developers and stay up to date with communications. 

## How do I playtest?

We ask that any proposal doc goes through a playtest. This can be done in three different ways:

### Prototype Upload

Space Station 14 has a very efficient way to run the game, which is through [entity prototypes](https://docs.spacestation14.com/en/ss14-by-example/adding-a-simple-bikehorn.html). Every item, NPC, and puddle on the floor is an entity that has a bunch of building blocks (components) that define how they work. These components define things like the entity's sprite, if it can be picked up, if it can be swung like a weapon, what damage it would deal, all in very simple `.yml` files. And because our core developers are really cool, we can upload those files directly to our live servers!

Prototype upload playtesting is best for features that are similar to existing features. This is because you are limited to the components that already exist, so you can't include completely new game code. Luckily we have a lot of components, so for many features it can get you 95% of the way there and be enough to playtest your idea. The benefit is that it's very easy to host a prototype upload playtest, making it by far the fastest option. 

Once you have your prototype files ready, contact the reviewing maintainer to host a playtest. You will work together with an admin to upload the files to one of our game servers. Make sure your proposal includes any instructions
