"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.common import service
from typing import Any, Optional

class Service(service.Service):
    """
    Object that manages the starting and stopping of the WebKitGTKDriver
    """
    def __init__(self, executable_path, port=..., log_path: Optional[Any] = ...):
        """
        Creates a new instance of the Service

        :Args:
         - executable_path : Path to the WebKitGTKDriver
         - port : Port the service is running on
         - log_path : Path for the WebKitGTKDriver service to log to
        """
        ...
    
    def command_line_args(self):
        ...
    
    def send_remote_shutdown_command(self):
        ...
    


