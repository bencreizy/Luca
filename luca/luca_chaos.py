class ChaosEngine:
   """
   Lorenz Attractor-based turbulence injector.
   """
   def __init__(self):
       self.x, self.y, self.z = 0.1, 0.1, 0.1
       self.sigma, self.rho, self.beta = 10.0, 28.0, 8.0/3.0
       self.dt = 0.01

   def tick(self) -> float:
       dx = (self.sigma * (self.y - self.x)) * self.dt
       dy = (self.x * (self.rho - self.z) - self.y) * self.dt
       dz = (self.x * self.y - self.beta * self.z) * self.dt
       self.x += dx; self.y += dy; self.z += dz
       return max(0.0, min(1.0, (self.x + 20) / 40.0))

   def suppress(self, factor: float = 0.5):
       self.x *= factor
       self.y *= factor
       self.z *= factor