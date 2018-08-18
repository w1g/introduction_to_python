import week_03_02
import sys

if __name__ == '__main__':
    
    path = sys.argv[1]
    
    l = week_03_02.get_car_list(path)
    
    for itm in l:
        print(f'{itm.car_type}, {itm.brand}, {itm.photo_file_name}, {itm.carrying}, {itm.get_photo_file_ext()}')