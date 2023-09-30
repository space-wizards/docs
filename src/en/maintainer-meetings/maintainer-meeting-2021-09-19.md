# 2021-09-19 - Maintainer Meeting Notes
```admonish info
Any decisions taken in these notes may no longer be applicable.
```

Attendees:  
Paul  
Smug  
Silver  
Vera  
PJB  
Shadow  
Mirrorcult

# Overall Summary

Next Meeting Items:
- have a moderator
- buy pjb a MoMMI plushie for the meetings
- less ideaguying, more concrete topics

Action Items:
- combat and disarm shouldn't be actions
- PJB fix UI (or anyone else)
- multi hotbar (switching with shift+num) should be optional, so it isn't used accidentally.
- add the ability to perform actions from the Action List Menu
- Resolve should assert UIDs match in debug only.
- Code wide-chat.
- add as an optional UI style.
- Code Shuttles first. Revisit this after.
- Fix Ui for lathes and research
- Investigate better research server sync mechanic
- Delete research code. Maybe from memory too
- Investigate KSP style point return
- Investigate Point Types
- Balance point receiving mechanics.
- Add Debug Only UI for errors. Make it on HUD and hard to miss on debug
- Enforce naming things OnX instead of HandleX. Use OnEntityEvent vs HandleEntityEvent etc
- Investigate how shuttles would be created.
- Shuttles should be able to fly and warp between z levels
- Investigate Shuttlebombing as a problem.
- admin tools and logging
- EU/US Biweekly playtests.
- split game admins to EU/US
- Three month limit on progress reports.
- Two month minimum for progress reports.
- Fix Slow Tests. Fix Test framework to be fast and cancer free
- Write Docs on how to write Tests
- what should have required tests: medium to large changes, systemchanges
- Write docs for ss13 dev transitioning like system xyz and you or byond to C# for byond refugees
- YAML Real time Linter. Language server
- GOTO YAML
- XAML Linter hot reloading, Previewing
- Fluent Linter
- Custom editor for yaml prototypes/constructiongraphs.
- worldline debugging
- save states
- test pooling

# Individual Discussions

## Action Bar
**Summary: Actions should be used for item actions & spells etc. Combat & Disarm just dont really belong there.**

Discussed Items:
- using is a pain (especially combat & disarm action)
- combat is so specific it should just be a button
- alt click should be disarm in combat mode
- ui broken (pjs fault)
- Having to bind "scream" (for example) to the bar to use it is dumb. Specially if you're only gonna use it once or on special occasions.

Action Items:
- combat and disarm shouldn't be actions
- PJB fix UI (or anyone else)
- multi hotbar (switching with shift+num) should be opt in so it isn't used accidentally.
- being able to perform actions from the Action List Menu

(18:12 -- People distracted by SS14 in-game chess)(they lost btw)
(18:16 -- PJB can smell her dinner already. Oh no.)

## Entity System Method Resolves
Summary: Everyone agreed that ES resolution works fine now. Resolve testing only in debug should assert matching UIDs between server and client.

Discussion Items:
- Everyone seems to agree that this is the cleanest way to do it?
- resolve should assert that the entity UIDs match so components don't get mixed. (but only in debug!!)

Action Items:
- Resolve asserting UIDs match in debug.

## Wide-chat UI
Summary: code it as an option, leave it off by default, evaluate maybe making it default later.

Action Items:
- Code wide-chat.
- add as an optional UI style.

## Salvage Crew
Summary: Code Shuttles. Revisit afterwards.

Discussion Items:
- do we really wanna focus on this right now?
- probably want shuttles & docking first

Action Items:
- Code Shuttles first. Revisit this after.

## Research
Summary: Code Shuttles. Revisit afterwards.

Discussion Items:
- UI for lathes and research is bad
- the code and syncing with the server is bad
- ctrl+a backspace the code
- can I ctrl+a backspace it from my memory?
- KSP-style diminishing point returns?
- different types of points?
- avoid continuous points source or make sure they're not op

Action Items:
- Fix Ui for lathes and research
- Investigate better research server sync mechanic
- Delete research code. Maybe from memory too
- Investigate KSP style point return
- Investigate Point Types
- Balance point receiving mechanics.

(18:27 -- pjb announces there is a meteor swarm (AND CARP) on station)(now xenos)

## Exception tolerance in debug
Summary: We need a debug ui that shows errors

Discussion Items:
- a debug-only ui that shows the errors that occur (make it obvious)
- yes exception tolerance

