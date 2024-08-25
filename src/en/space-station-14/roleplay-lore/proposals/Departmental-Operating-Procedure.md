# Departmental Operating Procedure (DOP)

## Abstract

--- 

The DOP is an in-character set of guidelines oriented towards MRP servers. Each department will have it's own 'Operating Procedure' that will prepare it for any encounters it may face while in space. This will serve as a way to encourage roleplay and more belivable in-character behavior. 

The DOP will act as a guideline for departments to follow but not rules. This will allow for chaos to still ensue even when everything goes according to plan. 

## How will this look per department?

---

### Command: 

Command will follow the "Command Operating Procedure"(COP), it will feature a "Chain of Command", "Bolting Procedure", "Alert Procedure", and a "Commanding Officers Work Behavior Guideline"

#### Examples for Command: 

##### Chain of Command 

```mermaid
graph TD;
    subgraph Standard Alerts
    idG[Under Green Alert]-->idCC1[Central Command];
    style idG fill:#5ce65c,stroke:#333,stroke-width:4px
    idCC1-->idC1[Captain];
    idC1-->idHOP1[Head Of Personnel];
    idHOP1-->idG1[All head of staff are equal below HOP];

    idB[Under Blue Alert]-->idCC2[Central Command];
    style idB fill:#59b5f7,stroke:#333,stroke-width:4px
    idCC2-->idC2[Captain];
    idC2-->idHOP2[Head Of Personnel];
    idHOP2-->idB1[All head of staff are equal below HOP];

    idR[Under Red Alert]-->idCC3[Central Command];
    style idR fill:#cd1c18,stroke:#333,stroke-width:4px
    idCC3-->idC3[Captain];
    idC3-->idHOS1[The Head of Security is in command over Security issues during red alert];
    idHOS1-->idR1[All head of staff are equal below HOS];
    end
    subgraph Non-Standard Alerts

    idY[Under Yellow Alert]-->idCC4[Central Command];
    style idY fill:#ffd32c,stroke:#333,stroke-width:4px
    idCC4-->idC4[Captain];
    idC4-->idCE1[The Chief Engineer is in command over Engineering issues during yellow Alert];
    idCE1-->idY1[All head of staff are equal below CE];

    idV[Under Violet Alert]-->idCC5[Central Command];
    style idV fill:#7f00ff,stroke:#333,stroke-width:4px
    idCC5-->idC5[Captain];
    idC5-->idCMO1[The Chief Medical Officer is in command over Medical issues during violet alert];
    idCMO1-->idV1[All head of staff are equal below CMO];
    end
```

### Security: 

Security will follow the "Security Operating Procedure" (SOP), it will feature "Security Dresscode", "Optimal Proccessing Time Guideline", "Scene Response Guideline", "Evidence Handling and Collection Guideline", and "Interrogations 101" 

I plan for these to add not only some interesting guidelines that will hopefully improve roleplay, but to also add lore. You may have noticed at this point but a lot of these are named like guidelines you would see in an office, and that is sort of my intention. I am hoping to add lore friendly Nanotrasen guidebooks for each department. With fun tidbits and interesting insights to the departments. 

### Engineering: 

Engineering will follow the "Engineering & Atmospherics Operating Procedure" (EAOP), it will feature "Ship Modification Guidelines", "Departmental Repair Guidelines", and "Maintaining Clean Air"
