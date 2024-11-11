## ECS FAQ
**Q**: Whats the difference between E/C and ECS?

**A**: The E/C architecture was popularized in 2003 by the Unity Engine. ECS+Events is a better architecture than the Unity style E/C architecture. E/C uses component messages which involves putting logic in components. ECS is a specific design that's optimized for parallelism and cache friendliness. ECS downgrades entities from having their own code to just being a bundle of components, and does the same for components, loading all the work onto systems. The idea is a system can be optimized to do it's job in a massively parallel manner, and systems themselves can be executed in parallel with dependency resolution.

---

**Q**: So why do components not use encapsulation? (i.e. private members.)

**A**: First of all, components cannot use encapsulation because then they would have logic them, which would conflict with the ECS principles we follow. Encapsulation makes no sense when components are simple data containers, as they have no logic. Furthermore, if the purpose of encapsulation is to prevent coders from directly modifying underlying component members instead of going through specific entity systems, there are better ways to prevent that.
Documenting/commenting the code, reviewing PRs and using the new `Friend` attributes.

---

**Q**: Why were interfaces in components replaced by systems and events?

**A**: Using interfaces had very poor performance, events and systems are significantly faster, aside from more powerful and maintainable. Aside from that, using interfaces in components meant they needed to hold logic, violating one of our main ECS principles.

---

**Q**: And an entity is a collection of components with an identifier?

**A**: An ideal entity is just an identifier, and its components are stored elsewhere, efficiently.
The point is data oriented design. The identifier is just an index into several one-component-type-only arrays in most performant setups. Components have no code, no behaviour, nothing, just data fields.
Systems are supposed to do the behavior/logic.

---

**Q**: So components act like tags?

**A**: Yes. Components are data storage, essentially tags with configurable data. Entity Systems act on components, and their data.

---

**Q**: So the systems are just looking for components on entities?
**A**: Yes and no. The ideal system doesn't know about the entity at all, it only knows the components it acts on.

---

**Q**: So when you need an interaction between two components what looks at both of those components and goes "oh these need to work together"?

**A**: #1 It's best to avoid these kinds of relationships in the first place.
#2 You have a 3rd system (so you have A and ASystem, B and BSystem, you'd have an ABSystem that gets a list of tuples of (A,B) to act on).
For example, a player rendering system might need access to 3-4 components, but that's valid for its use case (in, e.g., a roguelike).

---

**Q**: What does `RaiseLocalEvent` do?

**A**: It raises an event, locally (as opposed to networked). There are two overloads to it. One only takes the event, and will raise it broadcasted. And the other takes in an `EntityUid` and the event to raise it directed to an entity, and has an optional parameter to also raise it broadcasted.
