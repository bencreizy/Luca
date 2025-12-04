class EmotionSwarm:
   """
   Affective Pressure System (VAD).
   """
   def __init__(self, genome_ref):
       self.genome = genome_ref
       self.valence = 0.0 
       self.arousal = 0.0 
       self.dominance = 0.5

   def modulate(self, stimulus_intensity: float, chaos_val: float):
       delta = stimulus_intensity * self.genome.emotional_gain
       self.arousal = min(1.0, self.arousal + delta + (chaos_val * 0.15))
       self.arousal *= 0.95
       if chaos_val > 0.8:
           self.valence += (0.5 - chaos_val) * 0.1

   def is_panicking(self) -> bool:
       return self.arousal > (self.genome.chaos_tolerance * 2.0)