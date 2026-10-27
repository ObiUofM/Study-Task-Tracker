\# M6 Prompt-and-Diff Log



\## AI prompt



Add deadline notifications to the Study Task Tracker and help write acceptance tests, unit tests, a coverage report, and a bug-injection demonstration.



\## Changes produced with AI assistance



\- Added a `due\_date` field to the SQLite tasks table.

\- Added a date input to the task form.

\- Added deadline notification logic for overdue, due today, due tomorrow, due within seven days, and later deadlines.

\- Updated the application to save and display task deadlines.

\- Added an acceptance test for submitting and displaying a task with a deadline.

\- Added unit tests for each deadline-notification condition.

\- Added test isolation using a temporary SQLite database.

\- Added coverage configuration through `pytest-cov`.



\## Human review and edits



I entered the code manually, ran the test suite, reviewed failures, and updated an older acceptance test so it included the newly required deadline.



\## Intentional fault



The correct condition was:



```python

elif days\_left == 1:

