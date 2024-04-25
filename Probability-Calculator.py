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

"""
    Defining the draw function:
        -> This method allows us to draw balls from the hat which we just initialised 
        -> We need to make sure that the number of balls which we are taking out of the hat isn't greater 
            than the number of balls which we have to choose from 
        -> We take the hat with the list of balls in it and remove a random selection of those balls, and 
            return a list of length `n` with these
        -> So each time this function is run on the balls in a hat, it returns a different selection of them 
        -> Rather than using the expected value of the probability, we can run this function multiple times 
            for an experiment 
        -> This is the next function
"""

    def draw(self, n):
        n = min(n, len(self.contents))
        return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]

"""
    Defining the experiment function:
        -> This function is defined outside of the `Hat` class
        -> We are running the draw function multiple times and creating a counter to track the number of 
            successful experiments
        -> Each time we run the draw function, we can calculate if the result matches its expected value 
        -> If it does, then we increment the value of a counter by 1
        -> Then this repeated multiple times by the function <- The more it is then the more accurate the 
            outcome 
        -> Then we take the counter as a percentage of all of the experiments run 
        -> This allows us to simulate a distribution of sample means for a given bag with a certain number 
            of balls in it 
        -> The counter is only incremented if the output of this matches the expected probability for all 
            of the colours in the hat 
"""

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat)
        balls_drawn = another_hat.draw(num_balls_drawn)
        balls_req = sum([1 for k, v in expected_balls.items() if balls_drawn.count(k) >= v])
        m += 1 if balls_req == len(expected_balls) else 0

    return m / num_experiments