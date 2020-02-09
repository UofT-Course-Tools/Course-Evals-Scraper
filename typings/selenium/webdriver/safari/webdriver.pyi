"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from typing import Any, Optional

class WebDriver(RemoteWebDriver):
    """
    Controls the SafariDriver and allows you to drive the browser.

    """
    def __init__(self, port=..., executable_path=..., reuse_service: bool = ..., desired_capabilities=..., quiet: bool = ..., keep_alive: bool = ..., service_args: Optional[Any] = ...):
        """

        Creates a new Safari driver instance and launches or finds a running safaridriver service.

        :Args:
         - port - The port on which the safaridriver service should listen for new connections. If zero, a free port will be found.
         - executable_path - Path to a custom safaridriver executable to be used. If absent, /usr/bin/safaridriver is used.
         - reuse_service - If True, do not spawn a safaridriver instance; instead, connect to an already-running service that was launched externally.
         - desired_capabilities: Dictionary object with desired capabilities (Can be used to provide various Safari switches).
         - quiet - If True, the driver's stdout and stderr is suppressed.
         - keep_alive - Whether to configure SafariRemoteConnection to use
             HTTP keep-alive. Defaults to False.
         - service_args : List of args to pass to the safaridriver service
        """
        self.service = ...
    
    def quit(self):
        """
        Closes the browser and shuts down the SafariDriver executable
        that is started when starting the SafariDriver
        """
        ...
    
    def set_permission(self, permission, value):
        ...
    
    def get_permission(self, permission):
        ...
    
    def debug(self):
        ...
    

