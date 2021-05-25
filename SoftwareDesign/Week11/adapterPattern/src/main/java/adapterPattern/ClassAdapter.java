package adapterPattern;

class Computer {
    Memory _memory;
    public Computer(Memory memory) { _memory = memory; }
    public void work() { 
        _memory.store(11111, (byte) 0);
    }
}
interface Memory {
    void store(int addr, byte value);
} 

class Memory1 implements Memory {
    @Override
    public void store(int addr, byte value) {
        System.out.println("Storing in memory1");
    }
}
class Memory2 {
    public void setAddr(int addr) {
        System.out.println("Memory2 set addr called");
    }
    public void write(byte value) {
        System.out.println("Memory2 writing");
    }
}
class Memory2Adapter1 extends Memory2 implements Memory {
    @Override
    public void store(int addr, byte value) {
        System.out.println("Using class adapter");
        setAddr(addr);
        write(value);
    }
}
public class ClassAdapter 
{
    public static void main( String[] args )
    {
        Computer comp = new Computer(new Memory1());
        comp.work();

        Computer comp2 = new Computer(new Memory2Adapter1());
        comp2.work();

    }
}
