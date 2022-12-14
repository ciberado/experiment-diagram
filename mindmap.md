%%{init: {
  'about': 'Mermaid diagram, https://mermaid.live',
  'theme': 'base', 
  'themeVariables': { 
    'edgeLabelBackground': 'white'
}}}%%


flowchart LR
 
    Groups(Groups) --> Users(Users)

    Users --  <font size=1>may have -->AK/SK(AK / SK)

    STS(STS) --  <font size=1>generates --> AK/SK

    Roles(Roles) --  <font size=1>assumed --> Users
    Roles -- <font size=1>assigned --> Lambda
    Roles -- <font size=1>assigned --> EC2
    Roles -- <font size=1>assigned --> ...

    PermPolicy(Permission policy) --  <font size=1>attached ---> Groups
    PermPolicy -- <font size=1>attached --> Users
    PermPolicy -- <font size=1>attached --> Roles

    PermBound(Permission boundary) -- <font size=1>attached ---> Users
    PermBound(Permission boundary) -- <font size=1>attached ---> Roles

    linkStyle default opacity:0.35,stroke:#DF7861,stroke-width:1px,color:#555

    classDef default stroke-width:1px,font-size:15px

    classDef service fill:#FCF9BE,stroke:#DCD99E
    class STS service

    classDef authorizations fill:#E8F3D6,stroke:#C8D3B6
    class PermPolicy,PermBound authorizations

    classDef identity fill:#FAAB78,color:white,stroke:#DA8B58
    class Users,Roles identity;

    classDef auxiliary opacity:0.7;
    class Lambda,EC2,... auxiliary