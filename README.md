zendesk-xml-bsplit
==================

zendesk-xml-bsplit is a command-line script that splits an XML file exported from Zendesk into smaller files that don't exceed a certain size in bytes.
It's written in Python 3 and is not currently backward compatible with Python 2.7.

Installation
------------

zendesk-xml-bsplit is not currently available on the Python Package Index. It can be installed with:

    $ git clone https://github.com/simonrichard/zendesk-xml-bsplit.git
    $ cd zendesk-xml-bsplit
    $ python setup.py install

Example usage
-------------

    $ zendesk-xml-bsplit --outfile=tickets_{}.xml --limit=1e+8 tickets.xml
    $ zendesk-xml-bsplit --outfile=tickets_{}.xml --limit=100MB tickets.xml

This example splits `tickets.csv` into files that don't exceed 1e+8 bytes or 100 megabytes.
These files are named by inserting a number in the replacement field in curly braces (`{}`).
The two examples are equivalent.
