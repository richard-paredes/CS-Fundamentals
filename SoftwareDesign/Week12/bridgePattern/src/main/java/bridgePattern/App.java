package bridgePattern;

import java.util.Arrays;

interface Translator {
    void translate(String message);
}

class SpanishTranslator implements Translator {
    @Override
    public void translate(String message) {
        if (message.equals("Let me talk about indirection...")) {
            System.out.println("Permitame hablar sobre indireccion...");
        }else {
            System.out.println("...");
        }
    }
}

class ChineseTranslator implements Translator {
    @Override
    public void translate(String message) {
        if (message.equals("Let me talk about indirection...")) {
            System.out.println("pretend this is chinese...");
        }else {
            System.out.println("...");
        }
    }
}

class TamilTranslator implements Translator {
    @Override
    public void translate(String message) {
        if (message.equals("Let me talk about indirection...")){
            System.out.println("pretend this is tamil...");
        } else {
            System.out.println("...");
        }
    }
}

class Programmer extends Expert {
    public void talk() {
        getTranslator().translate("Let me talk about indirection...");
        // System.out.println("Let me talk about indirection...");
    }
}

// without inheriting, it duplicates with Programmer stuff
class Tester extends Expert {
    public void talk() {
        getTranslator().translate("Let me talk about indirection...");
        // System.out.println("Let me talk about indirection...");
    }
}

class Architect extends Expert {
    @Override
    public void talk() {
        getTranslator().translate("Let me talk about how to evolve the design and architecture...");
    }
}

// allows extending both hierarchies, the experts and the translators
abstract class Expert {
    Translator translator;
    public Translator getTranslator() {
        return translator;
    }
    public void setTranslator(Translator theTranslator) {
        translator = theTranslator;
    }
    public abstract void talk();
}

/**
 * Hello world!
 *
 */
public class App 
{
    public static void giveTalk(List<Expert> experts, String language) {
        try {
            Class translatorClass = (Class<Translator>) Class.forName("bridgePattern."+language+"Translator");
            Translator translator = translatorClass.newInstance();
            for(Expert expert: experts) {
                expert.setTranslator(translator);
                expert.talk();
            }
            // experts.forEach(Expert::talk);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    public static void main( String[] args )
    {
        List<Expert> experts = Arrays.asList(new Programmer(), new Tester(), new Architect());
        giveTalk(experts, "Spanish");
        giveTalk(experts, "Chinese");
        giveTalk(experts, "Tamil");
    }
}
