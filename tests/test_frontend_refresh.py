from pathlib import Path


def test_signup_flow_refreshes_activities_after_success():
    app_js = Path("src/static/app.js").read_text()

    assert "activitySelect.innerHTML = '<option value=\"\">-- Select an activity --</option>';" in app_js
    assert "await fetchActivities();" in app_js
