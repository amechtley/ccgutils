"""
This module contains methods for working with LackeyCCG file formats.
"""

import collections
import csv
import os
import xml.etree.ElementTree as et

CARD_DATA_FOLDER = 'sets'
CARD_DATA_MANIFEST_FILE = 'ListOfCardDataFiles.txt'


def get_card_database(
        plugin_name,
        path_to_plugins='/Applications/LackeyCCG/plugins'
):
    """
    Loads all of the card data into a list of named tuples.
    @param plugin_name: Name of the directory for the plugin whose database
        should be retrieved.
    @param path_to_plugins: Path to the Lackey plugins on disk.
    @return: A list of named tuples with data for all of the cards.
    """
    path_to_plugin_manifest = os.path.join(
        path_to_plugins, plugin_name, CARD_DATA_MANIFEST_FILE
    )
    with open(path_to_plugin_manifest) as f:
        document = et.parse(f).getroot()
    data_entries = list()
    for tag in document.findall('filetoinclude'):
        path_to_data_file = os.path.join(
            path_to_plugins, plugin_name, CARD_DATA_FOLDER, tag.text
        )
        with open(path_to_data_file) as f:
            reader = csv.DictReader(f, delimiter='\t')
            field_names = reader.fieldnames
            data_entries += [row for row in reader]
    card = collections.namedtuple('Card', field_names)
    return [card(**e) for e in data_entries]


def get_cards_in_deck(path_to_deck):
    """
    Gets a dict containing a dict for each superzone, each with counts of cards
        keyed by card name.
    @return: A dict in the form {'Zone1': {'Card': 1}, 'Zone2': {'Card': 1}}.
    @param path_to_deck: Path to a Lackey .dek file.
    """
    with open(path_to_deck) as f:
        document = et.parse(f).getroot()
    deck = dict()
    for superzone in document.findall('superzone'):
        z_name = superzone.attrib['name']
        deck[z_name] = dict()
        for entry in superzone.iter('card'):
            card_name = entry.find('name').text
            deck[z_name][card_name] = deck[z_name].setdefault(card_name, 0) + 1
    return deck