import com.ibm.wala.classLoader.IClass;
import com.ibm.wala.classLoader.IMethod;
import com.ibm.wala.ipa.callgraph.AnalysisScope;
import com.ibm.wala.ipa.callgraph.CallGraph;
import com.ibm.wala.ipa.callgraph.Entrypoint;
import com.ibm.wala.ipa.callgraph.cha.CHACallGraph;
import com.ibm.wala.ipa.callgraph.impl.Util;
import com.ibm.wala.ipa.cha.ClassHierarchy;
import com.ibm.wala.ipa.cha.ClassHierarchyException;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ipa.cha.IClassHierarchy;
import com.ibm.wala.types.ClassLoaderReference;
import com.ibm.wala.util.CancelException;
import com.ibm.wala.util.config.AnalysisScopeReader;
import com.ibm.wala.util.io.FileProvider;

import java.io.File;
import java.io.IOException;
import java.net.URISyntaxException;
import java.net.URL;

public class CallGraphExample {

    /**
     * @param projectJar JAR of the project to be analyzed
     * @return the {@link AnalysisScope} object indicating what classes are available in the class path
     * @throws URISyntaxException
     */
    public static AnalysisScope createScope(String projectJar) throws URISyntaxException, IOException {
        URL jreUrl = CallGraphExample.class.getResource("jdk-17.0.1/rt.jar");
        File exFile = new FileProvider().getFile("Java60RegressionExclusions.txt");

        AnalysisScope scope = AnalysisScopeReader.makeJavaBinaryAnalysisScope(projectJar, exFile);
        AnalysisScopeReader.addClassPathToScope(jreUrl.getPath(), scope, ClassLoaderReference.Primordial);
        return scope;
    }
    // javac HelloWorld.java --release 8
    public static void main(String[] args) throws IOException, ClassHierarchyException, URISyntaxException, CancelException {
        // creates an analysis scope
        AnalysisScope scope = createScope(CallGraphExample.class.getResource("HelloWorld.class").getPath());
        // build the class hierarchy
        IClassHierarchy cha = ClassHierarchyFactory.make(scope);

        CHACallGraph cg = new CHACallGraph(cha, true);
        Iterable<Entrypoint> entrypoints = Util.makeMainEntrypoints(scope, cha);
        cg.init(entrypoints);
        cg.forEach(n ->{
            System.out.println(n);
        });

    }
}
