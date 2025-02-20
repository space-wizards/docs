# Botany 

| Designers | Implemented | GitHub Links |
|---|---|---|
| MilonPL | :x: No | TBD |

## Overview

This design document proposes the removal of botany as a standalone sub-department and its integration into the kitchen gameplay loop. The goal is to streamline plant growing mechanics while making them more meaningful as part of food preparation, turning hydroponics into a side activity for chefs rather than a separate role.

## Background

Currently, botany suffers from several issues:
- Heavily RNG-based gameplay with little player agency
- Limited interaction with other departments except kitchen and medical
- Lack of meaningful progression or goals
- Redundant role that could be better served as part of existing gameplay loops

By integrating botany into the kitchen, we can:
- Give chefs more varied gameplay during slow periods
- Maintain the essential function of growing ingredients
- Create a more focused and purposeful growing system

## Features to be Added

### Kitchen Garden

A compact hydroponics area should be mapped directly adjacent to or within the kitchen. This area would include 3-6 hydroponics trays, depending on the station's size. The limited space encourages choices about what to grow rather than mass production.

### Mutations Overhaul

Mutations should remain as an optimional optimization strategy:
- Base plants should be viable without mutations
- Mutations should provide meaningful but not essential benefits, such as:
  - Higher yield
  - Shorter growth times
  - Different growth conditions
 
### Growing Mechanics

Each tray contains a solution of water and nutrients. Basic nutrient soluition is required for growth, but optional fertilizers can enhance it.

Plants are affected by their environment:
- Temperature: Each plant has an optimal growing range
- Atmosphere: Plants need proper gas mix (O2/CO2 balance)
- Light level: Different plants may require different light levels.
- Pressure: Atmospheric pressure that affects plant health.
- Solution pH

The basic growing system should remain simple but rewarding:
- Water and nutrient requirements
- Clear visual growth stages
- Basic maintenance needs (pruning, pest management)
- 3-5 minute growth cycle for basic plants

## Game Design Rationale

Moving botany into the kitchen creates a more cohesive food preparation gameplay loop while maintaining the essential functions of growing plants. This change addresses several current issues:

- **Focused Role**: Instead of having two somewhat-related sub-departments, we combine them into one more meaningful role
- **Better Pacing**: Growing plants becomes a background task while preparing food, filling downtime

## Round Flow & Player Interaction

A typical round flow might look like:

1. Chef starts shift by planting basic ingredients needed for common meals
2. While plants grow, chef prepares initial meals from stored ingredients
3. During slow periods, chef tends to plants and plans next growing cycle
4. Medical staff can request specific plants, creating additional tasks
5. Failed crops create meaningful setbacks without completely disrupting gameplay

### Main Things to Consider

- Balance growing times to maintain engagement without becoming overwhelming
- Ensure the system remains simple enough to be a side activity
- Create meaningful choices about what to grow and when
- Maintain the ability to grow medical plants without making it too easy
- Design consequences for neglecting plants that don't completely devastate kitchen operations

## Technical Implementation Notes

### Core Structure

The system will be built around three main concepts:
- Plant holders (hydroponic trays) that c ontain the solutions and can host plants
- Plant entities that can grow and be harvested
- Plant data that defines the characteristics and mutations

### Main Components

1. PlantHolderComponent
    - Stores the solution
    - Hosts a single plant entity
    - Tracks environmental conditions

2. PlantComponent
    - Stores the growth progress
    - Handles mutations
    - Defines the ideal growing conditions
  
### Additional Considerations

- Solutions do not have pH levels, one workaround would be to have different reagents metabolized to increse/decrease the pH.
- There's no way of checking the light level on a tile. Checking the nearby lights might work.
- Should be implemented in a way that allows easy future expansions, such as different mutations.
