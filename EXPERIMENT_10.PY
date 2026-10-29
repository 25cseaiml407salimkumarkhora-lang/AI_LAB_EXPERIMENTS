from itertools import permutations
def travelling_salesman(graph,start):
  cities = list(range(len(graph)))
  cities.remove(start)
  min_cost = float('inf')
  best_path = None
  for perm in permutations(cities):
    current_cost = 0
    current_path=[start]
    k=start
    for city in perm:
      current_cost += graph[k][city]
      current_path.append(city)
      k=city
    current_cost += graph[k][start]
    current_path.append(start)
    if current_cost < min_cost:
      min_cost = current_cost
      best_path = current_path
  return best_path,min_cost
n = int(input("Enter the number of cities: "))
print("enter the cost matrix:")
graph=[]
for i in range(n):
  row=list(map(int,input().split()))
  graph.append(row)
start=int(input("Enter the starting city(0 to {}): ".format(n-1)))
best_path,min_cost=travelling_salesman(graph,start)
print("The optimal path :",  " -> ".join(map(str,best_path)))
print("minimal cost:",min_cost)