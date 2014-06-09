# ccgutils

This package contains utility modules for things related to collectable and
living card games (Magic: The Gathering and Android: Netrunner). It currently
contains the following modules:

## anr

Modules for Android: Netrunner

### parser

This module contains utilities for parsing and converting file formats. It can
be imported or run from the command line. For example, you can output a .o8d
file from OCTGN/cardgamedb in a form that can be pasted into a text file that
LackeyCC can import:

```python parser.py -tolackey /path/to/some/octgn/deck.o8d```

## mtg

Modules for Magic: The Gathering

### parser

This module contains utilities for parsing and converting file formats. It can
be imported or run from the command line. For example, you can output a .dek
file from LackeyCCG in a form that can be pasted into the deck editor on
deckstats.net:

```python parser.py -todeckstats /path/to/some/lackey/deck.dek```

## lackey

This module contains methods for getting cards from Lackey plugin databases and
deck formats

## octgn

This module contains methods for getting cards from OCTGN deck formats.

# Creation Info

## Donations
http://adammechtley.com/donations/

## License
The MIT License

Copyright (c) 2014 Adam Mechtley (http://adammechtley.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the 'Software'), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.