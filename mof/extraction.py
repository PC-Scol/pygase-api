#!/usr/bin/env python3

import click
from mof import mof_client
from mof_client.api.extractions_api import ExtractionsApi


__client = ExtractionsApi(mof_client())


@click.group()
def extractions():
    pass


@click.command()
@click.argument('etablissement')
@click.argument('periode')
def arbres_pour_une_periode(etablissement, periode):
    global __client
    arbres = __client.extraire_arbres_pour_une_periode(
        etablissement, periode,
        _check_return_type=False
    )
    click.echo(arbres)


extractions.add_command(arbres_pour_une_periode)

