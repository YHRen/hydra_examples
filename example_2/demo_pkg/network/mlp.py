import click
class MLP:
    def __init__(self, **params):
        click.secho("\nInitializing "+self.__class__.__qualname__+": ", fg="green")
        for k, v in params.items():
            click.secho(str(k)+" : "+str(v)+"\t"+str(type(v)), fg="green")
        click.secho("="*80, fg="green")
    # def __init__(self, input_dim, hidden_dims, output_dim):
    #     self.idim = input_dim
    #     self.hdim = hidden_dims
    #     self.odim = output_dim
