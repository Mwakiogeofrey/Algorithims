### Graphs
A graph is away of representing relationships that exist between pairs of objects, a graph is a set of objcts called vertices, together with a collection of pairwise connection between them called edges.
Graphs have applications in modelling many domains including mapping, transportation, computer networks and electrical engineering
Edges from graphs are either directed or undirected. An edge (u,v) is said to be directed from u to v if the pair (u,v) is ordered, with u preceeding v. An edge (u,v) is said to be undirected if the pair (u,v) is not ordered 
A path is a sequence of alternating vertices and edges that starts at a vertex and ends at a vertex such that each edge is incident to its predecessor and successor vertex.
A cycle is a path that starts and ends at the same vertex, and that includes at least one edge
A directed graph is acyclic if it has no directed cycles 

## Breadth-first search
In this part you will learn how to model a network using a new abstract data structure: graphs
You learn dreadth-first search, an algorithm you can run on graph to answer questions like, "What is the shortest path to go to X"
You learn about directed versus undirected graphs
You learn topological sort, a different kind of algorithms that exposes dependencies between nodes.
Breadth-first search is a tpe of graph algorithm that allows you to find the shortest distance between two things,
Shortest distance can mean :
Wrtie a spellchecker(fewest edits from your misspelling to real word-for example, READED->READER is one edit)
Find the doctor closest to you in your network
Build a search engine crawleer
A graph models a set of connections, for example suppose you and your friends are playing a poker, and you want to model who owes whom money
Graphs are made up of nodes and edges
Those nodes are called in-neigbours or out-neighbors 
Arrow node pointing to another is in-neighbor and vice-versa

# Breadth-first search
It's a type of search algorithms that runs on graphs
points where arrows point to them but no arrows point from them to some other point is called a directed graph

