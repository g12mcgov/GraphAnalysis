import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.io.InputStream;

public class FacebookInteractions {
	/* Inline class for multiple return types */
	public static class FileData {
		
		public Node[] nodearray;
		public int numvertex;
		public String numedge;
		
		// Basic constructor.
		public FileData(Node[] nodearray, int numvertex, String numedge) {
			this.nodearray = nodearray;
			this.numvertex = numvertex;
			this.numedge = numedge;
		}
	}
	
	public static void main(String args[]) throws IOException	{
		String filename = "FBdata.txt";
		
		ClassLoader classLoader = FacebookInteractions.class.getClassLoader();
		File file = new File(classLoader.getResource(filename).getFile());
		
		Scanner scan = new Scanner(file); //for reading the input
		FileData fileDataObject = FacebookInteractions.getFileData(scan);

		int numvertex = fileDataObject.numvertex;
		String numedge = fileDataObject.numedge;
		Node[] nodearray = fileDataObject.nodearray;
		
		// Question 1
		int max = 0;
		
		for(int a = 0; a < numvertex + 1 ; a++){
			int temp = nodearray[a].getedgeNodes();
			if (temp > max){
				max = a;
			}
		}
		
        System.out.println("Max is " + nodearray[max].name + " with a value of max " + nodearray[max].getedgeNodes());
		
		//Question 2
		float sum = 0;
		
		for(int a = 0; a < numvertex + 1 ; a++){
			float temp = nodearray[a].getedgeNodes();
			sum += temp;
		}
		
		float average = sum / numvertex;
	    
		System.out.println("Average value of interactions is : " + average);
	}

	public static FileData getFileData(Scanner scan) {
		int numvertex = scan.nextInt();

		String[] stringname = new String[numvertex+1];
		Node[] nodearray =  new Node[numvertex+1];

		ArrayList<Node> nodes = new ArrayList<Node>();

		// Vertices
		int i = 0;
		while (scan.hasNextLine()) {
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

		// Edges
		while (scan.hasNextLine() ) {
			String line = scan.nextLine();
			String[] splited = line.split("\\s+");
			
			int x = Arrays.asList(stringname).indexOf(splited[0]);
			int y = Arrays.asList(stringname).indexOf(splited[1]);
//	        
// System.out.println("Connecting " + x + " to " + y );
//	        System.out.println("Connecting " + splited[0] + " to " + splited[1]);
//	        System.out.println("Connecting " + nodearray[x].name + " to " + nodearray[y].name);
			nodearray[x].addEdgeNode(nodearray[y]);
		}
		
		scan.close();
	
		// Create a new FileData inline object to provide multiple return params
		return new FileData(nodearray, numvertex, numedge);
	}
}