'''
Created on 2015. 12. 3.

@author: User
'''
10.2 The mechanical Internet
class Chappe:
"""
>>> network = Chappe(¡¯chappe.txt¡¯)
>>> network.neighbours(¡¯Lille¡¯)
{¡¯Paris¡¯, ¡¯Bruxelles¡¯, ¡¯Dunkerque¡¯, ¡¯Boulogne¡¯}
>>> network.neighbours(¡¯Paris¡¯)
{¡¯Tours¡¯, ¡¯Dreux¡¯, ¡¯Tonerre¡¯, ¡¯Lille¡¯}
>>> network.neighbours(¡¯Brest¡¯)
{¡¯St Brieux¡¯}
>>> network.neighbours(¡¯Londres¡¯)
Traceback (most recent call last):
AssertionError: city does not belong to network
>>> network.hubs(¡¯Lille¡¯, ¡¯Lille¡¯)
0
>>> network.hubs(¡¯Lille¡¯, ¡¯Tours¡¯)
2
>>> network.hubs(¡¯Lille¡¯, ¡¯Toulouse¡¯)
11
>>> network.hubs(¡¯Lille¡¯, ¡¯Montpellier¡¯)
9
>>> network.hubs(¡¯Lille¡¯, ¡¯Perpignan¡¯)
11
>>> network.hubs(¡¯Lille¡¯, ¡¯Marseille¡¯)
-1
>>> network.hubs(¡¯Lille¡¯, ¡¯Londres¡¯)
52
Traceback (most recent call last):
AssertionError: city does not belong to network
"""
def __init__(self, filename):
# intialize network
self._network = {}
# build network
for line in open(filename, ¡¯r¡¯, encoding=¡¯utf-8¡¯):
# line contains two cities, separated by a tab
city1, city2 = line.strip().split(¡¯\t¡¯)
# add city2 to collection of neighbours of city1
if city1 not in self._network:
self._network[city1] = set()
self._network[city1].add(city2)
# add city1 to collection of neighbours of city2
if city2 not in self._network:
self._network[city2] = set()
self._network[city2].add(city1)
def neighbours(self, city):
# check whether city belongs to network
assert city in self._network, ¡¯city does not belong to network¡¯
# lookup and return neighbours of given city
return self._network[city]
def hubs(self, city1, city2):
# check whether both cities belong to network
assert city1 in self._network, ¡¯city not in network¡¯
assert city2 in self._network, ¡¯city not in network¡¯
# if both cities are the same, the distance between them is 0 by
# definition
if city1 == city2:
return 0
# breadth-first traversal of all cities, starting from city1, until
# city2 is reached or complete subnetwork of city1 has been traversed
extension, shortestPath = [city1], {city1:0}
while extension:
# determine next city and its distance to city1 during breadt-first
# traversal of network
city = extension.pop(0)
distance = shortestPath[city]
# traverse each neighbour of next city
for neighbour in self.neighbours(city):
if neighbour == city2:
# found shortest path from city1 to city2
return distance + 1
elif neighbour not in shortestPath:
# add neighbour to queue that guides breadth-first traversal
# of subnetwork of city1
extension.append(neighbour)
# store shortest distance to neighbour in dictionary; this
53
# also avoids that path to neighbour is extended repeatedly
# if multiple paths lead into this neighbour
shortestPath[neighbour] = distance + 1
# entire subnetwork of city1 has been traversed, and no path has been
# found between city1 and city2
return -1
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
