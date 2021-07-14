import click
class CNN:
    def __init__(self, **params):
        click.secho("\nInitializing CNN: ", fg="green")
        for k, v in params.items():
            click.secho(str(k)+" : "+str(v)+"\t"+str(type(v)), fg="green")
        click.secho("="*80, fg="green")
