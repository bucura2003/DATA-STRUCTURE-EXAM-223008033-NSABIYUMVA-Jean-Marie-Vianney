class BSTNode:
    def __init__(self, key, data):
        self.key = key  
        self.data = data  
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 1
        self.max_size = None

    def set_max_size(self, max_size):
        self.max_size = max_size

    def insert(self, key, data):
        if self.max_size is not None and self.size >= self.max_size:
            print("Maximum size reached. Cannot add more orders.")
            return False
        if self.root is None:
            self.root = BSTNode(key, data)
        else:
            self._insert(self.root, key, data)
        self.size += 1
        return True

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, data)
            else:
                self._insert(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, data)
            else:
                self._insert(node.right, key, data)
        else:
            print(f"Order with key {key} already exists.")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        if deleted:
            self.size -= 1
        return deleted

    def _delete(self, node, key):
        if node is None:
            return node, False

        if key < node.key:
            node.left, deleted = self._delete(node.left, key)
        elif key > node.key:
            node.right, deleted = self._delete(node.right, key)
        else:
           
            if node.left is None:
                return node.right, True
            elif node.right is None:
                return node.left, True
           
            successor = self._min_value_node(node.right)
            node.key, node.data = successor.key, successor.data
            node.right, _ = self._delete(node.right, successor.key)
            return node, True

        return node, False

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        if node is not None:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.data))
            self._inorder_traversal(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.set_max_size(5)  

    bst.insert(101, {"NSABIYUMVA": "Order A", "price": 100000})
    bst.insert(102, {"RIRIMBA": "Order B", "price": 200000})
    bst.insert(103, {"RUKUNDO": "Order C", "price": 150000})
    bst.insert(104, {"MAMILLA": "Order D", "price": 250000})
    bst.insert(105, {"DIVINE": "Order E", "price": 300000})
    

    print("Inorder Traversal (All Orders):", bst.inorder_traversal())

    
    bst.insert(106, {"name": "Order F", "price": 350000})

    
    order = bst.search(102)
    print("Search for Order 102:", order)

    
    bst.delete(103)
    print("Inorder Traversal after deleting Order 103:", bst.inorder_traversal())
