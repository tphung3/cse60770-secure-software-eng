import com.ibm.wala.classLoader.IClass;
import com.ibm.wala.classLoader.IMethod;
import com.ibm.wala.ipa.callgraph.AnalysisScope;
import com.ibm.wala.ipa.cha.ClassHierarchy;
import com.ibm.wala.ipa.cha.ClassHierarchyException;
import com.ibm.wala.ipa.cha.ClassHierarchyFactory;
import com.ibm.wala.ipa.cha.IClassHierarchy;
import com.ibm.wala.types.ClassLoaderReference;
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

    public static void main(String[] args) throws IOException, ClassHierarchyException, URISyntaxException {
//        loadJRE();

        //
//        System.setProperty("sun.boot.class.path","/Library/Java/JavaVirtualMachines/jdk-17.0.1.jdk/Contents/Home");
//        System.setProperty("sun.boot.class.path","/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib");
//        System.setProperty("java.specification.version","9");
        // exclusions file


        // creates an analysis scope
//        File exFile = new FileProvider().getFile("Java60RegressionExclusions.txt");
//        AnalysisScope scope = AnalysisScopeReader.makeJavaBinaryAnalysisScope("/Users/joanna/Documents/Portfolio/GitHub/cse60770-secure-software-eng/StaticAnalyzer/src/main/resources/HelloWorld.jar", exFile);
//        AnalysisScopeReader.addClassPathToScope("/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home/lib/rt.jar",scope, ClassLoaderReference.Primordial);
//        AnalysisScopeReader.addClassPathToScope("/Users/joanna/Documents/Portfolio/GitHub/cse60770-secure-software-eng/StaticAnalyzer/src/main/resources",scope, ClassLoaderReference.Application);
        AnalysisScope scope = createScope(CallGraphExample.class.getResource("HelloWorld.class").getPath());
        // build the class hierarchy
        IClassHierarchy cha = ClassHierarchyFactory.make(scope);

        for (IClass c : cha) {
            if(c.getName().toString().contains("Hello")) System.out.println(c);
//            if (c.getClassLoader().toString().toLowerCase().startsWith("app")) System.out.println(c);
//            System.out.println(c.getClassLoader().getClass());
//            if(!c.getClassLoader().equals(cha.getLoader(ClassLoaderReference.Application))) continue;
//            String cname = c.getName().toString();
//            System.out.println("Class:" + cname);
//            for (IMethod m : c.getAllMethods()) {
////                String mname = m.getName().toString();
////                System.out.println("  method:" + mname);
//            }
//            System.out.println();
        }
    }
}
