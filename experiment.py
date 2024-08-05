import click


@click.command()

@click.option("--avatar")
@click.option("--command")

def main(avatar, command, **config_kwargs):
    """
    Lets test this
    :param avatar:
    :param command:
    :param config_kwargs:
    :return:
    """



if __name__ == '__main__':
    main()