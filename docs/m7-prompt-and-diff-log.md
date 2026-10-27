\# M7 Prompt-and-Diff Log



\## Prompt



Help me refactor the Study Task Tracker without changing its behavior. Use the existing M6 tests before and after the refactor.



\## Identified code smell



The Flask `add\_task(title, due\_date) and tasks = get\_tasks()` route had mixed responsibilities. It handled HTTP requests, form validation, SQLite connections, SQL commands, and page rendering.



\## AI-suggested refactor



Extract the database operations into these functions:



```python

def add\_task(title, due\_date):

