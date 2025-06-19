#include <iostream>
using namespace std;

struct Edge {
    int to;
    float weight;
};

struct Vertex {
    int id;
    Edge* edges;
    int edgeCount;

    Vertex() {
        id = -1;
        edges = NULL;
        edgeCount = 0;
    }

   
    void addEdge(int to, float weight) {
        Edge* newEdges = new Edge[edgeCount + 1];
        for (int i = 0; i < edgeCount; ++i) {
            *(newEdges + i) = *(edges + i);
        }
        *(newEdges + edgeCount) = createEdge(to, weight); 
        delete[] edges;
        edges = newEdges;
        edgeCount++;
    }

    Edge createEdge(int to, float weight) {
        Edge e;
        e.to = to;
        e.weight = weight;
        return e;
    }

    void printEdges() {
        cout << "Vertex " << id << ":";
        for (int i = 0; i < edgeCount; ++i) {
            cout << " -> (" << edges[i].to << ", w=" << edges[i].weight << ")";
        }
        cout << endl;
    }

    ~Vertex() {
        delete[] edges;
    }
};


class GraphBase {
public:
    virtual void addVertex(int id) = 0;
    virtual void removeVertex(int id) = 0;
    virtual void addEdge(int from, int to, float weight) = 0;
    virtual void display() = 0;
    virtual ~GraphBase() {}
};

class DirectedGraph : public GraphBase {
protected:
    Vertex* vertices;
    int vertexCount;

public:
    DirectedGraph() {
        vertices = NULL;
        vertexCount = 0;
    }

    void addVertex(int id) {
        Vertex* newVertices = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; ++i) {
            newVertices[i] = vertices[i];
        }
        newVertices[vertexCount].id = id;
        delete[] vertices;
        vertices = newVertices;
        vertexCount++;
    }

    void removeVertex(int id) {
        int index = -1;
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == id) {
                index = i;
                break;
            }
        }

        if (index == -1) return;

        Vertex* newVertices = new Vertex[vertexCount - 1];
        for (int i = 0, j = 0; i < vertexCount; ++i) {
            if (i != index) {
                newVertices[j++] = vertices[i];
            }
        }

        delete[] vertices[index].edges;
        delete[] vertices;
        vertices = newVertices;
        vertexCount--;
    }

    void addEdge(int from, int to, float weight) {
        for (int i = 0; i < vertexCount; ++i) {
            if (vertices[i].id == from) {
                vertices[i].addEdge(to, weight);
                break;
            }
        }
    }

    void display() {
        for (int i = 0; i < vertexCount; ++i) {
            vertices[i].printEdges();
        }
    }

    virtual ~DirectedGraph() {
        for (int i = 0; i < vertexCount; ++i) {
            delete[] vertices[i].edges;
        }
        delete[] vertices;
    }
};

class WeightedGraph : public DirectedGraph {
    
};

int main() {
	
    GraphBase** graphs = new GraphBase*[2];
    graphs[0] = new DirectedGraph();
    graphs[1] = new WeightedGraph();

    
    for (int i = 0; i < 2; ++i) {
        graphs[i]->addVertex(0);
        graphs[i]->addVertex(1);
        graphs[i]->addVertex(2);
    }

    
    graphs[0]->addEdge(0, 1, 2.5); 
    graphs[0]->addEdge(1, 2, 3.0);
    graphs[1]->addEdge(0, 2, 4.5); 

    cout << "Directed Graph:\n";
    graphs[0]->display();

    cout << "\nWeighted Graph:\n";
    graphs[1]->display();

    for (int i = 0; i < 2; ++i) {
        delete graphs[i];
    }
    delete[] graphs;

    return 0;
}

