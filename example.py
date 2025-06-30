#!/usr/bin/env python

"""
A command-line tool to parse an NZB file and display its contents.

This example program demonstrates how to use the pynzb library to parse an
NZB file and extract information about the files it contains.
"""

import argparse
import os
from pynzb import nzb_parser

def format_size(size_in_bytes):
    """Converts a size in bytes to a human-readable string."""
    if size_in_bytes is None:
        return "0 B"
    # Define the units and iterate to find the correct one
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_in_bytes < 1024.0:
            break
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:3.2f} {unit}"

def main():
    """
    Parses command-line arguments and displays NZB file information.
    """
    parser = argparse.ArgumentParser(
        description="Parse an NZB file and display file and size information.",
        epilog="Example: python example.py my_ubuntu_download.nzb"
    )
    parser.add_argument("nzb_file", help="The path to the NZB file to parse.")
    args = parser.parse_args()

    file_path = args.nzb_file
    if not os.path.exists(file_path):
        print(f"Error: The file '{file_path}' was not found.")
        return

    print(f"Parsing '{os.path.basename(file_path)}'...")

    try:
        # Read the file as bytes first to handle different possible text encodings
        # in the NZB file.
        with open(file_path, 'rb') as f:
            nzb_bytes = f.read()

        # The pynzb parsers currently expect a string. We'll try decoding as UTF-8,
        # which is common, and fall back to latin-1 (which covers iso-8859-1)
        # if that fails. A more robust solution would inspect the NZB declaration.
        try:
            nzb_content_str = nzb_bytes.decode('utf-8')
        except UnicodeDecodeError:
            print("Warning: Could not decode as UTF-8, falling back to latin-1.")
            nzb_content_str = nzb_bytes.decode('latin-1')

        # Use the default pynzb parser to process the NZB content.
        # This will automatically select the fastest available parser (lxml, etree, or expat).
        files = nzb_parser.parse(nzb_content_str)

        if not files:
            print("No files were found in the NZB.")
            return

        print("\n--- NZB Content ---")
        for i, nzb_file in enumerate(files, 1):
            # Calculate the total size by summing the bytes of all segments.
            total_size = sum(segment.bytes for segment in nzb_file.segments)

            print(f"\nFile #{i}")
            print(f"  Subject: {nzb_file.subject}")
            print(f"  Size: {format_size(total_size)}")

        print("\n--- End of NZB ---")

    except Exception as e:
        print(f"\nAn error occurred while parsing the file: {e}")
        print("This may not be a valid NZB file.")

if __name__ == "__main__":
    main() 