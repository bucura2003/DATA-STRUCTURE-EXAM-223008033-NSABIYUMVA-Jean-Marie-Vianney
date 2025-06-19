Names: NSABIYUMVA Jean Marie Vianney
Reg No: 223008033
Module: OOP Final project exams
Lecturer: Prince Rukundo




PROJECT 87: Graph via Adjacency Lists


PROJECT OVERVIEW 

This project implements a graph representation using adjacency lists stored in dynamically allocated arrays. 
The graph supports directed and weighted types, demonstrating inheritance and polymorphism.


Implementation Details

The program is written in C++ and follows these key principles:
- Dynamic memory allocation for storing edges and vertices.
- Abstract base class (GraphBase) to enforce a common interface.
- Derived classes (DirectedGraph and WeightedGraph) to demonstrate inheritance.
- Pointer arithmetic for adjacency list traversal.
- Resizing arrays dynamically for adding/removing vertices.


Code Explanation (Line by Line)


1. Include Necessary Libraries

#include <iostream>
#include <vector>

- Enables input/output operations (std::cout for printing).
- Provides dynamic array (std::vector) for storing vertices.

2. Define the Edge Structure

struct Edge {
    int to;        // Destination vertex
    float weight;  // Edge weight
};

- Represents an edge in the graph.
- Stores destination vertex ID and edge weight.

3. Define the Vertex Structure

struct Vertex {
    int id;        // Vertex identifier
    Edge* edges;   // Dynamically allocated array of edges
    int edgeCount; // Number of edges

    Vertex(int id) : id(id), edges(nullptr), edgeCount(0) {}
};

- Represents a graph node.
- Stores vertex ID and dynamically allocated edges.

4. Add an Edge to a Vertex

void addEdge(int to, float weight) {
    Edge* newEdges = new Edge[edgeCount + 1]; // Resize dynamically
    for (int i = 0; i < edgeCount; i++) {
        newEdges[i] = edges[i]; // Copy existing edges
    }
    newEdges[edgeCount] = {to, weight}; // Add new edge
    delete[] edges; // Free old memory
    edges = newEdges;
    edgeCount++;
}

- Dynamically resizes the edge array.
- Copies existing edges and adds a new edge.

5. Destructor for Vertex

~Vertex() {
    delete[] edges; // Clean up dynamically allocated memory
};

- Ensures memory cleanup when a vertex is deleted.

6. Define the Abstract Base Class GraphBase

class GraphBase {
public:
    virtual void addEdge(int from, int to, float weight) = 0; // Pure virtual function
    virtual ~GraphBase() {}
};

- Defines a base class for all graph types.
- Forces derived classes to implement addEdge.

7. Define the DirectedGraph Class

class DirectedGraph : public GraphBase {
private:
    std::vector<Vertex*> vertices;

public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v = findOrCreateVertex(from);
        v->addEdge(to, weight);
    }
};

- Implements directed graph functionality.

8. Find or Create a Vertex

Vertex* findOrCreateVertex(int id) {
    for (Vertex* v : vertices) {
        if (v->id == id) return v;
    }
    Vertex* newVertex = new Vertex(id);
    vertices.push_back(newVertex);
    return newVertex;
};

- Searches for an existing vertex or creates a new one.

9. Destructor for DirectedGraph

~DirectedGraph() {
    for (Vertex* v : vertices) delete v;
};

- Deletes all vertices to prevent memory leaks.

10. Define the WeightedGraph Class

class WeightedGraph : public GraphBase {
private:
    std::vector<Vertex*> vertices;

public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v = findOrCreateVertex(from);
        v->addEdge(to, weight);
    }
};

- Implements weighted graph functionality.

11. Destructor for WeightedGraph

~WeightedGraph() {
    for (Vertex* v : vertices) delete v;
};

- Deletes all vertices to prevent memory leaks.

12. Main Function

int main() {
    GraphBase* graphs[2]; // Dynamic graph storage
    graphs[0] = new DirectedGraph();
    graphs[1] = new WeightedGraph();

    graphs[0]->addEdge(1, 2, 0);  // Directed edge
    graphs[1]->addEdge(1, 2, 3.5); // Weighted edge

    delete graphs[0];
    delete graphs[1];

    return 0;
};

- Creates directed and weighted graphs dynamically.
- Adds edges and deletes graphs to free memory.


Expected Output

Directed Graph:
Vertex 1 -> [2 (weight: 0)]

Weighted Graph:
Vertex 1 -> [2 (weight: 3.5)]



