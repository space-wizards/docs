# ATMs, Money Accounts, Starting Money

| Designers | Coders | Implemented | GitHub Links |
|---|---|---|---|
| MichaelChessall | MichaelChessall | :x: No | TBD |

## Overview

Adds a constructable, static ATM machine that characters can access to withdraw or deposit money into a personal account. When characters first join a round they will be given a random amount of money in some combination of cash and money deposited into their account based on the role they've been assigned. These additions will lay the groundwork for future economic content.

## Background

Most Space Station 13 forks include ATMs, personal money accounts and starting money for newly joined characters. In many cases this money is just a prop for RP purposes, as many versions of SS13 dont have a clear use case for it and character-based economy can be a hard thing to make meaningful in short, chaotic round based gameplay. However the presence of money accounts is ubiquitous in SS13 and that has allowed downsteam projects to build a lot of gameplay around character-based economy, while the feature is lightweight enough and harmless enough to provide net value in the form of a prop for RP, even where there are not clear gameplay use cases for the money.

Presently in SS14, cash can be found very rarely on the map and can obtained through the cargo department doing a direct withdraw from it's budget. Cash can be deposited back into the cargo budget where it can be spent. Most characters do not get an opportunity to either earn money, spend money or find money as both the only source and only gameplay use case are centralized to the cargo department.

## Features to be added

Constructable, destructable ATMs will be added to the station maps which allows characters to access a personal money account where they can deposit and withdraw money. Characters will be given a random amount of money on round start to seed their bank accounts. The ATMs will be accessed without any PIN or ID verification, and characters will only be able to access their own personal money account.

The starting money ranges will need to be balanced around any use cases that the money has, which is currently just requisitioning supplies through the cargo department.

## Game Design Rationale

Money is fun. Characters earning, spending and having currency is a common form of progression that players will be familiar with.

Money can be used to motivate a characters actions (through seeking money) or motivate other people (through spending money). It is a vector for both cooperation and competition.

Money is a world building tool. The money a character starts with was presumably earned during prior shifts for the corporation. Having individuals possess their own money is a worldbuilding prop which helps ground the 'Corporate Space Station' setting.

Economy mechanics in SS14 are suffering from a lack of supporting foundations. Character-focused use cases for money dont exist because cash is too scarce. ATMs, money accounts and starting money will lay a groundwork that future economic mechanics can built upon. Downstreams will benefit from having a centralized starting point for character based economics.

## Roundflow & Player interaction

Characters will start with a small amount of money split between cash in their inventory and money deposited into their account. At any point a character may withdraw or deposit cash from an ATM.
This money could be exchanged between characters such as tipping a bartender or perhaps ordering a specific food. The service department would likely be the most common place where money would be used as an RP prop.

More practically, cargo has an interest in depositing money into its budget account so that it can order more supplies. A gameplay focused Quartermaster may decide to transfer their entire net worth into the cargo budget where it has gameplay utility and that money collection may even extend to other employees of the cargo deparment. When characters are handing over their own personal funds to the department so that it can be spent on things they don't get to own afterwards, that feels like a gameplay incentive to act out of character. This is a problem that could be solved in a few different ways and may require further discussion, but one partial solution would be to balance the starting money values so that the money isn't really worth taking and doesn't have an appreciable balance impact on cargo. If and when more use cases for money are added the problem would be made less prominent.

## Administrative & Server Rule Impact (if applicable)

As detailed in the prior section, this feature can create an odd incentive to metagame by handing personal funds over to the cargo department so that it can be used by the station. Potentially this creates more cases of metagaming in MRP and HRP servers.

# Technical Considerations

I'll implement a moneyaccount component for the mind of humanoid characters when they join the game. Based on their assigned role, a random amount of money will be divided between their money account and as physical cash within their inventory. The moneyaccount component will track the current amount of money and be used when a mob accesses an ATM.

The Job Prototype will gain two integer values representing the range of starting money for that job. Default to 0, 0.

I'll create a new machine, the ATM, which is constructable and destructable. It will use a very small UI which displays the current amount of funds, has a field for a number to be entered and a 'withdraw' button. When the withdraw function is used the ATM transfers the money out of the account and into cash, similar to the digital requisition board. The ATM machine may need a new sprite to meet the art design requirements. An existing ATM sprite for SS13 is available to port, but if it's deemed unacceptable I can produce an ATM sprite that meets the design requirements.

Prebuilt versions of this machine will be added to the maps in a few limited spots, perhaps 1-2 per map and generally around doorms or cryo.

I want this implementation to be as limited in scope as possible while still providing a coherent and functional gameplay addition. Upon completion of this feature another design document can be drafted to implement features like the EFTPOS (A portable POS that can be used to transfer money directly from one player account to another) and a transaction tracking system where withdraws, deposits and direct transactions are logged for each money account.