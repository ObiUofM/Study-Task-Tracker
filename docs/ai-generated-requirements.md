\# AI-Generated Requirements



\## Prompt Given to AI



Elicit requirements for a Study Task Tracker web application. The app is intended to help students organize assignments. Provide user stories, acceptance criteria, and non-functional requirements.



\## AI Response



\### User Story 1: Create an Account



As a student, I want to create an account so that my assignments are private.



Acceptance criteria:



\- The user can register with an email and password.

\- Duplicate email addresses are rejected.

\- Passwords must contain at least eight characters.

\- The user can sign in and sign out.



\### User Story 2: Add an Assignment



As a student, I want to add an assignment so that I can remember upcoming work.



Acceptance criteria:



\- The user can enter a title, course, due date, and priority.

\- The title and due date are required.

\- A valid assignment appears in the task list.

\- Invalid information produces an error message.



\### User Story 3: Update an Assignment



As a student, I want to edit an assignment so that I can correct changed information.



Acceptance criteria:



\- The user can edit an existing assignment.

\- The form displays the current assignment information.

\- Saved changes remain after refreshing the page.



\### User Story 4: Complete an Assignment



As a student, I want to mark assignments complete so that I can monitor my progress.



Acceptance criteria:



\- The user can change a task from incomplete to complete.

\- Completed tasks have a visible completed label.

\- The completed status is saved in the database.



\### User Story 5: Delete an Assignment



As a student, I want to delete an assignment that I no longer need.



Acceptance criteria:



\- The user is asked to confirm the deletion.

\- Confirming removes the assignment.

\- Canceling leaves the assignment unchanged.



\### User Story 6: Receive Reminders



As a student, I want to receive reminders so that I do not miss deadlines.



Acceptance criteria:



\- The user can enable email reminders.

\- A reminder is sent 24 hours before the due date.

\- No reminder is sent for completed assignments.



\### User Story 7: Search and Filter



As a student, I want to search and filter assignments so that I can find important tasks quickly.



Acceptance criteria:



\- The user can search by assignment title.

\- The user can filter by course, priority, and completion status.

\- Clearing the filters displays every assignment.



\## Non-Functional Requirements



1\. Pages shall load within two seconds under normal use.

2\. Passwords shall be stored using a secure one-way password hash.

3\. The application shall maintain 99.5% monthly availability.

4\. The interface shall support current desktop and mobile browsers.

