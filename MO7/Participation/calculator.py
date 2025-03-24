from dataclasses import dataclass

@dataclass
class calculation():
    diameter:float = 0.0
    
    def calculate(self):
        if self.diameter != 0:
            pi = float(3.14159265359)
            radius = self.diameter / 2
            circumference = 2 * pi * radius

            return circumference
        
        else:
            self.message += f"Diameter must not be empty"