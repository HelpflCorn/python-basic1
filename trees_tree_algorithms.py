class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_node):
        self.children.remove(child_node)

    def insert_subtree(self, subtree):
        self.add_child(subtree)

    def remove_subtree(self, subtree):
        if subtree in self.children:
            self.remove_child(subtree)

    def display_tree(self):
        print(self.data)
        for child in self.children:
            print('---', end='')
            child.display_tree()


