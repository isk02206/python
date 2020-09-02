'''
Created on 2015. 12. 3.

@author: User
'''
9.4 The mechanical Internet
def network(filename):
"""
>>> chappe = network(¡¯chappe.txt¡¯)
>>> chappe[¡¯Lille¡¯]
{¡¯Paris¡¯, ¡¯Bruxelles¡¯, ¡¯Dunkerque¡¯, ¡¯Boulogne¡¯}
>>> chappe[¡¯Paris¡¯]
{¡¯Tours¡¯, ¡¯Dreux¡¯, ¡¯Tonerre¡¯, ¡¯Lille¡¯}
>>> chappe[¡¯Brest¡¯]
{¡¯St Brieux¡¯}
"""
# initialize network
network = {}
# build network
for line in open(filename, ¡¯r¡¯, encoding=¡¯utf-8¡¯):
46
# line contains two cities, separated by a tab
city1, city2 = line.strip().split(¡¯\t¡¯)
# add city2 to collection of neighbours of city1
if city1 not in network:
network[city1] = set()
network[city1].add(city2)
# add city1 to collection of neighbours of city2
if city2 not in network:
network[city2] = set()
network[city2].add(city1)
# return network
return network
def hubs(city1, city2, network):
"""
>>> chappe = network(¡¯chappe.txt¡¯)
>>> hubs(¡¯Lille¡¯, ¡¯Lille¡¯, chappe)
0
>>> hubs(¡¯Lille¡¯, ¡¯Tours¡¯, chappe)
2
>>> hubs(¡¯Lille¡¯, ¡¯Toulouse¡¯, chappe)
11
>>> hubs(¡¯Lille¡¯, ¡¯Montpellier¡¯, chappe)
9
>>> hubs(¡¯Lille¡¯, ¡¯Perpignan¡¯, chappe)
11
>>> hubs(¡¯Lille¡¯, ¡¯Marseille¡¯, chappe)
-1
>>> hubs(¡¯Lille¡¯, ¡¯Londres¡¯, chappe)
Traceback (most recent call last):
AssertionError: city not in network
"""
# check whether both cities belong to network
assert city1 in network and city2 in network, ¡¯city not in network¡¯
# if both cities are the same, the distance between them is 0 by definition
if city1 == city2:
return 0
# breadth-first traversal of all cities, starting from city1, until city2
# is reached or complete subnetwork of city1 has been traversed
extension, shortestPath = [city1], {city1:0}
while extension:
# determine next city and its distance to city1 during breadth-first
# traversal of network
city = extension.pop(0)
distance = shortestPath[city]
# traverse each neighbour of next city
for neighbour in network[city]:
if neighbour == city2:
# found shortest path from city1 to city2
return distance + 1
elif neighbour not in shortestPath:
# add neighbour to queue that guides breadth-first traversal
# of subnetwork of city1
extension.append(neighbour)
47
# store shortest distance to neighbour in dictionary; this also
# avoids that path to neighbour is extended repeatedly if
# multiple paths lead into this neighbour
shortestPath[neighbour] = distance + 1
# entire subnetwork of city1 has been traversed, and no path has been found
# between city1 and city2
return -1
if __name__ == ¡¯__main__¡¯:
import doctest
doctest.testmod()
