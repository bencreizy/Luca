import json
import time
import uuid
from dataclasses import dataclass, asdict
from typing import Dict, Any

@dataclass
class StimulusPacket:
   id: str
   timestamp: float
   modality: str
   intensity: float
   payload: Dict[str, Any]

class SensoryBridge:
   """
   The I/O Layer.
   """
   def __init__(self, kernel_ref):
       self.kernel = kernel_ref

   def transduce_text(self, text: str, urgency: float = 0.5):
       packet = StimulusPacket(
           id=str(uuid.uuid4()),
           timestamp=time.time(),
           modality="TEXT",
           intensity=urgency,
           payload={"content": text}
       )
       return packet

   def transduce_infusion(self, infusion_data: Dict):
       from luca_infusion import InfusionPacket
       packet = InfusionPacket(
           modality="COGNITIVE_INFUSION",
           intensity=infusion_data.get("intensity", 1.0),
           payload=infusion_data.get("payload", {}),
           timestamp=time.time()
       )
       return packet