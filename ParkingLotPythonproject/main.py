import heapq
from collections import defaultdict, OrderedDict
from car import Car
from parking_details import ParkingLot

print("Welcome to ParkingLot System")

parking_lot = ParkingLot(6)
print(parking_lot.available_parking_lots)

car = Car("KA-01-HH-1234", "White")
parking_lot.park_car(car)

car = Car("KA-01-HH-9999", "White")
parking_lot.park_car(car)

car = Car("KA-01-BB-0001", "Black")
parking_lot.park_car(car)

car = Car("KA-01-HH-7777", "Red")
parking_lot.park_car(car)

car = Car("KA-01-HH-2701", "Blue")
parking_lot.park_car(car)

car = Car("KA-01-HH-3141", "Black")
parking_lot.park_car(car)

# When no slots are available then
slot_no = parking_lot.get_nearest_slot()
print(slot_no)
slot_no = parking_lot.get_nearest_slot()
print(slot_no)

# Leave slot no 4
slot_no_to_be_freed = 4
parking_lot.free_slot(slot_no_to_be_freed)

heapq.heappush(parking_lot.available_parking_lots, 4)

car = Car("KA-01-P-333", "White")
parking_lot.park_car(car)

car = Car("DL-12-AA-9999", "White")
parking_lot.park_car(car)
parking_lot.status()
print(parking_lot.available_parking_lots)
print(parking_lot.registration_slot_mapping)
print(parking_lot.color_registration_mapping)

registration_numbers = parking_lot.get_registration_nos_by_color('White')
print("White : {}".format(registration_numbers))
registration_numbers = parking_lot.get_registration_nos_by_color('Red')
print("Red : {}".format(registration_numbers))
registration_numbers = parking_lot.get_registration_nos_by_color('Black')
print("Black : {}".format(registration_numbers))

slot_nos = parking_lot.get_slot_numbers_by_color('White')
print("White : {}".format(slot_nos))
slot_nos = parking_lot.get_slot_numbers_by_color('Red')
print("Red : {}".format(slot_nos))
slot_nos = parking_lot.get_slot_numbers_by_color('Black')
print("Black : {}".format(slot_nos))
parking_lot.status()
parking_lot.free_slot(1)
parking_lot.free_slot(2)
parking_lot.free_slot(3)
parking_lot.status()