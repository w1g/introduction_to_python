import csv
import os

class Vehicle:    
    def __init__(self, brand, photo, carrying):
        self.brand = brand
        self.photo_file_name = photo
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[-1]


class Car(Vehicle):
    def __init__(self, brand, photo, carrying, passenger_seats):
        super().__init__(brand, photo, carrying)
        self.car_type = 'car'
        self.passenger_seats_count = passenger_seats



class Truck(Vehicle):
    def __init__(self, brand, photo, carrying, whl):
        super().__init__(brand, photo, carrying)
        self.car_type = 'truck'
        self.body_width, self.body_height, self.body_length = whl
    
    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(Vehicle):
    def __init__(self, brand, photo, carrying, extra):
        super().__init__(brand, photo, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra
    


def get_car_list(csv_file_path):
    try:
        car_list = []
        with open(csv_file_path, 'r') as f:
            reader = csv.DictReader(f, delimiter=';')
            
            for row in reader:
                if row['car_type'] == 'car':
                    car_list.append(Car(row['brand'], row['photo_file_name'], float(row['carrying']), int(row['passenger_seats_count'])))
                    
                if row['car_type'] == 'truck':
                    try:
                        whl = [float(i) for i in row['body_whl'].split('x')]
                    except:
                        whl = (0, 0, 0)
                    car_list.append(Truck(row['brand'], row['photo_file_name'], float(row['carrying']), whl))
                
                if row['car_type'] == 'spec_machine':
                    car_list.append(SpecMachine(row['brand'], row['photo_file_name'], float(row['carrying']), row['extra']))
        
        return car_list
    
    except OSError as err:
        print(err.errno, err.strerror)