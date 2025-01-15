class Event:
    def __init__(self, payload: dict):
        self.payload = payload

class OrderSubmittedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)

class OrderRejectedEvent(Event):
    def __init__(self, payload: dict):
        super().__init__(payload)

class Store:
    def __init__(self, name):
        self.name = name    
        self.inventory = {}
        self.queue = []

    def add_product(self, product_name, quantity):
            self.inventory[product_name] = self.inventory.get(product_name, 0) + quantity
    
    def submit_order(self, customer, product_name, quantity):
        if product_name in self.inventory and self.inventory[product_name] >= quantity:
            self.inventory[product_name] -= quantity
            event = OrderSubmittedEvent({"customer": customer.name, "product": product_name, "quantity": quantity})
            self.queue.append(event)
        else:
            event = OrderRejectedEvent({"customer": customer.name, "product": product_name, "reason": "Out of stock"})
            self.queue.append(event)

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            if isinstance(event, OrderSubmittedEvent):
                print(f"Order Submitted: {event.payload}")
            elif isinstance(event, OrderRejectedEvent):
                print(f"Order Rejected: {event.payload}")

    