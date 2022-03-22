# class City:
#
#     def __init__(self, name: str):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     def __repr__(self):
#         return f"{self.name}"
#
#
# class Road:
#
#     def __init__(self, name: str, start: City, end: City = None):
#         self._name = name
#         self._start = start
#         self._end = end
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def start(self):
#         return self._start
#
#     @property
#     def end(self):
#         return self._end
#
#     def __repr__(self):
#         return f"{self.__class__.__name__}-{self.name}-{self.start}->{self.end}"
#
#
# class Highway(Road):
#     def __init__(self, name: str, start: City, end: City = None):
#         super().__init__(name, start, end)
#
#
# class FirstClassRoad(Road):
#     def __init__(self, name, start, end: City = None):
#         super().__init__(name, start, end)
#
#
# class SecondClassRoad(Road):
#     def __init__(self, name, start, end: City = None):
#         super().__init__(name, start, end)
#
#
# class ThirdClassRoad(Road):
#     def __init__(self, name, start, end: City = None):
#         super().__init__(name, start, end)
#
#
# class Map:
#
#     def __init__(self, name):
#         self.name = name
#         self.cities = []
#         self.roads = {}  # start_city: {end_city:Road}
#
#     def add_city(self, new_city: City):
#         self.cities.append(new_city)
#
#     def add_connection(self, new_road: Road):
#         if new_road.start not in self.roads:
#             self.roads[new_road.start] = {}
#         self.roads[new_road.start][new_road.end] = new_road  # {'sofia': {'varna':Road()}}
#
#     def search_connection(self, start: City, end: City):
#         if start not in self.roads.keys():
#             return False
#
#         queue = [start]
#         visited = set()
#         while queue:
#             current_city = queue.pop(0)
#             visited.add(current_city)
#             next_cities = []
#
#             try:
#                 next_cities = [city for city in self.roads[current_city].keys() if city not in visited]
#             except:
#                 continue
#
#             if end in next_cities:
#                 return True
#             queue.extend(next_cities)
#
#         return False
#
#
# if __name__ == '__main__':
#     map_bulgaria = Map("Bulgaria")
#     varna = City('Varna')
#     sofia = City('Sofia')
#     burgas = City('Burgas')
#     ruse = City('Ruse')
#     dobrich = City('Dobrich')
#
#     a1 = Highway('a1', sofia, burgas)
#     a2 = Highway('a2', sofia, varna)
#     a3 = Highway('a3', varna, dobrich)
#     fc1 = FirstClassRoad('2', ruse, sofia)
#     fc2 = FirstClassRoad('3', varna, sofia)
#
#     map_bulgaria.add_city(sofia)
#     map_bulgaria.add_city(varna)
#     map_bulgaria.add_city(burgas)
#     map_bulgaria.add_city(ruse)
#     map_bulgaria.add_city(dobrich)
#     map_bulgaria.add_connection(a1)
#     map_bulgaria.add_connection(a2)
#     map_bulgaria.add_connection(a3)
#     map_bulgaria.add_connection(fc1)
#     map_bulgaria.add_connection(fc2)
#
#     print(map_bulgaria.roads)
#
#     print(map_bulgaria.search_connection(ruse, dobrich))
#
#     with open('file.txt', 'rt', encoding='utf-8') as f:
#         line = f.readline()
#         print(line)

import sys

if __name__ == '__main__':
    pass