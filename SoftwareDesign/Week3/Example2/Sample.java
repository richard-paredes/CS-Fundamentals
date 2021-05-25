abstract class Human {
   abstract public void help();
}

interface Helper {
    public void help();
}

class Man implements Helper {
    public void help() {
        System.out.println("man helping");
    }
}
class Woman implements Helper {
    public void help() {
        System.out.println("woman helping");
    }
}
class Elephant implements Helper {
    public void help() {
        System.out.println("elephant can help quite a bit");
    }
}


public class Sample {
    public static void seekHelpFrom(Human helper) {
        helper.help();
    }
    public static void main(String[] args) {
        Man man = new Man();
        Woman woman = new Woman();
        seekHelpFrom(man);
        seekHelpFrom(woman);

        Elephant hathi = new Elephant();
        seekHelpFrom(hathi);
    }
}
