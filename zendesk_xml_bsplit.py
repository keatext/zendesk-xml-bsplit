#!/usr/bin/python3
import argparse

from io import BytesIO
from xml.etree import ElementTree as ET


def read(infile):
    with open(infile, "rb") as f:
        yield next(f) + next(f)

    for event, elem in ET.iterparse(infile, ("end",)):
        if event == "end" and elem.tag == "ticket":
            yield ET.tostring(elem)


def file(outfile, head, i):
    f = open(outfile.format(i), "wb")
    f.write(head)
    return f


def write(tickets, outfile, limit):
    head = next(tickets)
    i = 1
    f = file(outfile, head, i)

    for ticket in tickets:
        with BytesIO() as mock:
            mock.write(ticket)
            size = len(mock.getvalue())
        if f.tell() + size > limit:
            f.write(b"</tickets>")
            f.close()
            i += 1
            f = file(outfile, head, i)
        f.write(ticket)

    f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--outfile", required=True, help="Template for the output filename")
    parser.add_argument("-l", "--limit", required=True, help="Size limit in bytes (1e+8) or a human-friendly format (100MB)")
    parser.add_argument("infile", help="Path to the XML file exported from Zendesk")

    args = parser.parse_args()
    try:
        limit = float(args.limit)
    except ValueError:
        import humanfriendly as hf
        limit = hf.parse_size(args.limit)
    tickets = read(args.infile)
    write(tickets, args.outfile, limit)


if __name__ == "__main__":
    main()
