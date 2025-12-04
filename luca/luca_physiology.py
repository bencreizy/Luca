class Physiology:
   """
   The Metabolic Substrate.
   LUCA 'burns' resources to think.
   """
   def __init__(self, genome_ref):
       self.genome = genome_ref
       self.oxygenation = 1.0  
       self.glucose = 1.0      
       self.fatigue = 0.0      
       self.waste_entropy = 0.0 
       self.heart_rate = 60    
       
   def metabolize(self, cognitive_load: float):
       burn_rate = cognitive_load * (1.0 / self.genome.metabolic_efficiency)
       self.oxygenation = max(0.0, self.oxygenation - (burn_rate * 0.01))
       self.glucose = max(0.0, self.glucose - (burn_rate * 0.005))
       self.waste_entropy += burn_rate * 0.02
       self.oxygenation = min(1.0, self.oxygenation + 0.005)
       
       if self.waste_entropy > self.genome.drift_ceiling:
           self.fatigue = min(1.0, self.fatigue + 0.01)

   def get_performance_scalar(self) -> float:
       return self.oxygenation * (1.0 - self.fatigue)
       
   def reset(self):
       self.oxygenation = 1.0
       self.glucose = 1.0
       self.waste_entropy = 0.0
       self.fatigue = 0.0