Action Items:
- Add Debug Only UI for errors. Make it on HUD and hard to miss on debug

## Minor formatting naming like OnEntityEvent vs HandleEntityEvent.
Summary: Format Naming Discussion for OnX vs HandleX prefixes. Use OnX.

Discussion Items:
- on- because it's shorter

Action Items:
- Enforce naming things OnX instead of HandleX. Use OnEntityEvent vs HandleEntityEvent etc

## Shuttle
Summary: Investigate Creation, Flying, Warping and Shuttlebombing.

Discussion Items:
- how would players create a shuttle?
- cargo shuttle should be autonomous/untamperabler
- shuttles should be able to fly and "warp" (go between z levels)
- not sure how to handle remote shuttle control. Necessary for latejoin miners but abusable if shuttle not static (can get lost)
- shuttle bombing limited damage

Action Items:
- Investigate how shuttles would be created.
- Shuttles should be able to fly and warp between z levels
- Investigate Shuttlebombing as a problem.

## Scheduling Playtests
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- our current game admins are... slightly uncommited
- we desperately need admin tools & logs
- we're not building a community, but recruiting admin ties into this
- we should get a roadmap to see when we're ready for building a community?
- do one us & one eu time, biweekly
- split eu and us game admin

Action Items:
- admin tools and logging
- EU/US Biweekly playtests.
- split game admins to EU/US

## progress reports
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- PJB proposed smaller progress reports every now and then
- Having a "max amount of time between progress reports" was discussed
- Releasing a progress report before playtests was discussed
- need better way to keep track of stuff for progress reports
- robust film maker ???

Action Items:
- Three month limit on progress reports.
- Two month minimum for progress reports.

(19:11 -- PJB mentioned how Unitystation gets more upvotes than us on Reddit. All hell broke loose.)

(19:15 -- Vote is held for progress report time. using discord reactions :clap: :clap:)
result: six weeks won with 7 votes.
or not
ok
MORE wins 2months

(19:20 -- PJB screwed up the voting reaction order, we just realized. Some people voted wrongly due to this. Laughs were had. curtains roll, exit stage left. )

(19:24 -- PJB: "Discord screwed up the order don't blame me")

(19:25 -- PJB said "I'm hungry" and left. Just like that.)

## CI/Testing
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- Speed is a concern with CI. Integration tests are very slow.
  But why are they slow: because they we reuse the server
  -> we need to have a possiblity to reset the server instead of making a new one
  they are also not pooled/multithread.
- they are also ass to write, which means its alot of effort.
  write docs on how to write tests
- make it not cancer

Action Items:
- Fix Slow Tests. Fix Test framework to be fast and cancer free
- Write Docs on how to write Tests
- what should have required tests: medium to large changes, systemchanges

## Reaching out to (ss13) devs
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- mirror wants to make docs specifically for ss13 devs:
  here is what it looks like in byond, here is what it looks like in ss14. helping devs transitions
- passively attract devs by helping them transition, dont poach people
- more "system xyz & you"

Action Items:
- Write docs for ss13 dev transitioning like system xyz and you or byond to C# for byond refugees

## Tooling!!!! that doesnt suck ass
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- yaml goto, real time linter. language server
- xaml linter, (preview), hotreload, not make it ass for vs, automatically call robustxamlloader.load(this)
- ref events are ass to work with
  have an analyzer/attribute? name it a specific way?
- ftl linter, markup
- editor for yaml, prototypes, constructiongraphs. in-engine? per command?
- worldline debugging (@pjb)
- save state of game to save ourselves from redoing testing enviroments all the time
- do a doc in ss14docs for this (tooling ideas)
- TEST POOLING (WIP)


Action Items:
- YAML Real time Linter. Language server
- GOTO YAML
- XAML Linter hot reloading, Previewing
- Fluent Linter
- Custom editor for yaml prototypes/constructiongraphs.
- worldline debugging
- save states
- test pooling

## Roadmap
Summary: Playtest Scheduled for every two weeks. We will have US/EU seperated.

Discussion Items:
- 

Action Items:
- Law !@#!$>.
- Admin tools and logging
- Test suite fix
- Debugging (Debug ui, exception tolerance in debug)
- Tooling suite
- medbay
- traitor

## Conclusion
Summary: for the next meeting, maybe have a moderator and less ideaguying, more concrete topics

Discussion Items:
- 

Action Items:
- for the next meeting, maybe have a moderator
- buy pjb a MoMMI plushie for the meetings
- less ideaguying, more concrete topics
