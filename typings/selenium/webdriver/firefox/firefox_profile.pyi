"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

WEBDRIVER_EXT = "webdriver.xpi"
WEBDRIVER_PREFERENCES = "webdriver_prefs.json"
EXTENSION_NAME = "fxdriver@googlecode.com"
class AddonFormatError(Exception):
    """Exception for not well-formed add-on manifest files"""
    ...


class FirefoxProfile(object):
    ANONYMOUS_PROFILE_NAME = ...
    DEFAULT_PREFERENCES = ...
    def __init__(self, profile_directory: Optional[Any] = ...):
        """
        Initialises a new instance of a Firefox Profile

        :args:
         - profile_directory: Directory of profile that you want to use. If a
           directory is passed in it will be cloned and the cloned directory
           will be used by the driver when instantiated.
           This defaults to None and will create a new
           directory when object is created.
        """
        self.default_preferences = ...
        self.native_events_enabled = ...
        self.profile_dir = ...
        self.tempfolder = ...
        self.extensionsDir = ...
        self.userPrefs = ...
    
    def set_preference(self, key, value):
        """
        sets the preference that we want in the profile.
        """
        ...
    
    def add_extension(self, extension=...):
        ...
    
    def update_preferences(self):
        ...
    
    @property
    def path(self):
        """
        Gets the profile directory that is currently being used
        """
        ...
    
    @property
    def port(self):
        """
        Gets the port that WebDriver is working on
        """
        ...
    
    @port.setter
    def port(self, port):
        """
        Sets the port that WebDriver will be running on
        """
        ...
    
    @property
    def accept_untrusted_certs(self):
        ...
    
    @accept_untrusted_certs.setter
    def accept_untrusted_certs(self, value):
        ...
    
    @property
    def assume_untrusted_cert_issuer(self):
        ...
    
    @assume_untrusted_cert_issuer.setter
    def assume_untrusted_cert_issuer(self, value):
        ...
    
    @property
    def native_events_enabled(self):
        ...
    
    @native_events_enabled.setter
    def native_events_enabled(self, value):
        ...
    
    @property
    def encoded(self):
        """
        A zipped, base64 encoded string of profile directory
        for use with remote WebDriver JSON wire protocol
        """
        ...
    
    def set_proxy(self, proxy):
        ...
    
    def _set_manual_proxy_preference(self, key, setting):
        ...
    
    def _create_tempfolder(self):
        """
        Creates a temp folder to store User.js and the extension
        """
        ...
    
    def _write_user_prefs(self, user_prefs):
        """
        writes the current user prefs dictionary to disk
        """
        ...
    
    def _read_existing_userjs(self, userjs):
        ...
    
    def _install_extension(self, addon, unpack: bool = ...):
        """
            Installs addon from a filepath, url
            or directory of addons in the profile.
            - path: url, absolute path to .xpi, or directory of addons
            - unpack: whether to unpack unless specified otherwise in the install.rdf
        """
        ...
    
    def _addon_details(self, addon_path):
        """
        Returns a dictionary of details about the addon.

        :param addon_path: path to the add-on directory or XPI

        Returns::

            {'id':      u'rainbow@colors.org', # id of the addon
             'version': u'1.4',                # version of the addon
             'name':    u'Rainbow',            # name of the addon
             'unpack':  False }                # whether to unpack the addon
        """
        ...
    


