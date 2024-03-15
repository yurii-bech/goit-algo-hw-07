class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.key) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def right_rotate(y):
    x = y.left
    T3 = x.right

    x.right = y
    y.left = T3

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if key < root.left.key:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if key > root.right.key:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

def delete_node(root, key):
    if not root:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    if balance < -1:
        if get_balance(root.right) <= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root

# Function to find the largest value in the AVL tree. To find the largest value in the AVL tree, we need to traverse the tree to the rightmost node, as the largest value will be present in the rightmost leaf node
def find_largest_value(root):
    if root is None:
        return None

    current_node = root
    while current_node.right is not None:
        current_node = current_node.right

    return current_node.key

# Function to find the smallest value in the AVL tree. To find the smallest value in the AVL tree, we need to traverse the tree to the leftmost node, as the smallest value will be present in the leftmost leaf node
def find_smallest_value(root):
    if root is None:
        return None

    current_node = root
    while current_node.left is not None:
        current_node = current_node.left

    return current_node.key

# Function to find the sum of all the values in the AVL tree. To find the sum of all the values in the AVL tree, we can perform an in-order traversal of the tree and sum up the values of each node
def sum_of_values(root):
    if root is None:
        return 0

    # Recursive approach
    total_sum = root.key + sum_of_values(root.left) + sum_of_values(root.right)

    # Iterative approach
    # total_sum = 0
    # stack = [root]
    # while stack:
    #     node = stack.pop()
    #     total_sum += node.key
    #     if node.right:
    #         stack.append(node.right)
    #     if node.left:
    #         stack.append(node.left)

    return total_sum

# Driver program to test the above functions
root = None
keys = [10, 20, 30, 25, 28, 27, -1]

for key in keys:
    root = insert(root, key)
    print("Вставлено:", key)
    print("AVL-Дерево:")
    print(root)

# Delete
keys_to_delete = [10, 27]
for key in keys_to_delete:
    root = delete_node(root, key)
    print("Видалено:", key)
    print("AVL-Дерево:")
    print(root)

# Example of finding the largest value in the AVL tree
largest_value = find_largest_value(root)
print("Largest value in AVL tree:", largest_value)

# Example of finding the smallest value in the AVL tree
smallest_value = find_smallest_value(root)
print("Smallest value in AVL tree:", smallest_value)

# Example of finding the sum of all the values in the AVL tree
total_sum = sum_of_values(root)
print("Sum of all values in AVL tree:", total_sum)