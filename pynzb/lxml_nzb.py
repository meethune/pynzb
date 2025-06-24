from pynzb.base import BaseETreeNZBParser, NZBFile, NZBSegment

try:
    from lxml import etree
except ImportError:
    raise ImportError("You must have lxml installed before you can use the " +
        "lxml NZB parser.")

from io import BytesIO

class LXMLNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, xml, et=etree):
        return iter(et.iterparse(BytesIO(xml.encode('utf-8')), events=("start", "end")))