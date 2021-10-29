# Obstacle class for graph-based search problems
# By Patrick Han
import numpy as np

class Obstacle:
    """
    Implements base class for an N-D polygonal obstacle
    """
    def __init__(self):
        """
        _vertices : Ordered list of vertices and connections, last vertex is connected to the first in the list
        """
        self._vertices = []
        self._dim = None
    def isCollision(self, point):
        """
        args:
            point : N-D tuple coordinate of the point we want to check if it collides with the obstacle
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
            N-D tuple of the last successful step taken
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


class AxisAlignedRectangle2D(Obstacle):
    """
    Implements class for a 2D Axis-Aligned rectangular obstacle
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
        self._dim = 2

        if len(lowerLeft) != 2 or len(upperRight) != 2:
            print("AxisAlignedRectangle2D must be specified with 2-dimensional coordinates")
            raise

        self._vertices.append(lowerLeft)
        self._vertices.append((lowerLeft[0], upperRight[1])) # Upper left
        self._vertices.append(upperRight)
        self._vertices.append((upperRight[0], lowerLeft[1])) # Lower right

        self._lowerLeft = lowerLeft
        self._upperRight = upperRight

        # 1->2
        # ^  V
        # 0<-3

    def isCollision(self, point):
        if len(point) != 2:
            print("Must specify 2D point for collision check with AxisAlignedRectangle2D")
            raise
        # Just need to check if the x coordinate of the point is to the right of lower left's and the left of upper right's
        # AND
        # if the y coordinate of the point is above lower left's and below upper right's
        if point[0] <= self._upperRight[0] and point[0] >= self._lowerLeft[0] and point[1] <= self._upperRight[1] and point[1] >= self._lowerLeft[1]:
            return True
        else:
            return False


class AxisAlignedRectangle3D(Obstacle):
    """
    Implements class for a 3D Axis-Aligned rectangular obstacle. The z coordinates for the lowerLeft and lowerRight must match
    """
    def __init__(self, lowerLeft, upperRight, height):
        """
        args:
            lowerLeft  : (x,y,z') coordinate of the lower left corner of the base
            upperRight : (x,y,z') coordinate of the upper right corner of the base
            height : z-coordinate for height
        returns:
            Nothing
        """
        super().__init__()
        self._dim = 3

        if len(lowerLeft) != 3 or len(upperRight) != 3 or lowerLeft[2] != upperRight[2]:
            print("AxisAlignedRectangle3D must be specified with 3-dimensional coordinates with matching z-coordinates for arguments lowerLeft and upperRight")
            raise

        # Bottom layer
        self._vertices.append(lowerLeft)
        self._vertices.append((lowerLeft[0], upperRight[1], lowerLeft[2])) # Upper left
        self._vertices.append(upperRight)
        self._vertices.append((upperRight[0], lowerLeft[1], lowerLeft[2])) # Lower right
        self._vertices.append(lowerLeft)

        # Top layer
        lowerLeftTop = (lowerLeft[0], lowerLeft[1], lowerLeft[2] + height)
        upperRightTop = (upperRight[0], upperRight[1], upperRight[2] + height)
        self._vertices.append(lowerLeftTop)
        self._vertices.append((lowerLeftTop[0], upperRightTop[1], lowerLeftTop[2])) # Upper left
        self._vertices.append(upperRightTop)
        self._vertices.append((upperRightTop[0], lowerLeftTop[1], lowerLeftTop[2])) # Lower right
        self._vertices.append(lowerLeftTop)


        self._lowerLeft = lowerLeft
        self._upperRight = upperRight
        self._lowerLeftTop = lowerLeftTop

        # Might revisit this later, since this is really only for drawing purposes
        # 6->7
        # ^  V
        # 5/9<-8

        # 1->2
        # ^  V
        # 0/4<-3

    def isCollision(self, point):
        if len(point) != 3:
            print("Must specify 3D point for collision check with AxisAlignedRectangle3D")
            raise
        # Just need to check if the x coordinate of the point is to the right of lower left's and the left of upper right's
        # AND
        # if the y coordinate of the point is above lower left's and below upper right's
        # AND
        # if the z coordinate of the point is between the z coordinates of lowerLeft and lowerLeftTop
        if point[0] <= self._upperRight[0] and point[0] >= self._lowerLeft[0] and point[1] <= self._upperRight[1] and point[1] >= self._lowerLeft[1]:
            if point[2] >= self._lowerLeft[2] and point[2] <= self._lowerLeftTop[2]:
                return True
            else:
                return False
        else:
            return False