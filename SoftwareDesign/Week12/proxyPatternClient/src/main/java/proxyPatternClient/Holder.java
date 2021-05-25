class Holder {
    // creates Heavy before instantiating the Holder
    // private HeavyImpl heavy = new HeavyImpl();

    //Create a virtual proxy instead
    //no longer eager creation
    Heavy heavy = new Heavy();

    public Holder() {
        System.out.println("Creating holder...");
    }
    public Heavy getHeavy() {
        return heavy;
    }
}

// this is a virtual proxy
// basically holds same methods as HeavyImpl
// should have the same interface!
class  Heavy {
    private HeavyImpl _heavy = null;

    private getHeavy() {
        if (_heavy == null) { _heavy = new HeavyImpl(); }
        return _heavy;
    }

    public int someMethod() {
        return getHeavy().someMethod();
    }

    public int someMethod2() {
        return getHeavy().someMethod();
    }
}

class HeavyImpl {
    public Heavy() {
        System.out.println("Creating Heavy object...");
    }
    public int someMethod() {
        return 2;
    }
}
public class App {
    public static void main(String[] args) {
        Holder holder = new Holder();
        
        System.out.println("About to call getHeavy...");
        Heavy heavy = holder.getHeavy();
        System.out.println(heavy.someMethod());
    }
}
