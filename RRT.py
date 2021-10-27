# Implements RRT
# By: Vishnu Devarakonda
from Tree import TreeNode
import numpy as np

class RRT:
    def __init__(self) -> None:
        """
        Initialize an RRT object
        """

    def get_closest(self, node_list, state):
        """
        args:
            node_list: List of TreeNodes.
            state: numpy array. The state to check distance against.
        """
        minDist = float('inf')
        return_node = None
        for node in node_list:
            node_state = node._val
            distance = np.linalg.norm(state - node_state, 2)
            if distance < minDist:
                minDist = distance
                return_node = node
        return return_node

    def run(self, start_state, goal_state, obstacles : list, sampler, limit = 100, step_count=100):
        """
        Function run RRT
        args:
            start_state: numpy array. The start state.
            goal_state: numpy array. The goal state to search for.
            obstacles: List. Obstacles that are in the space.
            sampler: Function with params(state). Determines how to sample a
            random point from the space.
            limit: Number of RRT iterations to run.
            step_count: Number of steps to make between randomly sampled point
              and closest point in RRT graph.
        """
        head = TreeNode(start_state)
        G = [ head ]
        while limit:
            new_state = goal_state if limit % 5 == 0 else sampler()
            closest_node = self.get_closest(G, new_state)
            for obs in obstacles:
                new_state = obs.findMaxTrajectory(
                    closest_node._val, new_state, step_count)
            new_node = TreeNode(new_state)
            closest_node._nodes.append(new_node)
            G.append(new_node)
            limit -= 1
        return head