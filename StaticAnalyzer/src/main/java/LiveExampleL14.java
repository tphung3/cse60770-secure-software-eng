import com.ibm.wala.ipa.callgraph.*;
import com.ibm.wala.ipa.callgraph.cha.CHACallGraph;
import com.ibm.wala.ipa.callgraph.impl.Util;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ipa.cha.IClassHierarchy;
import com.ibm.wala.ssa.IR;
import com.ibm.wala.types.ClassLoaderReference;
import com.ibm.wala.util.config.AnalysisScopeReader;
import com.ibm.wala.util.io.FileProvider;

import java.io.File;
import java.net.URL;

public class LiveExampleL14 {
    public static void main(String[] args) throws Exception {
        File exFile = new FileProvider().getFile("Java60RegressionExclusions.txt");

        URL resource = LiveExampleL14.class.getResource("Example1.jar");
        AnalysisScope scope = AnalysisScopeReader.makeJavaBinaryAnalysisScope(resource.getPath(),exFile );
        String runtimeClasses = LiveExampleL14.class.getResource("jdk-17.0.1/rt.jar").getPath();
        AnalysisScopeReader.addClassPathToScope(runtimeClasses, scope, ClassLoaderReference.Primordial);

        IClassHierarchy classHierarchy = ClassHierarchyFactory.make(scope);

        // Class Hierarchy
        CHACallGraph cg = new CHACallGraph(classHierarchy, true);
        Iterable<Entrypoint> entrypoints = Util.makeMainEntrypoints(scope, classHierarchy);
        cg.init(entrypoints);
        for(CGNode n: cg){
            if(n.toString().contains("main")){
                IR ir = n.getIR();
                System.out.println(ir);
                new CFGVisualizer(n,true).generateVisualGraph(new File("cfg-bb.dot"));
            }

        }
        // RTA?
//        AnalysisOptions options = new AnalysisOptions();
//        options.setEntrypoints(entrypoints);
//        CallGraphBuilder<InstanceKey> builder = Util.makeRTABuilder(options, new AnalysisCacheImpl(), classHierarchy, scope);
//        CallGraph rtaCallGraph = builder.makeCallGraph(options, null);
//
//        System.out.println(rtaCallGraph.getNumberOfNodes());


    }
}
