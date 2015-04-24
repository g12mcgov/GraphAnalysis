
import java.util.LinkedList;
import java.util.List;

public class Node {
    public String name;
    public List<Node> edgeNodes;


    public Node(String nametoinput) {
        this.name = nametoinput;
        this.edgeNodes = new LinkedList<Node>();
    }

    public void addEdgeNode(final Node node) {
        this.edgeNodes.add(node);
        node.edgeNodes.add(this);
    }
    public int getedgeNodes(){
    	return edgeNodes.size();
    }

}