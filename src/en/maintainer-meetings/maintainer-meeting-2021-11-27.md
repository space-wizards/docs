# Maintainer Meeting Notes - Date: 27 Nov 2021
=
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

Paul  
Vera  
Smug  
Visne  
Acruid  
PJB  
Electro  
ShadowCommander  
Remie  
Sloth

# Recruiting new game admins | Vera, Paul
- Application form
- Staff application forums
- no irc
- perhaps recruit some ss13 admins?

# How do we cope with the many PRs we've been getting | Paul, Sloth
- Having a "How to make your pr more reviewable"-guide
    - Don't make a bunch of miscellaneous additional changes in a PR, e.g. changing the heat resistance of a pair of gloves alongside your PR adding a new gun
    - Don't make a bunch of formatting changes in a file if you change 1 line. It makes the review significantly more difficult to parse what actually changed and can generate conflicts for other PRs.
    - Once a review has started on your PR do not force push to it.
    - prefer multiple small PRs over one large PR
- simply have 100% test coverage it reviews itself

From https://docs.spacestation14.io/en/maintainer-meetups/secret/2021-10-30-meetup
(Also here now! https://github.com/space-wizards/space-station-14/issues/5542)
![](https://i.imgur.com/vPY8qhP.png)

We need a knowledgebase, so contribs can find everything important at once.

Engine code quality needs to go up.

We need to:
- write more docs, especially super simple 14
    - most common things people are pr'ing
        - how to use containers
    - go through prs to see what people are doing
        - if you are reading the code, write down what you are looking for
    - playerfilters
    - make subfolder in docs for drafts
        - drafts can just be bullet points/a skeleton/outline

# Making Transform not required for entities | Vera
- for serialization
  ![](https://i.imgur.com/BY3W0oM.png)
- free VV, no extra work IT ALREADY WORKS!!!!
- whats
- simply support serializing entity systems instead
    - make systems entities
        - way too powerful
- how to handle saving non-transitive data used by entity systems

# Chat filter | Shadowcommander
implement the chatfilter, because admins are doing it rn
remember to save it in base64 or something so we dont get bopped by github
to sum it up: dont allow to send, notify admins, give them a popups
- use unicode's "confusables" information to find chars that look like eachother, and use that to bad "variants" of no-no words


# Roadmap | Vera
"No" - Smug
"Why" - Vera
"It would be extremely painful" - Smug
"You're a big guy" - Vera
"For you" - Smug

- New roadmap:
    - Body system
    - thats it
    - dont forget photography
    - TBF the last roadmap had ideaguys all over it

- make the roadmap make the last topic of each meeting
    - this way we all get input
    - the roadmap is at worst 2 weeks out of date

# ComponentProtoName attribute | Sloth
![](https://i.imgur.com/kzYoNoF.png)  
https://docs.microsoft.com/en-us/dotnet/core/compatibility/core-libraries/6.0/static-abstract-interface-methods

# Stable/bleeding edge branches | Mirror
- where is mirror, wake her up!!!!!
- we are currently very volatile compared to ss13
- pause fukken updates to the servers somehow PLEASE
    - thistbh

# Synthetic stress test of USWest | Mirror
PaulVS + USWest Hardware + .NET 6 + Atmos/Solar optimizations

# Should we continue running biweekly playtests | Mirror
considering we get 20-40 pop pretty much constantly
- keep doing playtests
- they are good to remind people we exist
- better player stat tracking? like retention, etc

# Roadmap content
- emergency shuttle
    - auto shuttle movement
- gamemodes/antags
    - nuke ops
    - lings?
    - blob?
    - cult?
- EL BODY SYSTEM
- Salvage
- Teleporters (Beam me up (Scotty))
    - telescience
- body system but again
- body system (get smug to code it)
- __***ENGINE EDITOR***__
- Tutorial
    - In game guides

# Post-meeting ~~jstris~~ tetr.io! | Visne, Tomeno
- when the hwehgneh the isss suss
    - ![](https://cdn.discordapp.com/emojis/818484273995841547.png?size=32)
