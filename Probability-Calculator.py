# Importing modules 
import copy
import random

class Hat:

"""
    Defining the hat class: 
        -> This is the class which we use to create hats 
        -> Each of those hats contains balls 
        -> The __init__ method <- This is the method which allows us to set the number of different balls 
            of each colour in the hat
        -> We have a number of balls and the colour of each type of ball 
        -> This method takes this and puts it into a list for the hat 
        -> We are taking the colour and repeating it in the list by the frequency we have been given for 
            that colour 
        -> Then doing this for all of the balls in the hat
"""

    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments