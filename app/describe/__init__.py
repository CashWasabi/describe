from typing import Any

from describe.word.models import db_session
from describe.word.schema import schema
from flask import Flask
from flask_graphql import GraphQLView


app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # for having the GraphiQL interface
    )
)


@app.teardown_appcontext
def shutdown_session(exception: Any = None) -> None:
    db_session.remove()
