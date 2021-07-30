import heapq
from collections import defaultdict, OrderedDict

class ParkingLot:
    def __init__(self, total_slots):
        self.registration_slot_mapping = dict()
        self.color_registration_mapping = defaultdict(list)
        # we need to maintain the orders of cars while showing 'status'
        self.slot_car_mapping = OrderedDict()

        # initialize all slots as free
        self.available_parking_lots = []
        # Using min heap as this will always give minimun slot number in O(1) time
        for i in range(1, total_slots + 1):
            heapq.heappush(self.available_parking_lots, i)

    def status(self):
        print("Slot No.  Registration No  Colour")
        for slot, car in self.slot_car_mapping.items():
            print("{}         {}    {}".format(slot, car.registration_number, car.color))
        return True

    def get_nearest_slot(self):
        return heapq.heappop(self.available_parking_lots) if self.available_parking_lots else None

    def free_slot(self, slot_to_be_freed):
        found = None
        for registration_no, slot in self.registration_slot_mapping.items():
            if slot == slot_to_be_freed:
                found = registration_no

        # Cleanup from all cache
        if found:
            del self.registration_slot_mapping[found]
            car_to_leave = self.slot_car_mapping[slot_to_be_freed]
            self.color_registration_mapping[car_to_leave.color].remove(found)
            del self.slot_car_mapping[slot_to_be_freed]
            print("leave ", slot_to_be_freed)
        else:
            print("slot is not in use")

    def park_car(self, car):
        slot_no = self.get_nearest_slot()
        if slot_no is None:
            print("Sorry, parking lot is full")
            return
        self.slot_car_mapping[slot_no] = car
        self.registration_slot_mapping[car.registration_number] = slot_no
        self.color_registration_mapping[car.color].append(car.registration_number)

    # ● Registration numbers of all cars of a particular colour.
    def get_registration_nos_by_color(self, color):
        return self.color_registration_mapping[color]

    # ● Slot numbers of all slots where a car of a particular colour is parked.
    def get_slot_numbers_by_color(self, color):
        return [self.registration_slot_mapping[reg_no] for reg_no in self.color_registration_mapping[color]]


