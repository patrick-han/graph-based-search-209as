# Implements RRT
# By: Vishnu Devarakonda
from Tree import TreeNode
import numpy as np

class RRT:
    def __init__(self, nearest: function) -> None:
        """
        Initialize an RRT object
        args:
            collision: Function with params (state, obstacles). Returns true
            if state collides with any obstacles else False
            nearest: Function with params (state, [List of TreeNodes]). Returns
            the nearest/best node to state.
        """
        self._nearest = nearest

    def get_closest(self, node_list, state):
        minDist = float('inf')
        return_state = None
        for node in node_list:
            node_state = node.val
            distance = np.linalg.norm(state - node_state, 2)
            if distance < minDist:
                minDist = distance
                return_state = node_state
        return return_state

    def run(self, start_node, obstacles : list, sampler: function, drive: function, K = 100, step_count=100):
        """
        Function run RRT
        args:
            start_node: Tuple. The start state.
            obstacles: List. Obstacles that are in the space.
            sampler: Function with params(state). Determines how to sample a
            random point from the space.
            drive: Function with params(state1, state2). Function returns a new
            state when driving from state1 to state2.
        """
        head = TreeNode(start_node)
        G = [ head ]
        while K:
            new_state = sampler()
            closest_state = self.get_closest(G, new_state)
            for obs in obstacles:
                new_state = obs.findMaxTrajectory(closest_state, new_state, step_count)
            new_node = TreeNode(new_state)
            nearest_node = self._nearest(new_state, G)
            nearest_node._nodes.append(new_node)
            G.append(new_node)
            K -= 1
        return head