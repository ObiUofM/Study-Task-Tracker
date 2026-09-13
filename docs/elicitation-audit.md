\# AI Elicitation Audit Log



\## Project



Study Task Tracker



\## Audit Purpose



This audit compares my original requirements in `requirements.md` with the separately generated requirements in `ai-generated-requirements.md`. The goal is to evaluate the AI response instead of automatically accepting it.



\## What the AI Missed



\### 1. Empty Task List Behavior



The AI did not explain what the application should display when no assignments exist. My requirements specify that the application must display a message when the task list is empty. Without this condition, a blank page could confuse the user or appear broken.



\### 2. Overdue Assignment Identification



The AI did not include a requirement for labeling overdue assignments. This is important because the main purpose of the application is helping students recognize work that needs immediate attention.



\### 3. Specific Persistence Conditions



The AI stated that some changes should remain after refreshing the page, but it did not fully define persistence. My requirements specify that assignments and their statuses must survive application restarts, not just page refreshes.



\### 4. Filter State Definitions



The AI suggested filtering but did not clearly define the exact behavior of the All, Incomplete, and Completed filters. Clearly defined filter states make the requirement easier to test.



\### 5. Protection Against Removing the Wrong Task



The AI said a task should be removed after confirmation, but it did not explicitly require that deleting one assignment must not affect any other assignment. This is an important data-integrity condition.



\### 6. Testable Performance Conditions



The AI said pages should load within two seconds “under normal use.” The phrase “normal use” is unclear and cannot be tested consistently. My requirement provides a specific condition: loading within two seconds with up to 500 assignments on the development computer.



\## What the AI Invented



\### 1. User Accounts



The original concept did not include accounts, passwords, sign-in, or private user data. The first version is intended to be a simple, single-user application. Adding authentication would increase the project’s difficulty without supporting the current milestone.



\### 2. Email Reminders



The AI invented automated email reminders. I did not request email integration, and it would require an email provider, account configuration, credentials, background scheduling, and additional security work.



\### 3. Assignment Priority



The AI added priority levels even though the original concept only included a title, course, due date, and completion status. Priority could be added later, but it is not required for the first version.



\### 4. 99.5 Percent Availability



The AI invented a monthly availability target. The project is currently a locally operated student application and will not initially run as a continuously available production service. Therefore, this requirement does not match the project’s intended scale.



\### 5. Mobile Browser Support



The AI included mobile-browser support without being asked. Responsive mobile support may be useful later, but the first version is only required to work in current desktop versions of Chrome and Edge.



\## What the AI Got Right That I Had Not Fully Considered



\### 1. Delete Confirmation



The AI required confirmation before deleting an assignment and specified that canceling must leave the assignment unchanged. This is useful because it prevents accidental deletion. I would add this condition to a future revision of my deletion story.



\### 2. Search by Assignment Title



The AI suggested searching by assignment title. My original requirements included status filters but not a text search. Search would become useful when a student has many assignments, so I would consider it for a later version.



\### 3. Clear Validation Feedback



The AI specified that invalid information should produce an error message. My requirements reject blank titles but do not explicitly state that the user must be told why the task was rejected. A visible validation message would improve usability.



\### 4. Clear Filters



The AI suggested filtering by course in addition to completion status. This could help students focus on work from one class and may be valuable after the basic status filter is implemented.



\## Final Decisions



\### Accepted



\- Add confirmation before permanent deletion.

\- Display a clear error message when required information is missing.

\- Consider title search and course filtering for a later version.



\### Rejected for the First Version



\- User accounts and passwords.

\- Email reminders.

\- Assignment priority.

\- A 99.5 percent availability requirement.

\- Required mobile-browser support.



\## Conclusion



The AI response identified useful ideas, especially deletion confirmation, validation feedback, and search. However, it also expanded the project beyond its intended beginner-level scope by adding accounts, email reminders, and production availability. It missed several specific edge cases and used unclear language in its performance requirement. The response was useful as a source of suggestions, but it required human review before any requirements could be accepted.

