# Visualizer for graph-based search problems
# By Patrick Han
import matplotlib.pyplot as plt
import numpy as np

# TEMPORARY FILE : To be moved into our environment class


# Visualizer takes in:
# 1) a list of all the obstacles (each of which has their ordered vertices)
# 2) A tree/graph's root node

# Visualize by:
# 1) Plot all obsetacles using straight lines between ordered vertices
# 2) Traverse graph using BFS/DFS and plot nodes with connecting straight lines

class TreeNode:
    def __init__(self, val=None, children = None) -> None:
        """
        args:
            val: Object. Any state.
            children: List. List of TreeNodes which are neighbors
        """
        self._val = val
        self._nodes = [] + children


class Environment:
    def __init__(self):
        self.shape = [[0.0,0.0],[0.0,0.5],[0.7,0.5],[0.7,0.0]]
        self.shape2 = [[0.1,0.1],[0.1,0.4],[0.6,0.4],[0.6,0.1]]
        self.shape3 = [[1.2,1.2],[2,2.2],[3,1.2]]
        self._obstacles = []
        self._obstacles.append(self.shape)
        self._obstacles.append(self.shape2)
        self._obstacles.append(self.shape3)

        cc1 = TreeNode((0.6,0.6),[])
        cc2 = TreeNode((0.4,0.15),[])
        c1 = TreeNode((.1,.1),[cc1])
        c2 = TreeNode((.1,.2),[])
        c3 = TreeNode((.2,.1),[cc2])

        self._graph = TreeNode((0,0), [c1,c2,c3])
        self._xspace = (0, 3)
        self._yspace = (0, 3)
        

    def visualize(self):
        """
        Plots all obstacles and a built graph

        args:
            None
        """
        
        def plot_graph(head):
            for child in head._nodes:
                stack = np.array([head._val, child._val])
                plot_graph(child)
                plt.plot(stack[:,0], stack[:,1], color = 'red', marker = 'o')
            

        # Plot all obstacles 
        for obstacle in self._obstacles:
            # verts = np.array(obstacle._vertices)
            verts = np.array(obstacle)
            plt.plot(verts[:,0], verts[:,1], color = 'blue')
            plt.plot(verts[-1], verts[0], color ='blue') # Close off the shape


        # Plot the full graph/tree
        plot_graph(self._graph)

        # Set the plot boundaries to the configured size
        plt.xlim(self._xspace)
        plt.ylim(self._yspace)

        plt.show()


env = Environment()
env.visualize()