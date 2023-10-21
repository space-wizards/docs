# Maintainer Meeting (09 Sep 2023)
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

**Time:** 09 Sep 2023 18:00 UTC

**Attendees:**
- ElectroSR
- ShadowCommander
- Sloth
- PJB
- DrSmugleaf
- Notafet
- Julian
- Visne
- faint
- TheQuietOne
- keronshb
- Lank

## Remove component lifestage properties | metalgearsloth
- Remove component lifestage properties (this is a long-term thing but mainly looking at stopping new code adding checks):
- 90% of the time it's a bandaid for other shitty code
- probably needs removing when we go to struct components in the distant future
- Can probably just check the entity lifestage in most bandaid cases instead anyway
- **Fund it**
- **Most component stuff can just check entity instead, not too hard to remove**
- **Removing entity life stage would be much harder**

## Remove Component.Deleted | metalgearsloth
- adds unnecessary overhead to some codepaths like TryGetComponent\<T> / HasComponent\<T>
- It's really only useful in cases where something is queued but not removed yet but even then I'm kinda suss
- we can probably start investigating after arch port is stable
- **Do it**
- **How are we delaying component changes to the end of the tick some day who knows**

## Use the pooled collections instead of List\<T> / HashSet\<T> etc | metalgearsloth
- Uses the ArrayPool to back the arrays
- Should reduce heap allocsTM
- https://github.com/jtmueller/Collections.Pooled
- we may need to import it anyway for arch
- **Yes in engine, to replace ObjectPool**
- **Don't sandbox Shared pools**
- **Pool objects shouldn't be returned by methods**
- **I don't like it because it makes spaghetti out of memory management, and is basically just a bad bandaid after you give up doing it properly™️** - PJB

## Arch and performance | metalgearsloth
- We should get AddComp<TComp1, TComp2> etc to have content start leveraging minimising archetype changes though not sure how we want to handle it.
- any other overloads we could think of
    - HasComp, RemoveComp, TryGetComp, EnsureComp
- how do we handle queries i.e. does content cache our existing queries, how do we handle not having .WithAll\<T> / .WithAny\<T> / .WithNone\<T>, do we cache arch queries and just have engine relay them, idk)
    - **Use query description in engine**
    - **If used from content, validate the types that the query handler asks for as Arch doesn't check (it just crashes)**

## NetEntities and handling unknown entities to the client | metalgearsloth
- NetEntities and handling unknown entities to the client: client may get netentity for something it might not know about yet (due to streaming or whatever else). How do we handle this and what's going to be the best way 3 years from now, e.g. some kind of handle for netentity + entity and entitymanager just updates the field when it comes in? 
- Right now client just leaves the entityuid and code just checks for trygetcomp / deleted and it will just suddenly work when the entity comes in but with the entityuids no longer matching (and the entity may not exist yet) this is no longer possible
- Like:
- Do networked comps just store NetEntity? This is kinda ugly and adds dictionary overhead to everything
- Do we somehow put a ref on entitymanager then update it when the gamestate comes in and the entityuid automagically updates?
- **https://discord.com/channels/310555209753690112/900426319433728030/1147795695286362112**

## Refactoring UpdateBoundStateMessage / whatever the fuck UI is doing to compstates | metalgearsloth
- do we just dump all the data on components
- any data not already comps just dump on a dedicated UI component?
- **"You can scroll two points down for the BUI entities topic"**

## Changing TryComp\<T>(out var comp) to TryComp(out T comp) for most usages | metalgearsloth
- We had this discussion a long-ass time ago, like 4 years ago
- the latter is shorter
- I preferred it but we ended up using the former
- I think performance is almost identical
- bottom text
- **If we enforce it, enforce it with an analyzer**

## BUI entities | PJB
- Opening BUI just creates an entity that handles the UI logic. UI data is in that entity's components. We can do composition for various types of behaviors like interaction range. Move it all to content. PVS filter it so only target player has vision over it. One entity per BUI session (player).
- Do we give a shit about optimizing UI states if two players view the same UI? Right now this allows re-using the data but it seems like such a minor thing it's not worth making the system more complex over
- gooey booey looey
- **When you code it, ez clap, we're all in agreement**

## Disallow using Math and MathF | moony
- and make people use the type-specific functions instead that .NET 7 added
- so for example Math.Pow(x, y) would be double.Pow(x, y)
- Math/MathF are only defined for a limited set of types and are overall a bit more "magical" for what types they allow (due to overloading), so being explicit about the type is cleaner and allows that implied API to be extended (MyNumberType.Pow(x, y) would be what you'd expect to exist instead of initially guessing Math.Pow(x, y)) 
- all the functions on Math/MathF have equivalents on the type being operated on for the C# builtin types
- including the constants, so for example float.Pi exists
- also the divide between MathF and Math is just plain confusing most of the time
- **When you write an analyzer for it, for engine only**

## *"the thrilling case of the  missing  documentation "* | mirrorcult
- ok can we admit “just ask us for access to edit the dev wiki” is a failed prospect. no one actually knows you can do that and if they do know they dont want to bother with the friction of finding out who to ask and waiting just to submit a fix. as a result the dev wiki is extremely atrophied
- oh my god PLEASE can we move it all to mediawiki or something, i dont care what it is wikijs was a bad idea and i just want something that anyone can edit and add articles to. please
- we really desperately need to do a full audit over the docs, not necessarily like add new stuff rn because i get thats effort but just make sure its up to date information and all useful pages are actually discoverable
- maybe think about mirroring codebase changes to docs site once we get something better like mediawiki. this would probably involve just linking to the docs page in GH and discord as the source of truth
- we REALLY need to make the docfx sites more visible and linked in more places (and docs in general but), discord channels/pins/github/forum/ingame literally everywhere please (and maybe give them better domain names theyre really bad rn) and also
  - add a ‘component glossary’ section to docfx which just shows all types that are registered components and what docs/fields they have. like half of the people in <#560845886263918612> ask for something like this and we just have to tell them ‘uhhh look in your IDE’ which is good when they already have the component they're looking for but terrible for when theyre trying to discover potential components they can use for some behavior
  - topy was working on this at some point but they are inactive now. if possible just revive their branch we really need this
- **When You Document It**
- **We'll host it for whoever wants to experiment with shit**
- **I saw the search bar on mdbook and I'm convinced**
- **Replace wikijs with mdbook**

## Early Access Roadmap
- **nothing on this roadmap matters except early access trailer.**
- A trailer for Steam
    - Also the >>>>**screenshots**<<<< for steam and the website
    - holy shit we have **replays** now
- gamemodes/antags
    - dynamic [c#16548](https://github.com/space-wizards/space-station-14/pull/16548)
    - revolutionaries [c#18477](https://github.com/space-wizards/space-station-14/pull/18477)
    - wizard
- The game runs like shit how do people play this
    - "IDK but maybe when I fix the watchdog you can figure it out easier" | 09/09/2023


Crashes / Critical bugs: (when are we moving these to GitHub)
=> till next time
like and subscribe
smash that button
~~did you know only 6% of contribs join this meeting?~~ According to YouTube's statistics, 
