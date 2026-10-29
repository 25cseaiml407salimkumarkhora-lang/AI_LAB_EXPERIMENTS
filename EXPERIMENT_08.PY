# TO IMPLEMENT THE WATER JUG PROBLEM USING BREADTH-FIRST SEARCH [BFS] IN PYTHON
   # AND FIND A SEQUENCE OF OPERATIONS TPO OBTAIN THE DESIRED
       # TARGET QUANTITY OF WATER.
       

from collections import deque

# Function to solve water jug problem using BFS
def water_jug(capacity1, capacity2, target):
    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:
        jug1, jug2, path = queue.popleft()

        # Skip if the state has already been visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Add current state to the path
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        # Generate all possible next states
        next_states = [

            # Fill Jug 1
            (capacity1, jug2),

            # Fill Jug 2
            (jug1, capacity2),

            # Empty Jug 1
            (0, jug2),

            # Empty Jug 2
            (jug1, 0),

            # Pour from Jug 1 to Jug 2
            (
                jug1 - min(jug1, capacity2 - jug2),
                jug2 + min(jug1, capacity2 - jug2)
            ),

            # Pour from Jug 2 to Jug 1
            (
                jug1 + min(jug2, capacity1 - jug1),
                jug2 - min(jug2, capacity1 - jug1)
            )
        ]

        # Add unvisited states to the queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    # No solution found
    return None


# Main Program
jug1 = int(input("Enter the capacity of Jug 1: "))
jug2 = int(input("Enter the capacity of Jug 2: "))
target = int(input("Enter the target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")