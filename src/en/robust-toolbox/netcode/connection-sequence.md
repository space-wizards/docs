# RobustToolbox Connection Sequence

This is a complete sequence of what steps get taken when a client connects in RobustToolbox (and to some extent, Space Station 14). This is an incredibly involved and messy system that evolved over multiple years, and has many moving parts and sets of state. Oof.

## Basic overview

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Server
    
    C->>S: Lidgren Connection Attempt
    S->>C: Lidgren Connection Approval
    
    rect
        Note over C,S: Initial handshake
        
        C->>S: MsgLoginStart
        Note left of S: Server decides to auth or not
        opt Authentication
            S->>C: MsgEncryptionRequest
            create participant A as Auth Server
            C->>A: POST /api/session/join
            C->>S: MsgEncryptionResponse
            %% I'd use <<->> but my Trilium doesn't have Mermaid v11.0.0 yet.
            destroy A
            S->A: GET /api/session/hasJoined
        end
        Note over S: Connecting event is raised,<br/>content can deny connection if desired
        S->>C: MsgLoginSuccess
        Note over C,S: Both sides enable encryption if necessary
        Note over C,S: Both sides create NetChannel
    end
    S->>C: MsgStringTableEntries
    rect
        Note over C,S: Serializer handshake
        S->>C: MsgMapStrServerHandshake
        C->>S: MsgMapStrClientHandshake
        opt Client needs strings
            S->>C: MsgMapStrStrings
            C->>S: MsgMapStrClientHandshake
        end
    end
    Note over S,C: NetManager.Connected event<br/>Non-handshake messages are now allowed
    C-->>S: MsgConVars
    C-->>S: MsgConCmdReg
    par PlayerManager.NewSession
        Note over S: Server-side player session gets created,<br/>PlayerStatusChanged gets ran for first time
        S->>C: MsgSyncTimeBase
        Note over S: NetConfigurationManager.SyncConnectingClient
        S->>C: MsgConVars
        Note over C: Client-side player session gets created
        C->>S: MsgPlayerListReq
    and UploadedContentManager
        loop Send uploaded resources
            S->>C: NetworkResourceUploadMessage
        end
        loop Send uploaded prototypes
            S->>C: GamePrototypeLoadMessage
        end
    end
    Note over S: Player session is set to Connected
    S->>C: MsgPlayerList<br/>Contains Connected Status
    Note over C: Player session is set to Connected
    Note over S: Content sets client session to InGame
    S->>C: Starts sending game states
    Note over C: Player session is set to InGame
```
