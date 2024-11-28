# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/11/28

# Node class to represent each node in the binary tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Function to insert nodes in the binary tree using level-order traversal
def build_tree(values):
    if not values or values[0] == -1:
        return None
    
    root = Node(values[0])  
    queue = [root]  # Start with the root in the queue
    i = 1
    
    # Using level-order traversal to insert nodes
    while i < len(values):
        current = queue.pop(0)
        
        if values[i] != -1:
            current.left = Node(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] != -1:
            current.right = Node(values[i])
            queue.append(current.right)
        i += 1
        
    return root

# Function to calculate the diameter of the binary tree
def diameter(root):
    # Helper function to calculate height and diameter
    def height_and_diameter(node):
        # Base case: If the node is None, return height 0 and diameter 0
        if not node:
            return 0, 0
        
        # Recursively calculate the height and diameter of left and right subtrees
        left_height, left_diameter = height_and_diameter(node.left)
        right_height, right_diameter = height_and_diameter(node.right)
        
        # Current height is the maximum of left and right subtrees' heights + 1 (for the current node)
        current_height = max(left_height, right_height) + 1
        
        # Current diameter is the sum of left and right heights (edges between the nodes)
        current_diameter = left_height + right_height
        
        # The overall diameter is the maximum of the current diameter and the diameters of the left and right subtrees
        max_diameter = max(left_diameter, right_diameter, current_diameter)
        
        return current_height, max_diameter
    
    # Start the recursion from the root and calculate the diameter
    _, diameter_value = height_and_diameter(root)
    return diameter_value + 1  # Add 1 to account for the number of nodes, not edges

# Main function to interact with the user
def main():
    # Input(separated by spaces)
    input_values = list(map(int, input("Enter the level-order traversal of the binary tree (use -1 for null nodes): ").split()))
    
    # Build the binary tree
    root = build_tree(input_values)
    
    # Calculate and print the diameter
    result = diameter(root)
    print(result)

# Calling the main function
if __name__ == "__main__":
    main()
