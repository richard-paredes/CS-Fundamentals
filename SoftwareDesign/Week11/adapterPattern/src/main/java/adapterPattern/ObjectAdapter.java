package adapterPattern;

// if Memory2 is a final class, the ClassAdapter has issues

// This is an Object adapter
class Memory2Adapter2 implements Memory {
    private Memory2 _memory2;

    public Memory2Adapter2(Memory2 memory2) {
        _memory2 = memory2;
    }

    @Override
    public void store(int addr, byte value) {
        System.out.println("Using object adapter");
        _memory2.setAddr(addr);
        _memory2.write(value);
    }
}

class Memory2Derived extends Memory2 {

}

public class ObjectAdapter {
    Computer computer2 = new Computer(new Memory2Adapter2(new Memory2()));
    computer2.work();

    Computer computer3 = new Computer(new Memory2Adapter2(new Memory2Derived()));
    computer3 .work();
}
