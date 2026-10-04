import sqlite3

import app as app_module


def test_home_page():
    client = app_module.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Study Task Tracker" in response.data


def test_add_task_end_to_end(tmp_path, monkeypatch):
    test_database = tmp_path / "test_tasks.db"

    monkeypatch.setattr(
        app_module,
        "DATABASE",
        str(test_database),
    )

    app_module.initialize_database()
    client = app_module.app.test_client()

    response = client.post(
        "/",
        data={"title": "Finish Digital Design homework"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Finish Digital Design homework" in response.data

    connection = sqlite3.connect(test_database)
    saved_task = connection.execute(
        "SELECT title FROM tasks"
    ).fetchone()
    connection.close()

    assert saved_task[0] == "Finish Digital Design homework"