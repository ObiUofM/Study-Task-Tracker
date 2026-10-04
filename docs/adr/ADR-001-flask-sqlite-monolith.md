\# ADR-001: Use a Server-Rendered Flask Application with SQLite



\- Status: Accepted

\- Date: 2026-09-28



\## Context



The Study Task Tracker needs to let one student create, view, edit, complete, and delete assignments. Each assignment includes a title, course name, due date, and completion status. The application also needs to preserve assignments after the application restarts.



The first version is being developed by one beginner developer within a limited academic schedule. The existing project already uses Python, Flask, pytest, pip, Git, and GitHub. The accepted requirements do not currently include multiple user accounts, shared task lists, mobile clients, email reminders, or large-scale deployment.



A major architectural decision was whether to keep the interface, application logic, and database access inside one Flask application or separate the frontend and backend into different applications.



\## Decision



The first version will use a server-rendered Flask monolith with SQLite.



Flask routes will receive browser requests, validate form data, call the application’s assignment logic, and render HTML through Jinja templates. SQLite will store assignments locally. The application will remain one Python project and one deployable process.



Logical boundaries will still separate:



\- Routes and request handling

\- Assignment rules

\- Database operations

\- HTML templates

\- Automated tests



The application will not initially use a JavaScript frontend framework or a separate REST API.



\## Alternatives Considered



\### React Frontend with a Flask REST API



This alternative would separate the user interface from the backend. React would manage browser state, while Flask would expose assignment data through JSON endpoints.



This could support a richer interface and make future mobile clients easier to add. However, it would require JavaScript and Node.js tooling, API design, client-side state management, cross-origin configuration, and separate frontend and backend testing.



\### Flask with PostgreSQL



PostgreSQL would support stronger concurrency and future multi-user deployment. It would also require installing, configuring, and maintaining a separate database server. Those costs are not justified for the current single-user scope.



\### Python Desktop Application



A desktop interface using Tkinter could work with local SQLite storage without a browser. However, it would require desktop packaging and would provide a less convenient path toward web deployment.



\## Consequences



\### Positive Consequences



\- The project uses one primary programming language.

\- The application can run as one process.

\- SQLite does not require a separate database server.

\- Flask’s test client can test complete requests using pytest.

\- Development and debugging remain manageable for one beginner developer.

\- Server-rendered forms reduce the amount of client-side state.

\- The application can deliver the accepted requirements with fewer dependencies.



\### Negative Consequences



\- The interface and server are more tightly coupled than they would be with a separate API.

\- Other clients cannot easily reuse the application logic over HTTP.

\- SQLite has limited support for many simultaneous write operations.

\- Horizontal scaling would require replacing or redesigning the database layer.

\- A future mobile application would likely require adding an API.

\- Moving to React later would require rebuilding much of the presentation layer.

\- Adding multiple users would require authentication, authorization, and a database migration.

\- Long-running features such as email reminders would require a background job system that the current architecture does not provide.



\### Doors This Decision Closes for the First Version



This decision rules out an independent JavaScript frontend, public API, native mobile client, large multi-user deployment, and distributed background processing in the first version.



These options remain possible later, but adopting them would require deliberate architectural changes rather than simple configuration.



\## Reconsideration Conditions



This decision should be reviewed if the accepted requirements add:



\- Multiple user accounts

\- Shared assignments

\- A mobile application

\- Public API access

\- High numbers of concurrent users

\- Scheduled email or push notifications

\- Deployment across multiple application servers

