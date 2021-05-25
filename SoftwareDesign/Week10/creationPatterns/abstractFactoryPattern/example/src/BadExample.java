package example;

class ComputerA {
    CPUA _cpu;
    MemoryA _memory;

    @Override
    public String toString() {
        return String.format("%s %s %s", getClass(), _cpu, _memory);
    }

    public void add(CPUA cpu) {
        _cpu = cpu;
    }
    public void add (MemoryA memory) {
        _memory = memory;
    }
}
class ComputerB {
    CPUB _cpu;
    MemoryB _memory;

    @Override
    public String toString() {
        return String.format("%s %s %s", getClass(), _cpu, _memory);
    }

    public void add(CPUB cpu) {
        _cpu = cpu;
    }
    public void add (MemoryB memory) {
        _memory = memory;
    }
}

class CPUA {
    @Override 
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}
class CPUB {
    @Override 
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}

class MemoryA {
    @Override
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}
class MemoryB {
    @Override
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}

public class BadExample {
    public static void main(String[] args) throws Exception {
        ComputerA computer1 = new ComputerA();
        createComputer(computer1);
        System.out.println(computer1);
        
        ComputerB computer2 = new ComputerB();
        createComputer(computer2);
        System.out.println(computer2);
    }


    // VIOLATES DRY
    
    private static void createComputer(ComputerA computer)
    {
        computer.add(new CPUA());
        computer.add(new MemoryA());
    }

    private static void createComputer(ComputerB computer)
    {
        computer.add(new CPUB());
        computer.add(new MemoryB());
    }
}
