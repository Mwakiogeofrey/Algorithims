class Graph:
    """Representation of a simple graph using an adjacency map"""

    def __init__(self, directed=False):
        """create an empty graph (undirected by default)
        Graph is dirrected if optional parameter is set to True"""

        self._outgoing = {}
        #Only create second map for directed graphs; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected
        Property is based on the original declaration of the graph, not its content"""
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        """Return the number of vertices in the graphs """
        return len(self._outgoing)
    
    def vertices(self):
        """Return an iteration of all vertices of the graph"""
        return self._outgoing.keys()
    
    def edge_count(self):
        """Return the number of edges in the graph"""
        total = sum(len(self.outgoing[v]) for v in self._outgoing)
        return total if self.is_dirrected() else total // 2
    
    def edges(self):
        """Return a set of all edges of the graph"""
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
            return result
        
    def get_edge(self, u, v):
        """Return the edge from u to v or None if not adjacent"""
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        """Return number of outgoing edges incident to vertex v in the graph 
        if graph is directed, optional parameter used to count incoming edges"""
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])
    
    def incident_edges(self, v, outgoing=True):
        """Return all outgoing edges incident to vertex v in the graph
        If graph is directed, optional parameter used to request incoming edges"""
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new vertex with element x"""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
            if self.is_directed():
                self._incoming[v] = {}
                return v
            
    def insert_edge(self, u, v, x=None):
        """Insert and return a new edge from u to v with auxiliary element x"""
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
