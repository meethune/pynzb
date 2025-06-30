# pynzb

## Introduction

NZB is an XML-based file format for retrieving posts from NNTP (Usenet) servers.
Since NZB is XML-based, it's relatively easy to build one-off parsers to parse
NZB files. This project is an attempt to consolidate those many one-off NZB
parsers into one simple interface.

This package includes three implementations: one based on expat, another based
on ElementTree, and a final implementation based on lxml. The fastest available
parser is automatically selected at import time.

## Installation

Basic installation:

```bash
pip install pynzb
```

For better performance with large NZB files, install with lxml support:

```bash
pip install pynzb[lxml]
```

The library will automatically use lxml when available, but falls back to the
built-in ElementTree parser if lxml is not installed.

## Quick Start

```python
from pynzb import nzb_parser

# Parse an NZB file
with open('my_file.nzb', 'r') as f:
    nzb_content = f.read()

files = nzb_parser.parse(nzb_content)

# Access file information
for nzb_file in files:
    print(f"Subject: {nzb_file.subject}")
    print(f"Size: {sum(segment.bytes for segment in nzb_file.segments)} bytes")
```

## Example Usage

For a complete working example that demonstrates parsing an NZB file and displaying file information, see [`example.py`](example.py).

Run it with:
```bash
python example.py path/to/your/file.nzb
```

## API Documentation

### Accessing the Default Parser

Simply import `nzb_parser` from the pynzb package. It's an instantiated version
of the fastest available parser that your system can support.

### Other Parser Locations

- **`ExpatNZBParser`**: Available in the `pynzb.expat_nzb` namespace.
- **`ETreeNZBParser`**: Available in the `pynzb.etree_nzb` namespace.
- **`LXMLNZBParser`**: Available in the `pynzb.lxml_nzb` namespace (requires lxml).

### Using the NZB Parser

If you're using a specific parser, like the `ETreeNZBParser`, you will first
have to instantiate it:

```python
from pynzb.etree_nzb import ETreeNZBParser
nzb_parser = ETreeNZBParser()
```

Otherwise, you can just import the default parser for your system:

```python
from pynzb import nzb_parser
```

Then, simply call the `parse` method, giving it the NZB content as a string:

```python
files = nzb_parser.parse(nzb_content)
```

This will return a list of `NZBFile` objects for you to use.

### NZBFile Objects

All of the parsers return `NZBFile` objects, which have the following properties:

- **`poster`**: The name of the user who posted the file to the newsgroup.
- **`date`**: A `datetime.date` representation of when the server first saw the file.
- **`subject`**: The subject used when the user posted the file to the newsgroup.
- **`groups`**: A list of strings representing the newsgroups in which this file may be found.
- **`segments`**: A list of `NZBSegment` objects containing information about where to get the file contents.

### NZBSegment Objects

Each `NZBFile` has a list of `NZBSegment` objects, which contain information
about how to retrieve a part of a file. Each `NZBSegment` object has these properties:

- **`number`**: The number of the segment in the list of files.
- **`bytes`**: The size of the segment, in bytes.
- **`message_id`**: The Message-ID of the segment (useful for retrieving the full contents)
