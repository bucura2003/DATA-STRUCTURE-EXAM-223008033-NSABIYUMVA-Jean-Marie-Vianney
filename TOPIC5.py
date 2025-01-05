class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, key):
        current = self.head
        prev = None
        while current and current.data.get("id") != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Item with ID {key} not found.")
            return False

        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next

        print(f"Item with ID {key} removed.")
        return True

    def display(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def search(self, key):
        current = self.head
        while current:
            if current.data.get("id") == key:
                return current.data
            current = current.next
        return None


if __name__ == "__main__":
    auction_list = LinkedList()

    
    auction_list.append({"id": 1, "name": "B lounge", "price": 1200000})
    auction_list.append({"id": 2, "name": "The Wave Hotel", "price": 800000})
    auction_list.append({"id": 3, "name": "Kaizen_Nyabugogo", "price": 500000})

    
    print("Auction Properties:", auction_list.display())

    
    property = auction_list.search(2)
    print("Search for property with ID 2:", property)

    
    auction_list.remove(3)
    print("Auction Properties after removal:", auction_list.display())
