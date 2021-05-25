abstract class Computer {
    CPU _cpu;
    Memory _memory;

    @Override
    public String toString() {
        return String.format("%s %s %s", getClass(), _cpu, _memory);
    }

    public void add(CPU cpu) {
        _cpu = cpu;
    }
    public void add (Memory memory) {
        _memory = memory;
    }
} 
class ComputerA {}
class ComputerB {}

abstract class CPU {
    @Override 
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}
class CPUA extends CPU {}
class CPUB extends CPU {}

abstract class Memory {
    @Override
    public String toString() {
        return String.format("%s %d", getClass(), hashCode());
    }
}
class MemoryA extends Memory {}
class MemoryB extends Memory {}

public class OkayExample {
    public static void main(String[] args) throws Exception {
        ComputerA computer1 = new ComputerA();
        createComputer(computer1);
        System.out.println(computer1);
        
        ComputerB computer2 = new ComputerB();
        createComputer(computer2);
        System.out.println(computer2);
    }

    // OCP
    private static void createComputer(Comptuer computer)
    {
        if (computer instanceof ComputerA) {
            computer.add(new CPUA());
            computer.add(new MemoryA());
        } else if (computer instanceof ComputerB) {
            computer.add(new CPUB());
            computer.add(new MemoryB());
        }
    }
}
