
from collections import deque

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def create_binary_tree(name):
    letters = list(name.upper())

    if not letters:
        return None

    root = TreeNode(letters[0])
    queue = deque([root])
    index = 1

    while index < len(letters):
        current = queue.popleft()

        current.left = TreeNode(letters[index])
        queue.append(current.left)
        index += 1

        if index < len(letters):
            current.right = TreeNode(letters[index])
            queue.append(current.right)
            index += 1

    return root


def bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS Traversal: ", end="")

    while queue:
        node = queue.popleft()
        print(node.name, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print()


def dfs(root):
    if root is None:
        return

    print("DFS Traversal: ", end="")

    def preorder(node):
        if node:
            print(node.name, end=" ")
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    print()


if __name__ == "__main__":
    name = input("Enter your name: ").strip()

    if name:
        root = create_binary_tree(name)
        print("\nBINARY TREE")
        bfs(root)
        dfs(root)
    else:
        print("Please enter a name.")
