import com.ibm.wala.classLoader.IClass;
import com.ibm.wala.ipa.callgraph.*;
import com.ibm.wala.ipa.callgraph.cha.CHACallGraph;
import com.ibm.wala.ipa.callgraph.impl.Util;
import com.ibm.wala.ipa.callgraph.propagation.InstanceKey;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ipa.cha.IClassHierarchy;
import com.ibm.wala.types.ClassLoaderReference;
import com.ibm.wala.util.config.AnalysisScopeReader;
import com.ibm.wala.util.io.FileProvider;

import java.io.File;
import java.io.IOException;
import java.net.URL;

public class LiveExample1 {
    public static void main(String[] args) throws Exception {
        File exFile = new FileProvider().getFile("Java60RegressionExclusions.txt");

        URL resource = LiveExample1.class.getResource("HelloWorld.class");
        AnalysisScope scope = AnalysisScopeReader.makeJavaBinaryAnalysisScope(resource.getPath(),exFile );
        String runtimeClasses = LiveExample1.class.getResource("jdk-17.0.1/rt.jar").getPath();
        AnalysisScopeReader.addClassPathToScope(runtimeClasses, scope, ClassLoaderReference.Primordial);

        IClassHierarchy classHierarchy = ClassHierarchyFactory.make(scope);

        // Class Hierarchy
//        CHACallGraph cg = new CHACallGraph(classHierarchy, false);
        Iterable<Entrypoint> entrypoints = Util.makeMainEntrypoints(scope, classHierarchy);
//        cg.init();
//        System.out.println(cg.getNumberOfNodes());
//        for(CGNode n: cg){
//            System.out.println(n);
//        }
        // RTA?
        AnalysisOptions options = new AnalysisOptions();
        options.setEntrypoints(entrypoints);
        CallGraphBuilder<InstanceKey> builder = Util.makeRTABuilder(options, new AnalysisCacheImpl(), classHierarchy, scope);
        CallGraph rtaCallGraph = builder.makeCallGraph(options, null);

        System.out.println(rtaCallGraph.getNumberOfNodes());


    }
}
