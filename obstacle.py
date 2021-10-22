# Obstacle class for RRT
# By Patrick Han


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
    


class AxisAlignedRectangle(Obstacle):
    """
    Implements class for an Axis-Aligned rectangular obstacle
    """
    def __init__(self, lowerLeft, upperRight):
        """
        args:
            lowerLeft  : 
            upperRight :
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


