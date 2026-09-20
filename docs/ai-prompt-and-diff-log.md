\# AI Prompt-and-Diff Log



\## Milestone One



\### AI Tool Used



ChatGPT/Codex



\### Prompt



"Stand up the solo repository and prove your toolchain works."



I asked the AI to guide me through creating the project manually, one step at a time.



\### AI Response



The AI helped me install and verify Git, create a Python virtual environment, install Flask and pytest, create the application, write an automated test, and prepare the repository.



\### Changes Accepted



\- Created app.py

\- Created requirements.txt

\- Created README.md

\- Created .gitignore

\- Created tests/test\_app.py

\- Added a working Flask home page

\- Added an automated pytest test



\### Test Result



The automated test passed successfully:



1 passed in 0.33s



\### Human Review



I manually entered the commands, created the files, reviewed the code, ran the application, and confirmed that the automated test passed.


\## Milestone Two: Requirements and AI Audit



\### Prompt



"Write requirements for a Study Task Tracker application, including user stories, acceptance criteria, and non-functional requirements."



\### AI-Generated Changes



The AI suggested requirements involving assignment management, user accounts, email reminders, priorities, searching, filtering, authentication security, mobile support, and availability.



\### Changes Accepted



\- Delete confirmation

\- Clear validation error messages

\- Title search as a possible future feature

\- Course filtering as a possible future feature



\### Changes Rejected



\- User accounts and passwords

\- Email reminders

\- Assignment priorities for the first version

\- 99.5 percent monthly availability

\- Required mobile-browser support



\### Reason for Differences



The rejected features increased the project beyond its intended beginner-level scope. The accepted ideas improved usability without changing the main purpose of the application.



\### Files Added or Updated



\- Added `docs/requirements.md`

\- Added `docs/ai-generated-requirements.md`

\- Added `docs/elicitation-audit.md`

\- Updated `docs/ai-prompt-and-diff-log.md`
## Milestone Three: Domain Model and AI Critique

### Prompt

"Using the Milestone 2 requirements for the Study Task Tracker, draft a domain model. Include the main entities, their attributes, and relationships. Do not implement the application."

### AI-Generated Model

The AI created the following entities:

- User
- User Settings
- Course
- Assignment
- Reminder
- Tag
- Audit Log

### Changes Accepted

- Assignment as the central entity
- Assignment ID
- Title
- Course information
- Due date
- Completion status

### Changes Rejected

- User accounts and passwords
- User settings
- Audit logs
- Email reminders
- Tags
- Separate Course entity
- Priority field
- Created and updated timestamps

### Changes Made

- Reduced the model to Assignment and AssignmentStatus.
- Kept course as an Assignment attribute.
- Restricted status to INCOMPLETE or COMPLETED.
- Added mark_complete and update behavior.
- Added derived overdue behavior.
- Preserved the AI’s original draft without editing it.

### Files Added

- `docs/m3-ai-domain-model-first-draft.md`
- `docs/m3-domain-model.mmd`
- `docs/m3-domain-model.png`
- `docs/m3-domain-model-critique.md`
