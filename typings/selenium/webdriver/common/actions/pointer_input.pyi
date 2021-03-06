"""
This type stub file was generated by pyright.
"""

from .input_device import InputDevice
from typing import Any, Optional

class PointerInput(InputDevice):
    DEFAULT_MOVE_DURATION = ...
    def __init__(self, kind, name):
        self.type = ...
        self.kind = ...
        self.name = ...
    
    def create_pointer_move(self, duration=..., x: Optional[Any] = ..., y: Optional[Any] = ..., origin: Optional[Any] = ...):
        ...
    
    def create_pointer_down(self, button):
        ...
    
    def create_pointer_up(self, button):
        ...
    
    def create_pointer_cancel(self):
        ...
    
    def create_pause(self, pause_duration):
        ...
    
    def encode(self):
        ...
    


