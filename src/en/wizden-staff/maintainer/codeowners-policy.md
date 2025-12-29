# Codeowners Policy
This document outlines the Codeowners policy, a permission granted to Maintainers by Lead Maintainers.

This permission allows them to process and merge pull requests on their own accord, including pull requests authored by the codeowner.

## Goals
The codeowners policy aims to achieve the following:
1. **Increase velocity and turnaround time for pull requests that touch a system.**
   1. Many abandoned/derelict systems have been adopted by a maintainer who now knows the system extensively. Oftentimes, work on a system is blocked by pull requests that would normally require another maintainer to re-learn the system in order to give a proper review. This results in work being stalled for months, as learning the system is often a great effort that is not feasible to exert. The codeowners policy allows maintainers who know the system extensively to process pull requests touching those systems without requiring another maintainer.
2. **Pin a system's knowledge and maintenance burden onto a maintainer instead of the maintenance team at large.**
   1. Seeking advice, reviews, and knowledge about a system can take a hot minute as the knowledge surrounding that system isn't held by all maintainers. By assigning a dedicated maintainer to handle a system, contributors can talk to said maintainer directly about needed work.
      1. Note that the codeowners policy is no excuse for neglecting documentation.

## Policy

### Supervision
Maintainers who perform codeowner actions are overseen by the Lead Maintainers.

They are to make sure that the aforementioned policy is followed.

### Formation
Maintainers are granted codeowner permissions for their chosen system by a Lead Maintainer.
Lead Maintainers can also deny the permissions if they do not deem the maintainer to be fit for the system, or if the requested system is undefinable in scope.

A maintainer can request codeowner permissions in any format, but it should ideally be in a space where it is documented and the active maintainer team knows about it (ex. a maintainer meeting).

### Revocation
Lead Maintainers may revoke codeowner permissions from a maintainer at any time.
Revocation is usually due to the following reasons:
- The maintainer has refused to implement tests or demonstrate performance improvements via benchmarks.
- The maintainer is merging large swaths of undocumented code.
- The maintainer exercises negligence in making sure that their code does not contain bugs.
- The maintainer is present for submitting and merging pull requests, but largely absent when bugs caused by them need fixing.

### Scope
The system that the maintainer chooses to become a codeowner for must be definable in scope.
Maintainers cannot simply request to claim all `EntitySystem`s, rather the request must be for a specific group of systems or mechanic that the maintainer is familiar with. Examples include:
- Atmospherics
- Solutions
- Physics
- Explosions
- Pow3r

### Permissions and Requirements
Maintainers with codeowner permissions have greater power over their area, however they must furfill specific requirements before exercising it.
1. **Codeowners can process pull requests targeting their scope by themselves.**
   1. No second review is required for merging.
   2. Codeowners can process their own pull requests (self-merging).
   3. The pull request must have tests that properly cover the changes.
   4. If the pull request targets performance improvements, the improvements must be demonstrated by a benchmark.
   5. The pull request must be open for at least 3 days before merging.

There is no restriction for regular maintainers processing pull requests that touch a scope claimed by a codeowner.
However, it is recommended that maintainers, when doing so, defer to the codeowner in question.


