"""
This type stub file was generated by pyright.
"""

from selenium.webdriver.common import service
from typing import Any, Optional

class Service(service.Service):
    """
    Object that manages the starting and stopping of the IEDriver
    """
    def __init__(self, executable_path, port=..., host: Optional[Any] = ..., log_level: Optional[Any] = ..., log_file: Optional[Any] = ...):
        """
        Creates a new instance of the Service

        :Args:
         - executable_path : Path to the IEDriver
         - port : Port the service is running on
         - host : IP address the service port is bound
         - log_level : Level of logging of service, may be "FATAL", "ERROR", "WARN", "INFO", "DEBUG", "TRACE".
           Default is "FATAL".
         - log_file : Target of logging of service, may be "stdout", "stderr" or file path.
           Default is "stdout"."""
        self.service_args = ...
    
    def command_line_args(self):
        ...
    


