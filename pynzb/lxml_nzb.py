try:
    from lxml import etree  # type: ignore
except ImportError:
    raise ImportError("lxml is not installed. Install it with: pip install pynzb[lxml]")

from io import BytesIO

from pynzb.base import BaseETreeNZBParser


class LXMLNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, nzb, et=etree):
        return iter(et.iterparse(BytesIO(nzb.encode("utf-8")), events=("start", "end")))
