import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;


public class WFUWWWNetwork {

	public static void main(String[] args) throws IOException {
		String filename = "cswebData.txt";

		ClassLoader classLoader = WFUWWWNetwork.class.getClassLoader();
		File file = new File(classLoader.getResource(filename).getFile());
		
		Scanner scan = new Scanner(file); //for reading the input
		
		int numvertex = scan.nextInt();
		
		String[] stringname = new String[numvertex+1];
		Node[] nodearray =  new Node[numvertex+1];
		ArrayList<Node> nodes = new ArrayList<Node>();
		
		int i = 0;
		while (scan.hasNextLine() ) {
	        String line = scan.nextLine();
	        if (line.equals("*****"))
	        	break;
	        else {
	        	nodearray[i] = new Node(line);
	        	nodes.add(nodearray[i]);
	        	stringname[i] = new String(line);
	        	i++;
	        }
	    }
		
		String numedge = scan.nextLine();
		
		while (scan.hasNextLine()){
	        String line = scan.nextLine();
	        String[] splited = line.split("\\s+");
	        int x = Arrays.asList(stringname).indexOf(splited[0]);
	        int y = Arrays.asList(stringname).indexOf(splited[1]);
//	        System.out.println("Connecting " + x + " to " + y );
//	        System.out.println("Connecting " + splited[0] + " to " + splited[1]);
//	        System.out.println("Connecting " + nodearray[x].name + " to " + nodearray[y].name);
	        nodearray[x].addEdgeNode(nodearray[y]);
	    }
		
		scan.close();
		Graph directedGraph = new Graph(nodes);
		
        //directedGraph.printGraph();
		//Question 1
		int max = 0;
		for(int a = 0; a < numvertex + 1 ; a++){
			int temp = nodearray[a].getedgeNodes();
			if (temp > max){
				max = a;
			}
		}
		
        System.out.println("Max is " + nodearray[max].name + " with a value of max " + nodearray[max].getedgeNodes());
		//
		//Question 2
		float sum = 0;
		for(int a = 0; a < numvertex + 1 ; a++){
			float temp = nodearray[a].getedgeNodes();
			sum += temp;
		}
		float average = sum / numvertex;   
	    System.out.println("Average value of interactions is : " + average);
	}

}
