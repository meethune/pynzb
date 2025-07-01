# flake8: noqa: F401
from pynzb.etree_nzb import ETreeNZBParser

# Try to import lxml parser, but don't fail if it's not available
try:
    from pynzb.lxml_nzb import LXMLNZBParser

    # lxml is fastest when available
    nzb_parser = LXMLNZBParser()
except ImportError:
    # Fall back to built-in ElementTree (still quite fast)
    nzb_parser = ETreeNZBParser()
