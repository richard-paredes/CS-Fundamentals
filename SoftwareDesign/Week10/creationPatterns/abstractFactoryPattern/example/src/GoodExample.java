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

interface ComputerFactory {
    CPU getCPU();
    Memory getMemory();
}
class ComputerFactoryA implements ComputerFactory {
    @Override
    public CPU getCPU() {
        return new CPUA();
    }
    @Override 
    public Memory getMemory() {
        return new MemoryA();
    }
}
class ComputerFactoryB implements ComputerFactory {
    @Override
    public CPU getCPU() {
        return new CPUB();
    }
    @Override 
    public Memory getMemory() {
        return new MemoryB();
    }
}

public class GoodExample {
    public static void main(String[] args) throws Exception {
        ComputerA computer1 = new ComputerA();
        createComputer(computer1, new ComputerFactoryA());
        // customize computer A by doing some other logic afterwards. . .
        System.out.println(computer1);
        
        ComputerB computer2 = new ComputerB();
        createComputer(computer2, new ComputerFactoryB());
        System.out.println(computer2);
    }

    private static void createComputer(Comptuer computer, ComputerFactory factory)
    {
        computer.add(factory.getCPU());
        computer.add(factory.getMemory());
    }
}
