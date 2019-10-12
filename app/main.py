import click
from python_project import run_it

@click.group()
def cli():
  pass

@cli.command('printit')
@click.argument('text')
@click.option('--silent')
def printit(text: str, silent=False):
  run_it(text, silent)

if __name__ == '__main__':
  cli()