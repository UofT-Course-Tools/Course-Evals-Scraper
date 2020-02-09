"""
This type stub file was generated by pyright.
"""

class Log(object):
    def __init__(self):
        self.level = ...
    
    def to_capabilities(self):
        ...
    


class Options(object):
    KEY = ...
    def __init__(self):
        self.log = ...
    
    @property
    def binary(self):
        """Returns the FirefoxBinary instance"""
        ...
    
    @binary.setter
    def binary(self, new_binary):
        """Sets location of the browser binary, either by string or
        ``FirefoxBinary`` instance.

        """
        ...
    
    @property
    def binary_location(self):
        """Returns the location of the binary."""
        ...
    
    @binary_location.setter
    def binary_location(self, value):
        """ Sets the location of the browser binary by string """
        self.binary = ...
    
    @property
    def accept_insecure_certs(self):
        ...
    
    @accept_insecure_certs.setter
    def accept_insecure_certs(self, value):
        ...
    
    @property
    def capabilities(self):
        ...
    
    def set_capability(self, name, value):
        """Sets a capability."""
        ...
    
    @property
    def preferences(self):
        """Returns a dict of preferences."""
        ...
    
    def set_preference(self, name, value):
        """Sets a preference."""
        ...
    
    @property
    def proxy(self):
        """ returns Proxy if set otherwise None."""
        ...
    
    @proxy.setter
    def proxy(self, value):
        ...
    
    @property
    def profile(self):
        """Returns the Firefox profile to use."""
        ...
    
    @profile.setter
    def profile(self, new_profile):
        """Sets location of the browser profile to use, either by string
        or ``FirefoxProfile``.

        """
        ...
    
    @property
    def arguments(self):
        """Returns a list of browser process arguments."""
        ...
    
    def add_argument(self, argument):
        """Add argument to be used for the browser process."""
        ...
    
    @property
    def headless(self):
        """
        Returns whether or not the headless argument is set
        """
        ...
    
    @headless.setter
    def headless(self, value):
        """
        Sets the headless argument

        Args:
          value: boolean value indicating to set the headless option
        """
        ...
    
    def set_headless(self, headless: bool = ...):
        """ Deprecated, options.headless = True """
        self.headless = ...
    
    def to_capabilities(self):
        """Marshals the Firefox options to a `moz:firefoxOptions`
        object.

        """
        ...
    

