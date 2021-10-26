# Obstacle class for graph-based search problems
# By Patrick Han
from util import *


class Obstacle:
    """
    Implements base class for a polygonal obstacle
    """
    def __init__(self):
        self._vertices = [] # Ordered list of vertices and connections, last vertex is connected to the first in the list
    def isCollision(self, point):
        """
        args:
            point : (x, y) tuple coordinate of the point we want to check if it collides with the obstacle
        returns:
            True if collision occurs, False else
        """
        raise NotImplementedError
    
    def findMaxTrajectory(self, s_nearest, s_rand, num_steps):
        """
        Given a selected s_nearest and a randomly sampled s_rand, take as many steps 
        from s_nearest to s_rand as you can in a world where only this obstacle exists. Return the farthest
        step taken before collision occurs, or s_rand if no collision occurs. The step size is determined
        by linearly sampling num_step steps between s_nearest and s_rand

        args:
            s_nearest : Existing node in the tree that is closest to the sampled s_rand
            s_rand : Sampled node that we'd like to step towards
            num_steps : Number of steps to discretize between s_nearest and s_rand
        returns:
            (x,y) of the last successful step taken
        """

        step_idx = 0

        possible_steps = np.linspace(s_nearest, s_rand, num_steps)

        s_best = s_nearest

        while True:
            s_try = possible_steps[step_idx]

            if self.isCollision(s_try): # This would be logic specific to the obstacle shape
                break # s_best is still the last s_try
            elif step_idx == num_steps - 1: # If we've successfully reached s_rand
                return s_rand
            else:
                s_best = s_try
            
            step_idx += 1

        return s_best


class AxisAlignedRectangle(Obstacle):
    """
    Implements class for an Axis-Aligned rectangular obstacle
    """
    def __init__(self, lowerLeft, upperRight):
        """
        args:
            lowerLeft  : (x,y) coordinate of the lower left corner
            upperRight : (x,y) coordinate of the upper right corner
        returns:
            Nothing
        """
        super().__init__()

        self._vertices.append(lowerLeft)
        self._vertices.append((lowerLeft[0], upperRight[1] - lowerLeft[1])) # Upper left
        self._vertices.append(upperRight)
        self._vertices.append((upperRight[0] - lowerLeft[0], lowerLeft[1])) # Lower right

        self._lowerLeft = lowerLeft
        self._upperRight = upperRight

        # 1->2
        # ^  V
        # 0<-3

    def isCollision(self, point):
        # Just need to check if the x coordinate of the point is to the right of lower left's and the left of upper right's
        # AND
        # if the y coordinate of the point is above lower left's and below upper right's
        if point[0] <= self._upperRight[0] and point[0] >= self._lowerLeft[0] and point[1] <= self._upperRight[1] and point[1] >= self._lowerLeft[1]:
            return True
        else:
            return False