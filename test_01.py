#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City


# assume getting data from database

states = storage.all(State)
# cities = storage.all(City)


for key, obj in states.items():
    print("key:", key)
    print("main:", obj)
    print("cities:", obj.cities)

# states_cities = []
# for state in states.values():
#     citys = []
#     for city in cities.values():
#         if city.state_id == state.id:
#             citys.append({city.id: city.name})
#     states_cities.append({state.id: {state.name: citys}})


# print(states_cities)

# states_cities = []
# for state in states.values():
#     for item in state.cities:
#         print(state.name, ':', item.name)