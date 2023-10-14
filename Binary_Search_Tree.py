class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursively(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursively(node.right, data)
        return node

    def print_tree(self):
        self._print_tree_recursively(self.root)

    def _print_tree_recursively(self, node, level=0, prefix="Root:"):
        if node is not None:
            print(" " * (level * 4) + f"{prefix} {node.data}")
            if node.left or node.right:
                self._print_tree_recursively(node.left, level + 1, "L---:")
                self._print_tree_recursively(node.right, level + 1, "R---:")

# Testing the BinarySearchTree
if __name__ == "__main__":
    numbers = [10, 5, 15, 3, 7, 12, 18]
    bst = BinarySearchTree()

    for num in numbers:
        bst.insert(num)

    bst.print_tree()
