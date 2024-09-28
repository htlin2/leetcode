class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Step 1: Build graph using adjacency list with min-heaps
        graph = defaultdict(list)
        
        # Populate the graph with sorted destination airports
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)
        
        itinerary = []

        # Step 2: Define the DFS function
        def dfs(airport):
            # Explore all destinations from the current airport in lexical order
            while graph[airport]:
                next_airport = heapq.heappop(graph[airport])
                dfs(next_airport)
            # Add the airport to itinerary once all its paths are visited
            itinerary.append(airport)
        
        # Step 3: Start DFS from "JFK"
        dfs("JFK")
        
        # Since we append the airports post DFS traversal, reverse the list at the end
        return itinerary[::-1]


"""
graph + backtracking
build adj -> value list need to be sorted
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
{
    muc: [lhr]
    jfk: [muc]
    sfo, [sjc]
    lhr: [sfo]
}
jfk -> muc -> lhr -> sfo -> sjc


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
{
    jfk: [atl, sfo],
    sfo: [atl],
    atl: [jfk, sfo],
}


"""