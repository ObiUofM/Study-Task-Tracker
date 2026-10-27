\# M7 Refactor Note



\## Code smell



The `home()` route had mixed responsibilities. It handled HTTP form input, opened and closed database connections, executed SQL statements, retrieved tasks, and rendered the HTML response. This made the route longer and harder to understand.



\## Refactoring performed



I extracted the database operations into two functions:



\- `add\_task(title, due\_date)` saves a task to SQLite.

\- `get\_tasks()` retrieves tasks from SQLite in deadline order.



The `home()` route now handles only the web request, calls the appropriate database function, and renders or redirects the response.



\## What is now easier



Database behavior is now located in clearly named functions. Future changes to task storage can be made without searching through the Flask route. The route is shorter, easier to read, and has fewer responsibilities.



\## Behavior-preservation evidence



I ran the same unchanged pytest suite before and after the refactor. All tests passed in both runs, demonstrating that task creation, SQLite persistence, deadline notifications, and page rendering still behave the same.

