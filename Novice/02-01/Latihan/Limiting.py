class Bus(object):
     passengers = set()
     def add_passenger(self, person):
        self.passengers.add(person)

bus1 = Bus()
bus2 = Bus()
bus1.add_passenger('abe')
bus2.add_passenger('bertha')
print(bus1.passengers) # returns ['abe', 'bertha']
print(bus2.passengers)  # also ['abe', 'bertha']