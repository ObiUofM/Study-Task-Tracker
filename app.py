import sqlite3

from flask import Flask, redirect, render_template_string, request, url_for

app = Flask(__name__)
DATABASE = "tasks.db"


def initialize_database():
    connection = sqlite3.connect(DATABASE)
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
        """
    )
    connection.close()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if title:
            connection = sqlite3.connect(DATABASE)
            connection.execute(
                "INSERT INTO tasks (title) VALUES (?)",
                (title,),
            )
            connection.commit()
            connection.close()

        return redirect(url_for("home"))

    connection = sqlite3.connect(DATABASE)
    tasks = connection.execute(
        "SELECT id, title FROM tasks ORDER BY id DESC"
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
                <label for="title">New task:</label>
                <input
                    id="title"
                    name="title"
                    type="text"
                    required
                    placeholder="Example: Finish math homework"
                >
                <button type="submit">Add Task</button>
            </form>

            <h2>Tasks</h2>

            {% if tasks %}
                <ul>
                    {% for task in tasks %}
                        <li>{{ task[1] }}</li>
                    {% endfor %}
                </ul>
            {% else %}
                <p>No tasks added yet.</p>
            {% endif %}
        </body>
        </html>
        """,
        tasks=tasks,
    )


initialize_database()