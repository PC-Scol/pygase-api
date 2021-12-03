#!/usr/bin/env python3
import click
from ref import ref_client
from ref_client.api.structure_api import StructureApi


__client = StructureApi(ref_client())


@click.group()
def structure():
    pass


@click.command()
@click.argument('etablissement')
def lire(etablissement):
    global __client
    structure = __client.lire_structure(
        etablissement,
        _check_return_type=False
    )
    click.echo(structure)


@click.command()
def liste():
    global __client
    structures = __client.lire_liste_structures(_check_return_type=False)
    click.echo(structures)


structure.add_command(lire)
structure.add_command(liste)
