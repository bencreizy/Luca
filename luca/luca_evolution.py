class EvolutionEngine:
   """
   Manages EPI and Metamorphosis.
   """
   def __init__(self, entity_ref):
       self.entity = entity_ref
       self.pressure_index = 0.0

   def calculate_pressure(self):
       phys = self.entity.physiology
       emo = self.entity.emotion
       gen = self.entity.genome
       
       raw_pressure = (phys.waste_entropy + phys.fatigue + emo.arousal)
       self.pressure_index = raw_pressure / max(0.1, gen.chaos_tolerance)

       if self.pressure_index > 0.5:
           gen.mutate(self.pressure_index)

       # Trigger Metamorphosis
       if self.pressure_index > 0.95:
           self.entity.collapse_and_rebirth()