# Feature Proposals

If you are considering adding or reworking some major component of the game it's recommended that you submit a proposal before you actually start coding whatever it is you want to do.

Feature Proposals help gain a consensus on what the other contributors and maintainers believe is the way that the feature should be implemented and how it should interact with the rest of the game.

Doing this will save a lot of headaches and rewrites as you will know what your deliverable is from the get-go.

## What is a Design Doc?

A design document is a high level summary of whatever you're proposing to add to the game. They serve to get the nebulous ideas down on paper so it's easier to see how exactly those ideas will mesh with the rest of the project. They generally have a few parts.

1. **Why the feature is being proposed**, which can be as simple as 'I think it would be cool' to as specific as 'I noticed ABC problems with Cargo's game-play loop and want to add XYZ to remedy those problems'.

2. **A high level summary of what the feature actually is**, how the feature engages with players, and how the feature interacts with other major parts of the game.

3. **A more detailed summary of the proposed mechanics for the feature**, how players are intended to interact with those mechanics, and how those mechanics involve or are involved with other parts of the game. You don't need to go into every specific case, it's enough to say that there should be chemicals filling specific roles and not detail the exact chemicals you

These don't have to be discrete sections and shouldn't be.

When you're detailing the mechanics it's probably a good idea to detail how the players will interact with those mechanics and how the way the players interact with those mechanics benefits the game.

If you want to see examples of successful design documents all of the accepted, but unimplemented, design docs can be found in the "Design Proposals" section below.
Design documents that actually got implemented eventually transmute into the feature docs in the "Space Station 14" section.

```admonish warning
**Do not**:
- Include pseudocode level descriptions of how your feature works. That's for after the proposal has been accepted and you're actually implementing the thing.
- Specify numerical amounts for every item, field, or mechanic. That's for eventual balance bikeshedding; for example it's enough to say that a disease will have one, several, or many symptoms.
- Forget to include _how_ players should interact with your features. SS14 is a multiplayer game and how the players engage with your mechanics is more important than the specific mechanics they engage with.
- Write an entire, actual FSD or SRS. It's not and will never be required as it constitutes egregious overkill for a project of our size and structure.
```

## Does This Need a Design Doc?

Before you make a proposal, you should ask yourself if this needs to be a proposal.

If it's something like adding a single gun or a couple simple plants it probably won't. On the other hand if you are adding an entire subdepartment like anomalies/xenoarchaeology or a large reworking, then it definitely will.

A good rule of thumb if the new feature or rework you have in mind would require modifying the guidebook or one of the feature docs on this wiki, then it probably needs a design doc. Same if the proposal could be accurately described as 'reworking the entirety of X'.

## Making a Proposal

To make a proposal, you must:

1. Make a copy of the design proposal template located at [`src/en/templates/proposal.md`](https://github.com/space-wizards/docs/blob/master/src/en/templates/proposal.md).

2. Read through the relevant design documentation.

   - For gameplay-related proposals, read through [SS14's Core Design Documentation](../../space-station-14/core-design.md).

3. Write your proposal, following the [guide to editing docs](../../meta/guide-to-editing-docs.md).

4. When you are ready for your proposal to be reviewed, make a pull request.

5. Your proposal is approved when a maintainer merges it. This is a green light for you or someone else to go ahead and implement it. A maintainer will then link your proposal to the side bar of this development wiki.

```admonish tip "Unfinished Proposals"
If you don't think that your proposal is ready for maintainer scrutiny, but still want feedback on it you can PR it as a draft.

Drafts are less likely to attract people looking to get down to brass tacks, but still let people comment and give advice.
```

## Will my design doc get accepted?

No idea! What design proposals do or do not get in is determined by maintainer approval like normal PRs.

If you can get at least one maintainer to decide that it sounds like a good idea, there's a good chance that it will get accepted. Pretty much any idea is going to need at least some critiquing before it gets merged so don't get discouraged!

```admonish tip "Design Principles"
If you want to improve your chances, it's recommended that you read the [SS14 Core Design Documentation](../../space-station-14/core-design.md) document to get a high-level overview before you start writing, as it'll provide context for why things are the way they are.

PR'd design documents should also follow the [Decorum Guidelines](./expected-feature-proposal-decorum.md).
```
