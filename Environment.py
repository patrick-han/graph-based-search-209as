# Enviroment class handeles all the scene and the generated graph on the env.
# By: Vishnu Devarakonda
import numpy as np

class Environment:
    def __init__(self, obstacles, graph_builder, goal_state, start_state = np.array([0,0]), limit = 100, step_count = 100, sampler = None) -> None:
        """
        Initilize an environment object.
        args:
            obstacles: List. List of obstacles in the environment
            graph_builder: Object. Used to construct the graph
                on the environment. 
            goal_state: numpy array. The goal state to search the graph for.
            start_state: numpy array. The starting state.
            limit: Number of RRT iterations to run.
            step_count: Number of steps to make between randomly sampled point
              and closest point in RRT graph.
            sampler: Function with params(state). Determines how to sample a
            random point from the space.
        """
        self._xspace = (0, 10)
        self._yspace = (0, 10)
        self._obstacles = obstacles
        self._graph = graph_builder.run(
            start_state, 
            self._obstacles, 
            self.uniform_sample if not sampler else sampler,
            limit,
            step_count) 


    def uniform_sample(self):
        state = np.array([np.random.rand(), np.random.rand()])
        return state