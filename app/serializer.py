import json
from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class Serializer(ABC):
    @abstractmethod
    def serialize(self, name, text):
        pass


class JSONSerializer(Serializer):
    def serialize(self, name: str, text: str) -> str:
        return json.dumps({"title": name, "content": text})


class XMLSerializer(Serializer):
    def serialize(self, name: str, text: str) -> str:
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = name
        content = ET.SubElement(root, "content")
        content.text = text
        return ET.tostring(root, encoding="unicode")
