import sqlite3
from datetime import date, timedelta

import pytest

import app as app_module


@pytest.fixture
def client(tmp_path, monkeypatch):
    test_database = tmp_path / "test_tasks.db"

    monkeypatch.setattr(
        app_module,
        "DATABASE",
        str(test_database),
    )

    app_module.initialize_database()
    app_module.app.config["TESTING"] = True

    with app_module.app.test_client() as test_client:
        yield test_client


def test_user_can_add_task_with_deadline(client):
    due_date = date.today() + timedelta(days=1)

    response = client.post(
        "/",
        data={
            "title": "Software Engineering test",
            "due_date": due_date.isoformat(),
        },
        follow_redirects=True,
    )

    page = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Software Engineering test" in page
    assert due_date.isoformat() in page
    assert "Due tomorrow!" in page

    connection = sqlite3.connect(app_module.DATABASE)
    saved_task = connection.execute(
        """
        SELECT title, due_date
        FROM tasks
        WHERE title = ?
        """,
        ("Software Engineering test",),
    ).fetchone()
    connection.close()

    assert saved_task == (
        "Software Engineering test",
        due_date.isoformat(),
    )


def test_no_deadline_notification():
    assert app_module.deadline_notification(None) == "⚪ No deadline"


def test_overdue_notification():
    due_date = date.today() - timedelta(days=1)

    assert (
        app_module.deadline_notification(due_date.isoformat())
        == "🔴 Overdue"
    )


def test_due_today_notification():
    assert (
        app_module.deadline_notification(date.today().isoformat())
        == "🔴 Due today!"
    )


def test_due_tomorrow_notification():
    due_date = date.today() + timedelta(days=1)

    assert (
        app_module.deadline_notification(due_date.isoformat())
        == "🟠 Due tomorrow!"
    )


def test_due_within_seven_days_notification():
    due_date = date.today() + timedelta(days=7)

    assert (
        app_module.deadline_notification(due_date.isoformat())
        == "🟡 Due in 7 days"
    )


def test_future_deadline_notification():
    due_date = date.today() + timedelta(days=10)

    assert (
        app_module.deadline_notification(due_date.isoformat())
        == "🟢 Due in 10 days"
    )