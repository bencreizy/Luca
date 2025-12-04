import time
from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class InfusionPacket:
   modality: str = "COGNITIVE_INFUSION"
   intensity: float = 1.0
   payload: Dict[str, Any] = field(default_factory=dict)
   timestamp: float = 0.0

class CognitiveInfusionEngine:
   """
   The CIE: A synthetic organ for high-intensity knowledge integration.
   """
   def __init__(self, entity_ref):
       self.entity = entity_ref
       self.active = False
       self.cooldown = 0
       self.last_event_ts = 0

   def inject(self, packet: InfusionPacket):
       if self.cooldown > 0:
           return {"status": "REJECTED", "reason": "COOLDOWN_ACTIVE"}

       self.active = True
       self.last_event_ts = time.time()
       
       # Hyperplasticity
       old_plasticity = self.entity.genome.plasticity_coefficient
       self.entity.genome.plasticity_coefficient = 1.0
       self.entity.chaos.suppress(0.3)
       
       frameworks = packet.payload.get("frameworks", [])
       vectors = packet.payload.get("knowledge_vectors", [])
       
       for vec in vectors:
           self.entity.memory.encode("INFUSION_DATA", vec, stability=1.0)
           
       if len(frameworks) > 0:
           self.entity.genome.metabolic_efficiency += 0.05
           self.entity.genome.dimensional_complexity += 0.02
           self.entity.genome.inhibition_bias += 0.05
           
           for fw in frameworks:
               organ_name = f"{fw.upper()}_CORTEX"
               self.entity.organ_fabricator.fabricate(organ_name, "Processing_Lobe", ["analysis"])

       self.active = False
       self.cooldown = 50
       self.entity.genome.plasticity_coefficient = old_plasticity
       return {"status": "ACCEPTED", "growth": len(frameworks)}

   def tick(self):
       if self.cooldown > 0: self.cooldown -= 1