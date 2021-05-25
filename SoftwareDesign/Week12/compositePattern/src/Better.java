import java.util.List;

class Board {
    private List<Gate> _gates = new ArrayList<>();

    public void add(Gate gate) {
        _gates.add(gate);
    }

    public int getGatesCount() {
        return _gates.size();
    }

    public Gate getGateAt(int location) {
        return _gates.get(location);
    }
    public void trigger() {
        System.out.println("Board triggered");

        _gate.forEach(Gate::trigger);
    }
}

abstract class Gate {
    
    public void add(Gate gate) {
        throw new RuntimeException("Cannot add a gate to this gate");
    }
    public int getNumberOfComponents() {
        // throw new RuntimeException("This gate does not have any components");
        return 0;
    }
    public void trigger() {
        System.out.println("Triggered " + getClass());
    }
}
class ANDGate extends Gate {

}
class ORGate extends Gate {

}
// FlipFlop can contain other gates inside of it
class FlipFlop extends Gate { 
    private List<Gate> _gates = new ArrayList<>();

    @Override
    public void trigger() {
        super.trigger();
        _gates.forEach(Gate::trigger);
    }
}

public class App {
   
    public static void addAGateToAFlipFlop(Board board, int location, Gate gate) {
        Gate gateAtLocation = board.getGateAt(location);

        // this fails the LSP
        // our classes need to know more about the derived class. . .
        // fails OCP as a result of failing LSP
        // if (gateAtLocation instanceof FlipFlop) {
        //     FlipFlop flipFlop = (FlipFlop) gateAtLocation;
        //     flipFlop.add(gate);
        // } else {
        //     throw new RuntimeException("Cannot add a gate to that location");
        // }

        gateAtLocation.add(gate);
    }

    public static void main(String[] args) throws Exception {
        Board board = new Board();

        board.add(new ANDGate());
        board.add(new ORGate());
        board.add(new ORGate());
        board.add(new FlipFlop());

        addAGateToAFlipFlop(board, 3, new ANDGate());
        addAGateToAFlipFlop(board, 3, new ANDGate());

        System.out.println(board.getGatesCount());

        // FlipFlop flipFlop = new FlipFlop();
        // flipFlop.add(new ANDGate());
        // flipFlop.add(new ORGate());
        // System.out.println(flipFlop.getNumberOfComponents());

        board.trigger(); 

        for (int i = 0; board.getGatesCount(); i++) {
            Gate gateAtLocation = board.getAt(i);
            System.out.println(gateAtLocation);
            
            
            // if (gateAtLocation instanceof FlipFlop) {
            //     FlipFlop flipFlop = (FlipFlop) gateAtLocation;
            //     System.out.println(flipFlop.getNumberOfComponents());
            // }
            
            int count = gateAtLocation.getNumberOfComponents();
            if (count > 0) {
                System.out.println("Contains: " + count + " components");
            }
        }
    }
}
