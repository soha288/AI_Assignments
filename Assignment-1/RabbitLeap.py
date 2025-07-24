from collections import deque

# Start and Goal states
start_state = "EEE_WWW"
goal_state = "WWW_EEE"

# Function to generate valid next moves
def get_next_states(state):
    moves = []
    pos = state.index('_')  # Find the blank

    # 4 possible moves:
    if pos > 0 and state[pos - 1] == 'E':
        s = list(state)
        s[pos], s[pos - 1] = s[pos - 1], s[pos]
        moves.append("".join(s))

    if pos > 1 and state[pos - 2] == 'E':
        s = list(state)
        s[pos], s[pos - 2] = s[pos - 2], s[pos]
        moves.append("".join(s))

    if pos < 6 and state[pos + 1] == 'W':
        s = list(state)
        s[pos], s[pos + 1] = s[pos + 1], s[pos]
        moves.append("".join(s))

    if pos < 5 and state[pos + 2] == 'W':
        s = list(state)
        s[pos], s[pos + 2] = s[pos + 2], s[pos]
        moves.append("".join(s))

    return moves

# ------------------
# BFS Algorithm
# ------------------
def bfs(start):
    queue = deque()
    queue.append((start, [start]))  # (current_state, path)
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# ------------------
#  DFS Algorithm
# ------------------
def dfs(start):
    stack = []
    stack.append((start, [start]))  # (current_state, path)
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal_state:
            return path

        visited.add(state)

        for next_state in get_next_states(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))

    return None

# ------------------
# Run both BFS and DFS
# ------------------

print(" BFS Rabbit Leap Solution:")
bfs_solution = bfs(start_state)
if bfs_solution:
    for step in bfs_solution:
        print(step)
else:
    print("No solution found with BFS.")

print("\n DFS Rabbit Leap Solution:")
dfs_solution = dfs(start_state)
if dfs_solution:
    for step in dfs_solution:
        print(step)
else:
    print("No solution found with DFS.")

