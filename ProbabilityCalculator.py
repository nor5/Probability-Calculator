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
    
      
  def draw(self,num_balls_drawn):
   # contents2 = copy.deepcopy(self.contents)
    if num_balls_drawn > len(self.contents):
      return self.contents
    else:
      drawn_balls = random.sample(self.contents, int(num_balls_drawn))
      for b in drawn_balls:
        if b in self.contents:
          
         self.contents.remove(b)
    
    return drawn_balls
    
    
      
    
    


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  expected_ballsList = []
  
  for key, value in expected_balls.items():
      for i in range (0, value):
        expected_ballsList.append(key)
  print(expected_ballsList)      
  for i in range (0,num_experiments):
    allMatch = True
    newHat = copy.deepcopy(hat)
    drawn_ballsList = newHat.draw(num_balls_drawn)
    for key in expected_balls.keys():
       if drawn_ballsList.count(key) < expected_balls[key]:
   
         allMatch = False
         break
    if allMatch:
        
            m += 1
    
    
  probability = m / num_experiments
  return probability


	
