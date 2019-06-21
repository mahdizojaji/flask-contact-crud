import click


@click.group()
def cli():
    pass


@click.command('generate-db')
def generate_database():
    from models import db
    from models import Contact
    db.connect()
    db.create_tables([Contact])


cli.add_command(generate_database)

if __name__ == "__main__":
    cli()
