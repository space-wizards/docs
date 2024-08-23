# Station AI

| Designers      | Implemented | GitHub Links                                                                      |
|----------------|---|-----------------------------------------------------------------------------------|
| metalgearsloth | :warning: Partially | https://github.com/space-wizards/space-station-14/pull/30944 and accompanying PRs |

## Overview

Station AI is an overseer of the station, providing a centralised means of providing information to the crew.
This proposal is targeting the MVP of station AI with no strong long-term direction in any particular way that people might have strong feelings about and significantly different technical challenges (e.g. camera-only gameplay).
It covers:
- AI Visibility and the means to counteract it and provide information to the crew.
- Basic interactions with station equipment.

Other mechanics such as shunting, malf AI, TTS, tracking etc are to be done and prototyped later once people have a base to work off of.

## Background

At the moment it's difficult to track stealth antags or individual crew members. Clicking around cameras is so slow it's unusable outside of checking fixed high-value areas (e.g. vault). As soon as someone leaves your screen they may as well not exist as you can't catch them.

AI adds another mechanic to stealth antags as they have a centralised agent to work around.
They can choose to deal with it in one of several ways:
- Cut cameras and leave an obvious dark zone that may have something happening.
- Leave it and hope the AI doesn't notice you.
- Do you cut door wires in advance and hope no one notices to ensure the AI can't stop you from escaping.

To achieve this several features are implemented:
- Cameras provide AI visibility.
- Where the AI doesn't have direct visibility it should have navmap visibility (given they still have access to crew monitoring) so they can still see station layout.
- Cameras can be cut / mended / constructed.
- The AI has access to consoles such as crew monitoring to increase their station awareness (long-term they should also get chat tracking but chat code).
- AI can be destroyed directly or put into an intellicard to fully remove them from their role.
- AI upload so their laws can be changed. They're more-or-less bound to the same role as borgs.