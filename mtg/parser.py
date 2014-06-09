#!/usr/bin/python

"""
This module contains methods for parsing and translating different card and deck
formats from the command line.
"""

import sys
import ccgutils.lackey as lackey

TO_DECKSTATS_FLAG = '-todeckstats'


def get_deckstats_text_string(path_to_lackey_dek):
    """
    Gets a string representation of the data in the supplied Lackey deck file
        for output in the console or writing to a text file.
    @param path_to_lackey_dek: Path to a Magic: The Gathering .dek deck.
    """
    result = list()
    deck = lackey.get_cards_in_deck(path_to_lackey_dek)
    for card, count in deck['Deck'].iteritems():
        result.append('{0} {1}'.format(count, card))
    result.append('//Sideboard')
    for card, count in deck['Sideboard'].iteritems():
        result.append('{0} {1}'.format(count, card))
    return '\n'.join(result)

# process command-line arguments if running as __main__
if __name__ == '__main__':
    try:
        path_to_dek = sys.argv[1]
    except IndexError:
        path_to_dek = None
    if path_to_dek is not None:
        if TO_DECKSTATS_FLAG in sys.argv:
            deck_str = get_deckstats_text_string(path_to_dek)
            sys.stdout.write(deck_str + '\n')
    else:
        sys.stdout.write(
            'usage: python {0} /path/to.dek [{1}]\n'.format(
                __file__, TO_DECKSTATS_FLAG
            )
        )