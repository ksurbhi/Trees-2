# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0.
        if root is None:
            return 0
        
        # Initialize the total sum to 0.
        self.sum = 0
        
        # Start the DFS traversal from the root with an initial current value of 0.
        self.dfs(root, 0)
        
        # Return the total sum of all root-to-leaf numbers.
        return self.sum
    
    def dfs(self, root: Optional[TreeNode], curr: int) -> None:
        # Base case: if the node is None, return.
        if root is None:
            return
        
        # Update the current number by appending the current node's value.
        curr = curr * 10 + root.val
        
        # If the current node is a leaf, add the current number to the total sum.
        if root.left is None and root.right is None:
            self.sum += curr
            return
        
        # Recur for the left and right subtrees.
        self.dfs(root.left, curr)
        self.dfs(root.right, curr)

# The time complexity of this algorithm is O(n), where n is the number of nodes in the tree.
# This is because each node is visited exactly once.

# The space complexity is O(h), where h is the height of the tree.
# In the worst case, for a skewed tree, the height h could be equal to n (number of nodes), resulting in O(n) space complexity.

        
