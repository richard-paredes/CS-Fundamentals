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
    public abstract String getPartsType();
} 
class ComputerA {
    @Override
    public String getPartsType() {
        return "A";
    }
}
class ComputerB {
    @Override
    public String getPartsType() {
        return "B";
    }
}

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

public class AlternateGoodExample {
    public static void main(String[] args)
    throws ClassNotFoundException, InstantiationException
    {
        ComputerA computer1 = new ComputerA();
        createComputer(computer1, new ComputerFactoryA());
        // customize computer A by doing some other logic afterwards. . .
        System.out.println(computer1);
        
        ComputerB computer2 = new ComputerB();
        createComputer(computer2, new ComputerFactoryB());
        System.out.println(computer2);
    }

    // Instead of relying fully with an abstract factory, we can take advantage of the language's Reflection capability
    // the concept remains the same though
    private static void createComputer(Comptuer computer, ComputerFactory factory)
    throws ClassNotFoundException, InstantiationException
    {
        String partsType = computer.getPartsType();

        computer.add((CPU) Class.forName("CPU"+partsType).newInstance());
        computer.add((Memory) Class.forName("Memory"+partsType).newInstance());
    }
}
