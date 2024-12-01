## ECS FAQ

**Q**: Whats the difference between E/C and ECS?

**A**: The E/C architecture was popularized in 2003 by the Unity Engine. ECS+Events architecture offers advantages over the the Unity style E/C architecture. E/C uses component messages which involves putting logic in components. ECS is a specific design that is optimized for parallelism and cache friendliness. ECS downgrades entities from having their own code to just being a bundle of components, and does the same for components, loading all the work onto systems. The idea is that a system can be optimized to do its job in a massively parallel manner, and systems themselves can be executed in parallel with dependency resolution.

---

**Q**: Why do components not use encapsulation? (i.e. private members.)

**A**: Components cannot use encapsulation because logic would conflict with the ECS principles we follow. Encapsulation makes no sense when components are simple data containers, as they have no logic. If the purpose of encapsulation is to prevent coders from directly modifying underlying component members instead of going through specific entity systems, then there are better ways to prevent that such as documenting/commenting the code, reviewing PRs, and using the new `Friend` attributes.

---

**Q**: Why were interfaces in components replaced by systems and events?

**A**: Interfaces have poor performance, events and systems are significantly faster, aside from being more powerful and maintainable. Interfaces are intended to ensure that a class contains logic. Using interfaces on components violates the main ECS principal of separation of data and logic.

---

**Q**: Is an entity is a collection of components with an identifier?

**A**: An entity does not directly aggregate components. Instead, several auxiliary data structures bind an `EntityUid` to the locations of components. ECS users need not care about how the components are stored, as functions provided by RobustToolbox obscure this complexity.

---

**Q**: Do components act like tags?

**A**: Systems act on entities with specific components. By adding or removing components the set of systems that operate on an entity changes. Viewing the components as a tag for whether a system operates on an entity is valid. However, within ECS, "tag" is frequently used to describe components with no data.

---

**Q**: Systems are just look for components on entities?

**A**: Yes, systems will operate directly on components but also are able to operate on the source entity via the `EntityUid`. Operations using the `EntityUid` are more costly than operating directly on the components.


---

**Q**: How do systems operate on more than one component?

**A**: Although a system for component A and another B may exist, this does not exclude the creation of other systems on A and B simultaneously. Systems can acquire singles, pairs, triples, etc. of components to operate on simultaneously. Each pair, triple, etc. will all come from the same entity. Operating on multiple components is costly.

---

**Q**: What does `RaiseLocalEvent` do?

**A**: It raises an event locally on the current machine as opposed to raising an event over the network. There are two types of local event: broadcasted and directed. Broadcasted events are sent to all listeners. Directed events take an `EntityUid` to direct the event to a specific entity. Directed events can be extended to broadcast events by supplying an optional parameter to also raise it as broadcasted while still containing an `EntityUid`.
