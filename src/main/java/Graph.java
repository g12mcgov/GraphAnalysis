import java.util.ArrayList;
import java.util.List;

public class Graph {
		private List<Node> vertices = new ArrayList<Node>();

	    public Graph(ArrayList<Node> vertices) {
	        this.vertices = vertices;
	    }

	    public void addVertex(Node vertex) {
	        if (!this.vertices.contains(vertex)) {
	            this.vertices.add(vertex);
	        }
	    }

	    public void printGraph() {
	        for (int i = 0; i < this.vertices.size(); i++) {
	            Node vertex = this.vertices.get(i);
	            String edges = "";
	            for (int j = 0; j < vertex.edgeNodes.size(); j++) {
	                edges += vertex.edgeNodes.get(j).name + ", ";
	            }
	            System.out.println("Node " + vertex.name + " relation to: " + edges);
	        }
	    }
}
