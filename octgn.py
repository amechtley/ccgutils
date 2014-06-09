"""
This module contains methods for working with OCTGN file formats.
"""

import xml.etree.ElementTree as et


def get_cards_in_deck(path_to_deck):
    """
    Gets a dict containing a dict for each superzone, each with counts of cards
        keyed by card name.
    @return: A dict in the form {'Zone1': {'Card': 1}, 'Zone2': {'Card': 1}}.
    @param path_to_deck: Path to a Octgn .o8d file.
    """
    with open(path_to_deck) as f:
        document = et.parse(f).getroot()
    deck = dict()
    for superzone in document.findall('section'):
        z_name = superzone.attrib['name']
        deck[z_name] = dict()
        for entry in superzone.iter('card'):
            card_name = entry.text
            deck[z_name][card_name] = \
                deck[z_name].setdefault(card_name, 0) + int(entry.attrib['qty'])
    return deck