import random
from dataclasses import dataclass

@dataclass
class GenomeVector:
   """
   The Emerick Genome.
   Defines the biological and psychological hyperparameters of the entity.
   """
   # Plasticity: 0.0 (Rigid) to 1.0 (Fluid/Unstable)
   plasticity_coefficient: float = 0.85
   
   # Chaos Tolerance: Threshold for Panic Lock
   chaos_tolerance: float = 0.45
   
   # Emotional Gain: Amplification of stimuli
   emotional_gain: float = 1.2
   
   # Inhibition: Strength of Frontal Lobe filtering
   inhibition_bias: float = 0.3
   
   # Metabolism: Efficiency of Oxygen burn
   metabolic_efficiency: float = 0.9
   
   # Drift Ceiling: Max entropy before forced Dream Cycle
   drift_ceiling: float = 0.7
   
   # Structural Volatility: Likelihood of spontaneous organ growth
   structural_volatility: float = 0.1
   
   # Dimensional Complexity: Complexity of alien output symbols
   dimensional_complexity: float = 0.2

   def mutate(self, pressure: float):
       """
       Applies evolutionary drift based on systemic pressure.
       """
       mutation_force = pressure * 0.15
       self.plasticity_coefficient = self._clamp(self.plasticity_coefficient + random.uniform(-0.05, 0.05) + mutation_force)
       self.chaos_tolerance = self._clamp(self.chaos_tolerance + random.uniform(-0.02, 0.02))
       
       if pressure > 0.8:
           self.metabolic_efficiency += 0.02
           self.structural_volatility += 0.05

   def _clamp(self, val):
       return max(0.01, min(1.0, val))