from xml.etree import ElementTree as etree
from io import BytesIO

from pynzb.base import BaseETreeNZBParser

class ETreeNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, xml, et=etree):
        return iter(et.iterparse(BytesIO(xml.encode('utf-8')), events=("start", "end")))