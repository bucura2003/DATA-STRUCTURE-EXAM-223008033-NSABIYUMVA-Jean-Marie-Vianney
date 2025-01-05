def bubble_sort(data, key):
   
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][key] > data[j + 1][key]:
                
                data[j], data[j + 1] = data[j + 1], data[j]


if __name__ == "__main__":
    
    auction_data = [
        {"id": 1, "OG2TONE": "Kaizen Hotel", "priority": 3, "price": 1200000},
        {"id": 2, "SLUMP GOD": "Modern Apartment", "priority": 1, "price": 800000},
        {"id": 3, "KEN CARSON": "Cozy Cottage", "priority": 5, "price": 500000},
        {"id": 4, "DESTROY LONELY": "Office Space", "priority": 2, "price": 2000000},
        {"id": 5, "KIVUMBI KING": "Retail Store", "priority": 4, "price": 1500000},
    ]

    print("Before Sorting:")
    for item in auction_data:
        print(item)

    
    bubble_sort(auction_data, key="priority")

    print("\nAfter Sorting by Priority:")
    for item in auction_data:
        print(item)
