from dataclasses import dataclass

@dataclass
class calculation():
    diameter:float = 0.0
    circumference:float = 0.0

    def calculate(self):
        if self.diameter == 0 and self.circumference != 0:
            pi = float(3.14159265359)
            radius = self.circumference / pi / 2
            diameter = 2 * radius

            return diameter
        
        elif self.diameter != 0 and self.circumference == 0:
            pi = float(3.14159265359)
            radius = self.diameter / 2
            circumference = 2 * pi * radius

            return circumference
        
        else:
            self.message += f"Diameter or Circumference must not be empty"