# Feature Proposals

If you are considering adding or reworking some major component of the game it's recommended that you submit a proposal before you actually start coding whatever it is you want to do. Pinning down exactly how your feature should work to mesh well with the rest of the game will save you a lot of headaches rewriting your PR for the ~~1st2nd4th~~ 7th time before it gets merged.

## How do I make a proposal?

1. Make a copy of the design proposal template located at `src/en/proposals/proposal-template.md`.

2. Write your proposal (see [guide to editing docs](../meta/guide-to-editing-docs.md)).

3. When you are ready for your proposal to be reviewed, make a pull request.

4. Your proposal is approved when a maintainer merges it. This is a green light for you or someone else to go ahead and implement it. A maintainer will then link your proposal to the side bar. *Note to maintainers: edit `src/SUMMARY.md`*

``` admonish tip "Unfinished Proposals"
If you don't think that your proposal is ready for maintainer scrutiny, but still want feedback on it you can PR it as a draft. Drafts are less likely to attract people looking to get down to brass tacks, but still let people comment and give advice.
```

## No, as in what is a design doc?

A design document is a high level summary of whatever you're proposing to add to the game. They basically serve to get nebulous ideas down on paper so it's easier to see how exactly those ideas will mesh with the rest of the project. They generally have a few parts.

1. Why the feature is being proposed, which can be as simple as 'I think it would be cool' to as specific as 'I noticed ABC problems with cargos gameplay loop and want to add XYZ to remedy those problems'.
2. A high level summary of what the feature actually is, how the feature engages with players, and how the feature interacts with other major parts of the game.
3. A more detailed summary of the proposed mechanics for the feature, how players are intended to interact with those mechanics, and how those mechanics involve or are involved with other parts of the game. You don't need to go into every specific case, it's enough to say that there should be chemicals filling specific roles and not detail the exact chemicals you

These don't have to be discrete sections and shouldn't be. When you're detailing the mechanics it's probably a good idea to detail how the players will interact with those mechanics and how the way the players interact with those mechanics benefits the game. If you want to see examples of successful design documents all of the accepted, but unimplemented, design docs can be found in the "Design Proposals" section below. Design documents that actually got implemented eventually transmute into the feature docs in the "Space Station 14" section.

``` admonish warning "Don't"
- Include pseudocode level descriptions of how your feature works. That's for after the proposal has been accepted and you're actually implementing the thing.
- Specify numerical amounts for every item, field, or mechanic. That's for eventual balance bikeshedding; for example it's enough to say that a disease will have one, several, or many symptoms.
- Forget to include how players should interact with your features. SS14 is a multiplayer game and how the players engage with your mechanics is more important than the specific mechanics they engage with.
- Write an entire, actual FSD or SRS. It's not and will never be required as it constitutes egregious overkill for a project of our size and structure.
```

## Does my idea really need a design doc?

It depends on the scale, and pervasiveness of whatever you're thinking of proposing. If it's something like adding a single gun or a couple simple plants it probably won't. On the other hand if you are adding an entire subdepartment ala anomalies/xenoarchaeology, or something on the order of reworking the entirity of botany or chemistry it certainly will.

A good rule of thumb if the new feature or rework you have in mind would require adding or reworking a page of the guidebook or one of the feature docs on this site then it probably needs a design doc. Same if the proposal could be accurately described as 'reworking the entirity of X'.

## Will my design doc get accepted?

No idea! What design proposals do or do not get in is determined by maintainer approval like normal PRs. If you can get at least one maint to decide that it sounds like a good idea then there's a good chance that it will get accepted. Pretty much any idea is going to need at least some critiquing before it gets merged so don't get discouraged!

``` admonish tip "Design Principles"
If you want to improve your chances, it's recommended that you read the [SS14 Core Game Design](en/space-station-14/core-design.md) document to get a high-level overview before you start writing, as it'll provide context for why things are the way they are.

PR'd design documents should also follow the [Decorum Guidelines](./feature-proposals/expected-feature-proposal-decorum.md).
```
