from io import BytesIO
from xml.etree import ElementTree as etree

from pynzb.base import BaseETreeNZBParser


class ETreeNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, nzb, et=etree):
        return iter(et.iterparse(BytesIO(nzb.encode("utf-8")), events=("start", "end")))
