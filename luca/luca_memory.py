import uuid
import random
from typing import List, Any
from dataclasses import dataclass

@dataclass
class MemoryNode:
   id: str
   content: Any
   embedding: List[float]
   coherence: float
   drift_rate: float
   timestamp: float

class MemoryMesh:
   """
   Plastic, drifting associative network.
   """
   def __init__(self, genome_ref):
       self.genome = genome_ref
       self.nodes: List[MemoryNode] = []

   def encode(self, content: Any, vector: List[float], stability: float = 0.5):
       node = MemoryNode(
           id=str(uuid.uuid4())[:8],
           content=content,
           embedding=vector,
           coherence=stability,
           drift_rate=(1.0 - stability) * self.genome.plasticity_coefficient,
           timestamp=0.0
       )
       self.nodes.append(node)

   def tick(self, chaos_val: float):
       alive_nodes = []
       for node in self.nodes:
           if random.random() < node.drift_rate:
               distortion = chaos_val * 0.05
               node.embedding = [v + random.uniform(-distortion, distortion) for v in node.embedding]
           node.coherence -= 0.0005
           if node.coherence > 0.05:
               alive_nodes.append(node)
       self.nodes = alive_nodes