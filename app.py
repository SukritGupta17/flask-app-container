import os

from flask import Flask
import sqlalchemy

from connect_connector import connect_with_connector

app = Flask(__name__)


def init_connection_pool() -> sqlalchemy.engine.base.Engine:

    # use the connector when INSTANCE_CONNECTION_NAME is defined
    if os.environ.get("INSTANCE_CONNECTION_NAME"):
        return connect_with_connector()

    raise ValueError(
        "Missing database connection type. Please define INSTANCE_CONNECTION_NAME"
    )


@app.route("/home")
def home():
    db = init_connection_pool()
    with db.connect() as conn:
        # Execute the query and fetch all results
        all_planets = conn.execute(
            "SELECT * FROM planets"
        ).fetchall()
    return "<p>Hello, World!</p> \n Welcome home. \n"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
