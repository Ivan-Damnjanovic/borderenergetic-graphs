/**
 * Template for selecting a subset of graphs that satisfy a given condition.
 */
import java.io.*;

public class SubsetTemplate {
    // Variables needed to run the template
    private String g6code;          // g6code of a graph
    private Graph g;                // graph
       
    // Files
    private BufferedReader in;      // input file with graphs
    private PrintWriter outResults; // output file for selected graphs and other data

    // graph counter, useful for occassionally printing the number of graphs processed so far
    private static int counter;
    
    public SubsetTemplate() {
    }
        
    /** 
     * The main method whose argument inputFileName
     * points to a file containing graphs in g6 format,
     * while createDotFiles instructs whether to write Graphviz .dot files for g6codes
     */
    public void run(String inputFileName, int createDotFiles) throws IOException {
        long startTime = System.currentTimeMillis();               // Take a note of starting time
        counter = 0;                                               // Initialise counter
        
        in = new BufferedReader(new FileReader(inputFileName));    // Open input and output files
        outResults = new PrintWriter(new BufferedWriter(new FileWriter(inputFileName + "-results.tex")));
        
        // Strings, arrays and other objects need to be created with "new" keyword.
        // For arrays, one has to specify type and dimensions as well.
        g6code = new String();
        
        while ((g6code = in.readLine())!=null) {  // Loading g6 codes until an empty line is found
            g = new Graph(g6code);                // Create a graph out of its g6 code
            int n = g.n();
            
            // Calculate necessary invariants here:
            double[] eigs = g.Aspectrum();
            double energy = g.Aenergy();
                
            // is it border-energetic?
            if (DoubleUtil.equals(energy, 2*n-2)) {
                outResults.println(g6code);       // output g6code and eigenvalues
                
                // export graph in Graphviz format for later visualisation
                if (createDotFiles!=0) {
                    StringBuilder data = new StringBuilder("eigenvalues=[");
                    for (int i=0; i<g.n(); i++) {   // create string representation of spectrum
                        data.append(eigs[i]);
                        if (i<g.n()-1)
                            data.append(", ");
                        else
                            data.append("]");
                    }
                    
                    g.saveDotFormat("be-n-" + g.n() + "-g6code-" + g6code + ".dot", 
                                    data.toString());
                }
            }
            
            counter++;                            // Update counter and report progress
            if (counter % 1000000 == 0)
                System.out.println("" + counter + " graphs processed so far");
        }
        
        in.close();                              // Testing done, close the files
        outResults.close();
        
        long totalTime = System.currentTimeMillis() - startTime;    // Report elapsed time
        System.out.println("Time elapsed: " + 
            (totalTime / 60000) + " min, " + ((double) (totalTime % 60000) / 1000) + " sec");
    }
    
    // This function may be used to run the template from out of BlueJ
    public static void main(String[] args) throws IOException, NumberFormatException {
        new SubsetTemplate().run(args[0], Integer.decode(args[1]));
    }
    
    public static void automateMe() throws IOException, NumberFormatException {
        SubsetTemplate st = new SubsetTemplate();
        st.run("graph3c.g6", 1);
        st.run("graph4c.g6", 1);
        st.run("graph5c.g6", 1);
        st.run("graph6c.g6", 1);
        st.run("graph7c.g6", 1);
        st.run("graph8c.g6", 1);
        st.run("graph9c.g6", 1);
        st.run("graph10c.g6", 1);
        st.run("graph11c.g6", 1);
        st.run("graph12c.g6", 1);
    }
}