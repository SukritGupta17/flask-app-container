import os

from flask import Flask
import sqlalchemy
import logging

from connector_connect import connect_with_connector

app = Flask(__name__)
logger = logging.getLogger()


def init_connection_pool() -> sqlalchemy.engine.base.Engine:

    # use the connector when INSTANCE_CONNECTION_NAME is defined
    if os.environ.get("INSTANCE_CONNECTION_NAME"):
        logger.info("connecting using python connector")
        return connect_with_connector()
    logger.info("failed to connect")
    raise ValueError(
        "Missing database connection type. Please define INSTANCE_CONNECTION_NAME"
    )


@app.before_first_request
def init_db() -> sqlalchemy.engine.base.Engine:
    global db
    db = init_connection_pool()


@app.route("/home")
def home():
    with db.connect() as conn:
        # Execute the query and fetch all results
        all_planets = conn.execute(
            "SELECT * FROM planets"
        ).fetchall()
    logger.info(f"all planets fetched {all_planets}")
    return f"""<p>Hello, World!</p>
               <p>Welcome home.</p>
               <p>Planet db data: {all_planets}</p>"""


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
