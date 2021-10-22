# Implements RRT
# By: Vishnu Devarakonda
from Tree import TreeNode

class RRT:
    def __init__(self, collision : function, nearest: function) -> None:
        """
        Initialize an RRT object
        args:
            collision: Function with params (state, obstacles). Returns true
            if state collides with any obstacles else False
            nearest: Function with params (state, [List of TreeNodes]). Returns
            the nearest/best node to state.
        """
        self._collision = collision
        self._nearest = nearest

    def run(self, start_node, obstacles : list, sampler: function, K = 100):
        """
        Function run RRT
        args:
            start_node: Tuple. The start state.
            obstacles: List. Obstacles that are in the space.
            sampler: Function with params(state). Determines how to sample a
            random point from the space.
        """
        head = TreeNode(start_node)
        G = [ head ]
        while K:
            new_state = sampler()
            if not self._collision(new_state, obstacles):
                new_node = TreeNode(new_state)
                nearest_node = self._nearest(new_state, G)
                nearest_node._nodes.append(new_node)
                G.append(new_node)
            K -= 1
        return head