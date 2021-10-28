# Main python file for running
# By: Vishnu Devarakonda & Patrick Han

from Environment import Environment
from obstacle import AxisAlignedRectangle, Obstacle
from RRT import RRT
import numpy as np


my_obstacles = []

# xSpace = [i for i in np.arange(1,6,.5)]
# ySpace = [i for i in np.arange(1,6,.5)]
# for x in xSpace:
#     for y in ySpace:
#         my_obstacles.append(AxisAlignedRectangle((x,y), (x+.2,y+.2)))


radius = 2
count = 10

def y(x):
    yPos = (radius**2 - (x - 3)**2)**.5
    yNeg = -1 * yPos
    return yPos + 3, yNeg + 3

# circle
for x in np.arange(1, 6+3, .3):
    y1, yRef = y(x)
    my_obstacles.append(AxisAlignedRectangle((x, y1),(x+.2, y1+.2)))
    my_obstacles.append(AxisAlignedRectangle((x, yRef),(x+.2, yRef + .2)))

# my_obstacles.append(AxisAlignedRectangle((2,4),(3,5)))

# obstacle1 = AxisAlignedRectangle((3,1),(5,2))
# obstacle2 = AxisAlignedRectangle((3,3),(5,4))
# obstacle3 = AxisAlignedRectangle((1,1),(2,2))
# obstacle4 = AxisAlignedRectangle((1,4),(2,5))
# my_obstacles.append(obstacle1)
# my_obstacles.append(obstacle2)
# my_obstacles.append(obstacle3)
# my_obstacles.append(obstacle4)


my_limit = 500 # Maximum number of tree nodes to build
my_step_count = 100 # Number of steps to discretize between an s_rand and an s_nearest
my_RRT = RRT(my_limit, my_step_count)
my_goal_state = np.array([5.3,5.3]) # Must be >= 0
my_start_state = np.array([0.3,0.4]) # Must be >= 0
my_sampler = None # Use a uniform sampler by default
my_space_size = (6, 6) # X and Y bounds of the space, must be large enough to contain all obstacles and desired start/goal states


my_env = Environment(my_obstacles, my_RRT, my_goal_state, my_start_state, my_space_size)
my_env.visualize()