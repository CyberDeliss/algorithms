"""
The task from LeetCode '1971. Find if Path Exists in Graph'

Example one:
    Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
    Output: true
    Explanation: There are two paths from vertex 0 to vertex 2:
    - 0 → 1 → 2
    - 0 → 2
Example two:
    Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
    Output: false
    Explanation: There is no path from vertex 0 to vertex 5.

Constraints:
    1 <= n <= 2 * 105
    0 <= edges.length <= 2 * 105
    edges[i].length == 2
    0 <= ui, vi <= n - 1
    ui != vi
    0 <= source, destination <= n - 1
    There are no duplicate edges.
    There are no self edges.

src = https://leetcode.com/problems/find-if-path-exists-in-graph/description/
"""


def valid_path(self, n: int, edges: list, source: int, destination: int) -> bool:
    visited_vertex: dict = {}

    paths_dict = get_paths_dict(edges)
    return bfs(paths_dict, source, destination, visited_vertex)


def dfs(paths_dict: dict, vertex: int, destination: int, visited_vertex: list) -> bool:
    if vertex == destination:
        return True
    if vertex in visited_vertex:
        return False

    visited_vertex.append(vertex)

    for neighbor in paths_dict[vertex]:
        if neighbor in visited_vertex:
            continue
        reached = dfs(paths_dict, neighbor, destination, visited_vertex)
        if reached:
            return True


def get_paths_dict(edges: list) -> dict:
    paths_dict = {}
    for vertex, goal in edges:
        if paths_dict.get(vertex):
            paths_dict[vertex].append(goal)
        else:
            paths_dict[vertex] = [goal]

        if paths_dict.get(goal):
            paths_dict[goal].append(vertex)
        else:
            paths_dict[goal] = [vertex]

    return paths_dict


def bfs(paths_dict: dict, vertex: int, destination: int, visited_vertex: dict) -> bool:
    if vertex == destination:
        return True
    queue = [vertex]
    visited_vertex[vertex] = True
    while len(queue) > 0:
        new_vertex = queue.pop()
        for neighbor in paths_dict[new_vertex]:
            if visited_vertex.get(neighbor):
                continue
            queue.append(neighbor)
            visited_vertex[neighbor] = True

            if neighbor == destination:
                return True
    return False
