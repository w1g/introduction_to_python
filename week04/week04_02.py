class Value:
    def __init__(self):
        self.value = None
        
    def __get__(self, instance, instance_type):
        return self.value
    
    def __set__(self, instance, amount):
        self.value = amount * (1 - instance.commission)
        


class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission