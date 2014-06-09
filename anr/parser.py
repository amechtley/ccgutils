#!/usr/bin/python

"""
This module contains methods for parsing and translating different card and deck
formats from the command line.
"""

import os
import re
import sys
import ccgutils.octgn as octgn

LACKEY_ID_DELIMITER = ','
OCTGN_ID_DELIMITER = ':'
OCTGN_NAMES_NO_PERIOD = frozenset(
    [
        'Joshua B',
        'Melange Mining Corp'
    ]
)
OUTPUT_FLAG = '-output'
TO_LACKEY_FLAG = '-tolackey'


def get_lackey_text_string(path_to_octgn_deck):
    """
    Gets a string representation of the data in the supplied OCTGN deck file for
        output in the console or writing to a text file.
    @param path_to_octgn_deck: Path to an Android: Netrunner .o8d deck.
    """
    deck = octgn.get_cards_in_deck(path_to_octgn_deck)
    result = list()
    for card, count in deck['R&D / Stack'].iteritems():
        result.append(
            '{0} {1}'.format(
                count,
                card if not card in OCTGN_NAMES_NO_PERIOD else card + '.'
            )
        )
    result.append('Identity:')
    for card, count in deck['Identity'].iteritems():
        result.append(
            '{0} {1}'.format(
                count,
                re.sub(OCTGN_ID_DELIMITER, LACKEY_ID_DELIMITER, card)
                if not card in OCTGN_NAMES_NO_PERIOD
                else re.sub(OCTGN_ID_DELIMITER, LACKEY_ID_DELIMITER, card) + '.'
            )
        )
    return '\n'.join(result)

# process command-line arguments if running as __main__
if __name__ == '__main__':
    try:
        path_to_o8d = sys.argv[1]
    except IndexError:
        path_to_o8d = None
    if path_to_o8d is not None:
        if TO_LACKEY_FLAG in sys.argv:
            deck_str = get_lackey_text_string(path_to_o8d)
            try:
                path_to_output = sys.argv[sys.argv.index(OUTPUT_FLAG) + 1]
                with open(path_to_output, 'w+') as f:
                    f.write(deck_str)
            except ValueError:
                sys.stdout.write(deck_str + '\n')
    else:
        sys.stdout.write(
            'usage: python {0} /input/path.o8d [{1} {2} /output/path.txt]\n'.format(
                __file__, TO_LACKEY_FLAG, OUTPUT_FLAG
            )
        )