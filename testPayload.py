from typing import Any, Dict, List, Union
from dataclasses import dataclass

@dataclass
class Information:
   name: str
   description: str

@dataclass
class testPayload:
   information: Information