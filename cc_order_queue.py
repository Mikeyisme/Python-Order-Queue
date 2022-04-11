class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)
        
    def show_queue(self):
        print(self.items)

class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()


    def take_order(self, customer: str, flavor: str, scoops: int):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops
        if flavor not in self.flavors:
            print("Sorry, we don't have that flavor")
            return
        
        if scoops <=0 or scoops >3:
            print("Choose between 1-3")
            return

        if scoops >=1 or scoops <=3:
            print("Order created!")
            return

        order = {"customer": customer, "flavor": flavor, "scoops": scoops }

        self.orders.enqueue(order)
        print("Order created")
    
    def show_all_orders(self):
        print(self.orders)
        print("\n All pending Ice Cream Orders:")
            

    def next_order(self):
        self.orders.dequeue()


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()