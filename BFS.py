GRAPH = {\
            'A': {'B': 140, 'C': 75, 'D': 118},\
            'B': {'A': 75, 'F': 71},\
            'C': {'D': 71, 'G': 151},\
            'D': {'A': 140, 'E': 151, 'F': 99, 'G': 80},\
            'E': {'A': 118, 'Lugoj': 111},\
            'F': {'D': 111, 'C': 70},\
            'G': {'A': 70, 'A': 75},\
            'H': {'F': 75, 'C': 120},\
        }

def bestfirst(source, destination):
    straight_line = {\
                        'A': 366,\
                        'B': 374,\
                        'C': 380,\
                        'D': 253,\
                        'E': 329,\
                        'F': 244,\
                        'G': 241,\
                        'H': 242,\
                    }
    from queue import PriorityQueue
    priority_queue, visited = PriorityQueue(), {}
    priority_queue.put((straight_line[source], 0, source, [source]))
    visited[source] = straight_line[source]
    while not priority_queue.empty():
        (heuristic, cost, vertex, path) = priority_queue.get()
        if vertex == destination:
            return heuristic, cost, path
        for next_node in GRAPH[vertex].keys():
            current_cost = cost + GRAPH[vertex][next_node]
            heuristic =  straight_line[next_node]
            if not next_node in visited or visited[next_node] >= heuristic:
                visited[next_node] = heuristic
                priority_queue.put((heuristic, current_cost,next_node, path + [next_node]))
def main():
    """Main function"""
    source = input("\nEnter Sourse:").strip().upper()
    goal = input("\nEnter Goal:").strip().upper()
    if source not in GRAPH or goal not in GRAPH:
        print('ERROR: CITY DOES NOT EXIST.')
    else:
               print('\nBFS PATH:')
               heuristic, cost, optimal_path = bestfirst(source, goal)
               print('PATH COST =', cost)
               print(' -> '.join(city for city in optimal_path))   
main()