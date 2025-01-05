class TreeNode:
    def __init__(self, name, data=None):
        self.name = name  
        self.data = data 
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        indent = " " * (level * 4)
        print(f"{indent}{self.name}: {self.data if self.data else ''}")
        for child in self.children:
            child.display(level + 1)


if __name__ == "__main__":
    
    root = TreeNode("Real Estate")

    
    residential = TreeNode("Residential")
    commercial = TreeNode("Commercial")

    root.add_child(residential)
    root.add_child(commercial)

    residential.add_child(TreeNode("B Lounge Hotel", {"price": 1200000, "location": "KICIKIRO"}))
    residential.add_child(TreeNode("Coppenhagen Kicukiro", {"price": 500000, "location": "KICUKIRO"}))

    
    commercial.add_child(TreeNode("CHIC Building", {"price": 2000000, "location": "Nyarugenge"}))
    commercial.add_child(TreeNode("Retail Store", {"price": 1500000, "location": "Nyabugogo"}))

   
    root.display()
