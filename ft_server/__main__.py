import click
from flask import g
import fastText
from .server import app

@click.command()
@click.argument('model', type=click.Path(exists=True))
def cli(model):
    app.config["FT_SERVER_MODEL_PATH"] = model
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])

cli()