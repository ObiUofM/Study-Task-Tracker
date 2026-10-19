import sqlite3
from datetime import date, datetime

from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
DATABASE = "tasks.db"


def deadline_notification(due_date):
    if not due_date:
        return "⚪ No deadline"

    deadline = datetime.strptime(due_date, "%Y-%m-%d").date()
    days_left = (deadline - date.today()).days

    if days_left < 0:
        return "🔴 Overdue"
    elif days_left == 0:
        return "🔴 Due today!"
    elif days_left == 1:
        return "🟠 Due tomorrow!"
    elif days_left <= 7:
        return f"🟡 Due in {days_left} days"
    else:
        return f"🟢 Due in {days_left} days"

def initialize_database():
    connection = sqlite3.connect(DATABASE)

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            due_date TEXT
        )
        """
    )

    columns = connection.execute(
        "PRAGMA table_info(tasks)"
    ).fetchall()

    column_names = [column[1] for column in columns]

    if "due_date" not in column_names:
        connection.execute(
            "ALTER TABLE tasks ADD COLUMN due_date TEXT"
        )

    connection.commit()
    connection.close()
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        due_date = request.form.get("due_date", "").strip()

        if title and due_date:
            connection = sqlite3.connect(DATABASE)
            connection.execute(
                "INSERT INTO tasks (title, due_date) VALUES (?, ?)",
                (title, due_date),
            )
            connection.commit()
            connection.close()

        return redirect(url_for("home"))

    connection = sqlite3.connect(DATABASE)
    tasks = connection.execute(
        """
        SELECT id, title, due_date
        FROM tasks
        ORDER BY due_date ASC
        """
    ).fetchall()
    connection.close()

    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Study Task Tracker</title>
        </head>

        <body>
            <h1>Study Task Tracker</h1>
            <p>Organize your assignments and stay on schedule.</p>

            <form method="POST">
                <label for="title">Task or test:</label>

                <input
                    id="title"
                    name="title"
                    type="text"
                    required
                    placeholder="Example: Software Engineering test"
                >

                <label for="due_date">Deadline:</label>

                <input
                    id="due_date"
                    name="due_date"
                    type="date"
                    required
                >

                <button type="submit">Add Task</button>
            </form>

            <h2>Upcoming Tasks</h2>

            {% if tasks %}
                <ul>
                    {% for task in tasks %}
                        <li>
                            <strong>{{ task[1] }}</strong>
                            — Deadline: {{ task[2] }}
                            — {{ deadline_notification(task[2]) }}
                        </li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No tasks added yet.</p>
            {% endif %}
        </body>
        </html>
        """,
        tasks=tasks,
        deadline_notification=deadline_notification,
    )


initialize_database()