
from collections import deque


class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def create_binary_tree(name):
    letters = [letter for letter in name.upper() if letter.isalpha()]

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


# DFS PREORDER: Root - Left - Right
def preorder(root):
    if root is None:
        return

    print(root.name, end=" ")
    preorder(root.left)
    preorder(root.right)


# DFS INORDER: Left - Root - Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.name, end=" ")
    inorder(root.right)


# DFS POSTORDER: Left - Right - Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.name, end=" ")


if __name__ == "__main__":

    name = input("Enter your name: ").strip()

    if name:
        root = create_binary_tree(name)

        print("\nBINARY TREE - DFS METHODS")

        print("\nPreorder Traversal: ", end="")
        preorder(root)

        print("\nInorder Traversal: ", end="")
        inorder(root)

        print("\nPostorder Traversal: ", end="")
        postorder(root)

        print()

    else:
        print("Please enter a name.")
