#!/usr/bin/python

"""
This module contains methods for parsing and translating different card and deck
formats.
"""

import collections
import csv
import os
import sys
import xml.etree.ElementTree as et

LACKEY_CARD_DATA_FOLDER = 'sets'
LACKEY_CARD_DATA_MANIFEST_FILE = 'ListOfCardDataFiles.txt'
TO_DECKSTATS_FLAG = '-todeckstats'
TO_LACKEY_FLAG ='-tolackey'


def get_lackey_card_database(
        path_to_plugin='/Applications/LackeyCCG/plugins/magic'
):
    """
    Loads all of the card data into a list of named tuples.
    @param path_to_plugin: Path to the Lackey Magic plugin on disk.
    @return: A list of named tuples with data for all of the cards.
    """
    with open(os.path.join(path_to_plugin, LACKEY_CARD_DATA_MANIFEST_FILE)) as f:
        document = et.parse(f).getroot()
    data_entries = list()
    for tag in document.findall('filetoinclude'):
        path_to_data_file = \
            os.path.join(path_to_plugin, LACKEY_CARD_DATA_FOLDER, tag.text)
        with open(path_to_data_file) as f:
            reader = csv.DictReader(f, delimiter='\t')
            field_names = reader.fieldnames
            data_entries += [row for row in reader]
    card = collections.namedtuple('Card', field_names)
    return [card(**e) for e in data_entries]


def get_cards_in_lackey_deck(path_to_deck):
    """
    Gets a dict containing a deck dict and sideboard dict, each with counts of
        cards keyed by card name.
    @return: A dict in the form {'Sideboard': {'Card': 1}, 'Deck': {'Card': 1}}.
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

# process command-line arguments if running as __main__
if __name__ == '__main__':
    try:
        path_to_dek = sys.argv[sys.argv.index(TO_DECKSTATS_FLAG) + 1]
    except ValueError:
        path_to_dek = None
    if path_to_dek is not None:
        deck = get_cards_in_lackey_deck(sys.argv[-1])
        for card, count in deck['Deck'].iteritems():
            sys.stdout.write('{0} {1}\n'.format(count, card))
        sys.stdout.write('//Sideboard\n')
        for card, count in deck['Sideboard'].iteritems():
            sys.stdout.write('{0} {1}\n'.format(count, card))
    else:
        sys.stdout.write(
            'usage: python {0} [{1} /path/to.dek]\n'.format(
                __file__, TO_DECKSTATS_FLAG
            )
        )