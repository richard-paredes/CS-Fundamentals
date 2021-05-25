package prototypePattern;

public class Computer {
    private Memory _memory;
    public Computer(Memory memory) {
        _memory = memory;
    }
    public Computer(Computer otherComputer) {
        // violates OCP
        // if (otherComputer._memory instanceof Memory1)
        //     _memory = new Memory1((Memory1) otherComputer._memory);
        // else
        //     _memory = new Memory2((Memory2) otherComputer._memory);
        _memory = otherCopy._memory.copyOf();
    }
    public Computer copyOf() {
        Computer newComputer = new Computer();
        return new Computer(_memory.copyOf());
    }
    @Override
    public String toString() {
        return "Computer with memory " + _memory.getClass();
    }
}

public interface Memory {
    public abstract Memory copyOf();
}
public class Memory1 implements Memory {
    public Memory1() {}
    public Memory1(Memory1 otherMemory) {}
    @Override
    public Memory copyOf() {
        return new Memory1();
    }
}
public class Memory2 implements Memory {
    public Memory2() {}
    public Memory2(Memory2 otherMemory) {}
    @Override
    public Memory copyOf() {
        return new Memory2();
    }
}
public class Memory3 implements Memory {
    public Memory3() {}
    public Memory3(Memory1 otherMemory) {}
    @Override
    public Memory copyOf() {
        return new Memory3();
    }
}
public class App 
{
    public static Computer makeCopy(Computer computer) {
        // return new Computer(computer);
        return computer.copyOf();
    }
    public static void main( String[] args )
    {
        Computer computer1 = new Computer(new Memory1());
        Computer computer2 = new Computer(new Memory2());
        Computer computer3 = new Computer(new Memory3());
        System.out.println(computer1);
        System.out.println(computer2);
        System.out.println(computer3);
        System.out.println(makeCopy(computer1));
        System.out.println(makeCopy(computer2));
        System.out.println(makeCopy(computer3));
    }
}
