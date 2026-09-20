\# AI Domain Model: First Draft



\## Prompt Given to AI



Using the Milestone 2 requirements for the Study Task Tracker, draft a domain model. Include the main entities, their attributes, and relationships. Do not implement the application.



\## AI Response



```mermaid

erDiagram

&#x20;   USER ||--o{ COURSE : creates

&#x20;   USER ||--|| USER\_SETTINGS : has

&#x20;   USER ||--o{ AUDIT\_LOG : generates

&#x20;   COURSE ||--o{ ASSIGNMENT : contains

&#x20;   ASSIGNMENT ||--o{ REMINDER : schedules

&#x20;   ASSIGNMENT }o--o{ TAG : categorized\_by



&#x20;   USER {

&#x20;       int id PK

&#x20;       string email

&#x20;       string password\_hash

&#x20;       datetime created\_at

&#x20;   }



&#x20;   USER\_SETTINGS {

&#x20;       int id PK

&#x20;       int user\_id FK

&#x20;       boolean email\_notifications

&#x20;       string theme

&#x20;   }



&#x20;   COURSE {

&#x20;       int id PK

&#x20;       int user\_id FK

&#x20;       string name

&#x20;       string instructor

&#x20;       string semester

&#x20;   }



&#x20;   ASSIGNMENT {

&#x20;       int id PK

&#x20;       int course\_id FK

&#x20;       string title

&#x20;       text description

&#x20;       datetime due\_date

&#x20;       string priority

&#x20;       string status

&#x20;       datetime created\_at

&#x20;       datetime updated\_at

&#x20;   }



&#x20;   REMINDER {

&#x20;       int id PK

&#x20;       int assignment\_id FK

&#x20;       datetime reminder\_time

&#x20;       boolean sent

&#x20;   }



&#x20;   TAG {

&#x20;       int id PK

&#x20;       string name

&#x20;       string color

&#x20;   }



&#x20;   AUDIT\_LOG {

&#x20;       int id PK

&#x20;       int user\_id FK

&#x20;       string action

&#x20;       datetime timestamp

&#x20;   }

```



\## AI Explanation



The User entity owns courses and settings. Each Course contains assignments. Assignments may have reminders and multiple tags. The Audit Log records changes performed by users. This structure supports authentication, organization by course, reminders, customization, and future reporting.

