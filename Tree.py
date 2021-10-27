# Implements Tree
# By: Vishnu Devarakonda

class TreeNode:
    def __init__(self, val = None, children = []) -> None:
        """
        args:
            val: Object. Any state.
            children: List. List of TreeNodes which are neighbors
        """
        self._val = val
        self._nodes = [] + children