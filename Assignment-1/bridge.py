from collections import deque

# Time taken by each person
times = {
    'A1': 5,    # Amogh
    'A2': 10,   # Ameya
    'Gm': 20,   # Grandmother
    'Gf': 25    # Grandfather
}

# Define goal condition
def is_goal(state):
    left, right, umbrella, time = state
    return len(left) == 0 and time <= 60

# Function to generate next valid states
def get_next_states(state):
    left, right, umbrella, time = state
    states = []

    if umbrella == 'left':
        people = list(left)
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                p1, p2 = people[i], people[j]
                move_time = max(times[p1], times[p2])
                new_time = time + move_time
                if new_time <= 60:
                    new_left = set(left) - {p1, p2}
                    new_right = set(right) | {p1, p2}
                    new_state = (tuple(new_left), tuple(new_right), 'right', new_time)
                    states.append(new_state)
    else:
        people = list(right)
        for p in people:
            move_time = times[p]
            new_time = time + move_time
            if new_time <= 60:
                new_left = set(left) | {p}
                new_right = set(right) - {p}
                new_state = (tuple(new_left), tuple(new_right), 'left', new_time)
                states.append(new_state)

    return states

# --------------------
#  BFS Function
# --------------------
def bfs(start):
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        current, path = queue.popleft()
        left, right, umbrella, time = current

        key = (tuple(sorted(left)), tuple(sorted(right)), umbrella)
        if key in visited:
            continue
        visited.add(key)

        if is_goal(current):
            print(" BFS Solution found in", time, "minutes!\n")
            for step in path:
                print(step)
            return

        for next_state in get_next_states(current):
            queue.append((next_state, path + [next_state]))

    print(" BFS: No solution found.")

# --------------------
#  DFS Function
# --------------------
def dfs(start):
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()
        left, right, umbrella, time = current

        key = (tuple(sorted(left)), tuple(sorted(right)), umbrella)
        if key in visited:
            continue
        visited.add(key)

        if is_goal(current):
            print(" DFS Solution found in", time, "minutes!\n")
            for step in path:
                print(step)
            return

        for next_state in get_next_states(current):
            stack.append((next_state, path + [next_state]))

    print(" DFS: No solution found.")


initial_state = (('A1', 'A2', 'Gm', 'Gf'), (), 'left', 0)

print(" Running BFS...")
bfs(initial_state)

print("\n Running DFS...")
dfs(initial_state)

