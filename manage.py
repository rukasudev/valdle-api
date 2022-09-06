from flask_sslify import SSLify

import os
import unittest

from flask_script import Manager
from flask import redirect
from app import blueprint
from app.main import create_app, db

app = create_app(os.getenv("APPLICATION_ENV") or "dev")
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@app.route("/")
def main():
    return redirect("/docs", code=308)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover("app/test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    if "DYNO" in os.environ:  # only trigger SSLify if the app is running on Heroku
        sslify = SSLify(app)

    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
