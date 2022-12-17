import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.balls = balls
    self.contents = []
    for key, value in self.balls.items():
      for i in range (0, value):
        self.contents.append(key)
    
      
  def draw(self, balls_nbr):
    drawn_balls = random.sample(self.contents, int(balls_nbr))
    
    return drawn_balls
    
hat = Hat(blue=4, red=2, green=6)



	
