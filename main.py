# Main python file for running
# By: Vishnu Devarakonda & Patrick Han

from Environment import Environment
from obstacle import AxisAlignedRectangle, Obstacle
from RRT import RRT
import numpy as np


my_obstacles = []
obstacle1 = AxisAlignedRectangle((3,1),(5,2))
obstacle2 = AxisAlignedRectangle((3,3),(5,4))
my_obstacles.append(obstacle1)
my_obstacles.append(obstacle2)


my_RRT = RRT()
my_goal_state = np.array([5,5]) # Must be >= 0
my_start_state = np.array([0.3,0.4]) # Must be >= 0
my_limit = 20 # Maximum number of tree nodes to build
my_step_count = 100 # Number of steps to discretize between an s_rand and an s_nearest
my_sampler = None # Use a uniform sampler by default
my_space_size = (6, 6) # X and Y bounds of the space, must be large enough to contain all obstacles and desired start/goal states


my_env = Environment(my_obstacles, my_RRT, my_goal_state, my_start_state, my_limit, my_step_count, my_sampler, my_space_size)
my_env.visualize()