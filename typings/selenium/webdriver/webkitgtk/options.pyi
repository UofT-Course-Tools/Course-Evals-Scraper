"""
This type stub file was generated by pyright.
"""

class Options(object):
    KEY = ...
    def __init__(self):
        ...
    
    @property
    def capabilities(self):
        ...
    
    def set_capability(self, name, value):
        """Sets a capability."""
        ...
    
    @property
    def binary_location(self):
        """
        Returns the location of the browser binary otherwise an empty string
        """
        ...
    
    @binary_location.setter
    def binary_location(self, value):
        """
        Allows you to set the browser binary to launch

        :Args:
         - value : path to the browser binary
        """
        ...
    
    @property
    def arguments(self):
        """
        Returns a list of arguments needed for the browser
        """
        ...
    
    def add_argument(self, argument):
        """
        Adds an argument to the list

        :Args:
         - Sets the arguments
        """
        ...
    
    @property
    def overlay_scrollbars_enabled(self):
        """
        Returns whether overlay scrollbars should be enabled
        """
        ...
    
    @overlay_scrollbars_enabled.setter
    def overlay_scrollbars_enabled(self, value):
        """
        Allows you to enable or disable overlay scrollbars

        :Args:
         - value : True or False
        """
        ...
    
    def to_capabilities(self):
        """
        Creates a capabilities with all the options that have been set and
        returns a dictionary with everything
        """
        ...
    

