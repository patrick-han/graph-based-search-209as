# Enviroment class handles all the scene and the generated graph on the env.
# By: Vishnu Devarakonda & Patrick Han
import numpy as np
import matplotlib.pyplot as plt

class Environment:
    def __init__(self, obstacles, graph_builder, goal_state, start_state = np.array([0,0]), limit = 100, step_count = 100, sampler = None, space_size = (6,6)) -> None:
        """
        Initilize an environment object.
        args:
            obstacles: List. List of obstacles in the environment
            graph_builder: Object. Used to construct the graph on the environment. 
            goal_state: numpy array. The goal state to search the graph for.
            start_state: numpy array. The starting state.
            limit: Number of RRT iterations to run.
            step_count: Number of steps to make between randomly sampled point and closest point in RRT graph.
            sampler: Function with params(state). Determines how to sample a random point from the space.
            space_size : (x,y) where x bounds the space in the x-axis and y in the y-axis
        """
        self._xspace = (0, space_size[0])
        self._yspace = (0, space_size[1])
        self._obstacles = obstacles
        self._start_state = start_state
        self._goal_state = goal_state
        self._graph = graph_builder.run(
            self._start_state,
            self._goal_state, 
            self._obstacles, 
            self.uniform_sample if not sampler else sampler,
            limit,
            step_count)
        


    def uniform_sample(self):
        """
        Uniformly samples a random point in the space, scaled by the space size

        args:
            None

        returns:
            Sampled point
        """
        state = np.array([np.random.rand() * self._xspace[1], np.random.rand() * self._yspace[1]])
        return state

    def visualize(self):
        """
        Plots all obstacles and a built graph

        args:
            None

        returns:
            None
        """
        
        def plot_graph(head):
            for child in head._nodes:
                stack = np.array([head._val, child._val])
                plot_graph(child)
                plt.plot(stack[:,0], stack[:,1], color = 'red', marker = 'o')
            

        # Plot all obstacles 
        for obstacle in self._obstacles:
            verts = np.array(obstacle._vertices)
            plt.plot(verts[:,0], verts[:,1], color = 'blue')
            loop_verts = np.array([verts[-1], verts[0]]) # Last vert to first vert
            plt.plot(loop_verts[:,0], loop_verts[:,1], color = 'blue') # Close off the shape

        # Plot the full graph/tree
        plot_graph(self._graph)

        # Plot start state
        plt.plot(self._start_state[0], self._start_state[1], color = 'purple', marker = 'o')

        # Plot goal state
        plt.plot(self._goal_state[0], self._goal_state[1], color = 'green', marker = 'o')

        # Set the plot boundaries to the configured size
        plt.xlim(self._xspace)
        plt.ylim(self._yspace)

        plt.show()