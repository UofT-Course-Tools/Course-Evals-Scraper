"""
This type stub file was generated by pyright.
"""

from bs4.builder import HTMLTreeBuilder, TreeBuilder
from typing import Any, Optional

__license__ = "MIT"
__all__ = ['LXMLTreeBuilderForXML', 'LXMLTreeBuilder']
LXML = 'lxml'
def _invert(d):
    "Invert a dictionary."
    ...

class LXMLTreeBuilderForXML(TreeBuilder):
    DEFAULT_PARSER_CLASS = ...
    is_xml = ...
    processing_instruction_class = ...
    NAME = ...
    ALTERNATE_NAMES = ...
    features = ...
    CHUNK_SIZE = ...
    DEFAULT_NSMAPS = ...
    DEFAULT_NSMAPS_INVERTED = ...
    def initialize_soup(self, soup):
        """Let the BeautifulSoup object know about the standard namespace
        mapping.
        """
        ...
    
    def _register_namespaces(self, mapping):
        """Let the BeautifulSoup object know about namespaces encountered
        while parsing the document.

        This might be useful later on when creating CSS selectors.
        """
        ...
    
    def default_parser(self, encoding):
        ...
    
    def parser_for(self, encoding):
        ...
    
    def __init__(self, parser: Optional[Any] = ..., empty_element_tags: Optional[Any] = ..., **kwargs):
        self.soup = ...
        self.nsmaps = ...
    
    def _getNsTag(self, tag):
        ...
    
    def prepare_markup(self, markup, user_specified_encoding: Optional[Any] = ..., exclude_encodings: Optional[Any] = ..., document_declared_encoding: Optional[Any] = ...):
        """
        :yield: A series of 4-tuples.
         (markup, encoding, declared encoding,
          has undergone character replacement)

        Each 4-tuple represents a strategy for parsing the document.
        """
        ...
    
    def feed(self, markup):
        ...
    
    def close(self):
        self.nsmaps = ...
    
    def start(self, name, attrs, nsmap=...):
        ...
    
    def _prefix_for_namespace(self, namespace):
        """Find the currently active prefix for the given namespace."""
        ...
    
    def end(self, name):
        ...
    
    def pi(self, target, data):
        ...
    
    def data(self, content):
        ...
    
    def doctype(self, name, pubid, system):
        ...
    
    def comment(self, content):
        "Handle comments as Comment objects."
        ...
    
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        ...
    


class LXMLTreeBuilder(HTMLTreeBuilder, LXMLTreeBuilderForXML):
    NAME = ...
    ALTERNATE_NAMES = ...
    features = ...
    is_xml = ...
    processing_instruction_class = ...
    def default_parser(self, encoding):
        ...
    
    def feed(self, markup):
        ...
    
    def test_fragment_to_document(self, fragment):
        """See `TreeBuilder`."""
        ...
    

