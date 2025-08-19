import math

# A function to guess the distance from a cell to the goal.
# We use the (Euclidean distance).
def calculate_heuristic(cell, goal):
    x1, y1 = cell
    x2, y2 = goal
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# this function gives all valid neighbors of a cell.
def get_neighbors(cell, grid_size):
    x, y = cell
    all_neighbors = []
    # Loop through all 8 possible directions (including diagonals)
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            # Skip the cell itself
            if dx == 0 and dy == 0:
                continue

            neighbor_x, neighbor_y = x + dx, y + dy

            # Check if the neighbor is within the grid size
            if 0 <= neighbor_x < grid_size and 0 <= neighbor_y < grid_size:
                all_neighbors.append((neighbor_x, neighbor_y))
    return all_neighbors

# A function to trace back the path from the goal to the start.
def reconstruct_path(came_from, current_cell):
    path = []
    # Start with the goal cell
    while current_cell is not None:
        path.append(current_cell)
        # Move to the cell that came before it
        current_cell = came_from.get(current_cell)
    
    # The path is from goal to start, so we reverse it
    path.reverse()
    return path

# --- Best-First Search (The "Greedy" one) ---
def best_first_search(grid):
    n = len(grid)
    start_node = (0, 0)
    goal_node = (n - 1, n - 1)

    # Check if start or end is a wall (1)
    if grid[start_node[0]][start_node[1]] == 1 or grid[goal_node[0]][goal_node[1]] == 1:
        return -1, []

    # A list of nodes we plan to visit.
    # We store tuples of (heuristic_score, node) so we can sort by the score.
    nodes_to_visit = [(calculate_heuristic(start_node, goal_node), start_node)]
    
    # A dictionary to remember which node came before another, to rebuild the path.
    # We set the start node's parent to None because nothing came before it.
    path_history = {start_node: None}
    
    # A set to keep track of nodes we've already visited.
    visited_nodes = {start_node}

    while len(nodes_to_visit) > 0:
        # Sort the list by the heuristic score (the first item in the tuple).
        nodes_to_visit.sort()
        
        # Get the node with the smallest heuristic score and remove it from the list.
        _, current_node = nodes_to_visit.pop(0)

        # If we reached the goal, we are done!
        if current_node == goal_node:
            path = reconstruct_path(path_history, current_node)
            return len(path), path

        # Check all neighbors of the current node
        for neighbor in get_neighbors(current_node, n):
            # If the neighbor is not a wall and we haven't visited it yet
            if grid[neighbor[0]][neighbor[1]] == 0 and neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                path_history[neighbor] = current_node # Remember we came from current_node
                
                # Add the neighbor to our list of nodes to visit
                heuristic_score = calculate_heuristic(neighbor, goal_node)
                nodes_to_visit.append((heuristic_score, neighbor))
                
    # If the loop finishes and we never found the goal, no path exists.
    return -1, []

# --- A* Search (The "Smart" one) ---
def a_star_search(grid):
    n = len(grid)
    start_node = (0, 0)
    goal_node = (n - 1, n - 1)
    
    if grid[start_node[0]][start_node[1]] == 1 or grid[goal_node[0]][goal_node[1]] == 1:
        return -1, []

    # g_score: The actual cost (number of steps) from the start to a node.
    g_score = { (x,y): float('inf') for x in range(n) for y in range(n) }
    g_score[start_node] = 0

    # f_score: The total estimated cost (g_score + heuristic).
    f_score = { (x,y): float('inf') for x in range(n) for y in range(n) }
    f_score[start_node] = calculate_heuristic(start_node, goal_node)
    
    # A list of nodes we plan to visit, sorted by f_score.
    nodes_to_visit = [(f_score[start_node], start_node)]
    
    # A dictionary to remember the path.
    path_history = {start_node: None}

    while len(nodes_to_visit) > 0:
        # Sort the list by the f_score to get the most promising node.
        nodes_to_visit.sort()
        
        # Get the node with the lowest f_score.
        _, current_node = nodes_to_visit.pop(0)

        if current_node == goal_node:
            path = reconstruct_path(path_history, current_node)
            return len(path), path

        for neighbor in get_neighbors(current_node, n):
            # Check if the neighbor is a wall
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue

            # Calculate the cost to get to this neighbor (g_score).
            # It's the cost to the current node plus 1.
            tentative_g_score = g_score[current_node] + 1
            
            # If we found a shorter path to this neighbor
            if tentative_g_score < g_score[neighbor]:
                # Update the path and scores for this neighbor
                path_history[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + calculate_heuristic(neighbor, goal_node)
                
                # Add the neighbor to our list of nodes to visit
                nodes_to_visit.append((f_score[neighbor], neighbor))

    return -1, []

# --- Function to run and print results ---
def solve(grid):
    print("Best First Search")
    bfs_len, bfs_path = best_first_search(grid)
    print(f"Path length: {bfs_len}, Path: {bfs_path}")
    
    print("\nA* Search")
    astar_len, astar_path = a_star_search(grid)
    print(f"Path length: {astar_len}, Path: {astar_path}")

# --- Grid definitions and function calls ---

# Example 1 Input
grid1 = [
    [0, 1],
    [1, 0]
]

# Example 2 Input
grid2 = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

# Example 3 Input
grid3 = [
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]

# --- Run the algorithms on all grids ---
print("--- Testing Grid 1 ---")
solve(grid1)
print("\n--- Testing Grid 2 ---")
solve(grid2)
print("\n--- Testing Grid 3 ---")
solve(grid3)
