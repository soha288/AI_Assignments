## Test Case Outputs
--- Testing Grid 1 ---
### Example 1: `grid = [[0, 1], [1, 0]]`

Best First Search
Path length: 2, Path: [(0, 0), (1, 1)]

A* Search
Path length: 2, Path: [(0, 0), (1, 1)]

--- Testing Grid 2 ---
### Example 2: `grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]`

Best First Search
Path length: 4, Path: [(0, 0), (0, 1), (1, 2), (2, 2)]

A* Search
Path length: 4, Path: [(0, 0), (0, 1), (1, 2), (2, 2)]

--- Testing Grid 3 ---
### Example 3: `grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]`

Best First Search
Path length: -1, Path: []

A* Search
Path length: -1, Path: []

## Algorithm Comparison

The main difference between Best-First Search and A* Search is how "smart" they are. 
Best-First Search is basically a greedy, optimistic algorithm. 
At every step, it only looks at the estimated distance to the finish line (the heuristic) 
and picks the path that looks closest. It completely ignores how long of a path it has already taken to get there. 
This makes it really fast in simple mazes where the direct path is the best one. 
However, its greedy nature is also its biggest flaw; it can easily be tricked into taking a path that 
seems short at first but leads to a long, dead-end, ultimately giving you a longer route than necessary.

On the other hand, A* Search is the smarter, more careful version. 
It's more balanced because it considers two things at every step: the distance it has already 
traveled (g-score) and the estimated distance to the goal (h-score). By combining these, 
A* gets a much more accurate picture of the total path length. This guarantees that it will always 
find the absolute shortest path. The only downside is that this "smarter" thinking requires more work. 
A* often has to explore more options and uses more memory to keep track of costs, which can make 
it a bit slower than the simple Best-First approach, especially on bigger grids.

Basically, you'd choose Best-First when you need a fast, "good enough" answer and are okay with it not being perfect.
You choose A* when you absolutely need the shortest possible path and are willing to let the computer work 
a little harder to find it.
