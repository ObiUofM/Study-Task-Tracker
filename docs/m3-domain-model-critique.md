\# Domain Model Critique



\## Project



Study Task Tracker



\## Models Compared



\- AI first draft: `m3-ai-domain-model-first-draft.md`

\- Final domain model source: `m3-domain-model.mmd`

\- Final diagram image: `m3-domain-model.png`



\## Summary



The AI produced a detailed domain model, but much of it exceeded the accepted scope of the Study Task Tracker. My final model keeps Assignment as the central entity and adds only the status values and behaviors required by the Milestone 2 requirements.



\## Where the AI Over-Modelled



\### User



The AI added a User entity with an email address and password hash. The accepted requirements describe a single-user application and specifically reject accounts and authentication for the first version. User does not belong in the current domain model.



\### User Settings



The AI created User Settings for email notifications and themes. Neither feature appears in the accepted requirements. Adding this entity would create additional forms, storage, validation, and tests without supporting the first release.



\### Audit Log



The AI added an Audit Log to record user actions. The application does not require regulatory auditing, activity history, or multiple users. This entity adds complexity without solving a stated problem.



\### Reminder



The AI added Reminder and connected it to Assignment. Email reminders appeared only in the AI-generated requirements and were rejected during the Milestone 2 audit. The application does not currently need scheduled background processes or email delivery.



\### Tag



The AI added a many-to-many relationship between Assignment and Tag. The accepted requirements include status filtering but do not require user-created tags. This relationship would also require an additional junction table that the AI did not show.



\### Separate Course Entity



The AI created Course as a separate entity with instructor and semester fields. The accepted requirements only require a course name to appear with each assignment. A course string inside Assignment is enough for the first version.



\## Where the AI Under-Modelled



\### Assignment Behavior



The AI treated Assignment mostly as stored data. It did not show behaviors such as:



\- Marking an assignment complete

\- Updating assignment information

\- Determining whether an assignment is overdue



These behaviors represent important domain rules and appear in my class diagram.



\### Controlled Status Values



The AI stored status as an unrestricted string. This would allow invalid values such as “finished,” “closed,” or misspelled text. My model uses AssignmentStatus with only INCOMPLETE and COMPLETED.



\### Derived Overdue Status



The AI did not explain how overdue status is determined. My model calculates it from the due date, current date, and completion status. Overdue should not be stored because it can change when time passes or when the assignment is completed.



\### Required Title Rule



The AI did not represent the requirement that an assignment title cannot be blank. This rule should be enforced when an Assignment is created or updated.



\## Relationships the AI Guessed Without Support



\### User Creates Course



The AI assumed that a User creates and owns multiple courses. The requirements contain no user accounts or course-management workflow, so there is no basis for this relationship.



\### Course Contains Assignments



Although grouping assignments by course is reasonable, the requirements only treat course as information entered on an assignment. They do not require a separate Course object or a one-to-many database relationship.



\### Assignment Schedules Reminders



The AI assumed every assignment could schedule reminders even though reminder functionality was rejected from the first version.



\### Assignment Categorized by Tags



The AI invented a many-to-many tagging relationship. No user story requires creating, assigning, deleting, or filtering by tags.



\## What the AI Got Right



\### Assignment as the Central Entity



The AI correctly identified Assignment as the main object in the application.



\### Core Assignment Attributes



It correctly included an identifier, title, due date, and status. These fields are supported by the accepted requirements.



\### Course Information



The AI correctly recognized that assignments need course information. I kept that information as an attribute instead of creating a separate entity.



\### Persistent Identifier



Including an Assignment ID was correct because editing, completing, and deleting must affect the selected assignment without changing other assignments.



\## Why My Model Is Smaller



My final model contains one main domain class and one status enumeration. This matches the current single-user scope and supports the required assignment operations without preparing for features that may never be built.



A smaller model reduces:



\- Database tables

\- Relationships and foreign keys

\- Validation rules

\- User-interface screens

\- Testing requirements

\- Migration work during the first release



The model can expand later if accounts, course management, reminders, or tagging become accepted requirements.



\## Final Assessment



The AI draft was useful because it identified Assignment and several correct attributes. However, it designed for a larger multi-user productivity platform instead of the accepted beginner-level application. Its main failure was over-modelling hypothetical future features. My final model stays traceable to the requirements and gives Assignment the behaviors needed to enforce the application’s actual rules.

