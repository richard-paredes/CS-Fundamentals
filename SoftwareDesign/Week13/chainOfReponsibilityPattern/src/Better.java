import java.util.Random;

class OurDataSource {
    private OurDataHandler _handler;
    public void start() throws InterruptedException {
        while (true) {
            Random random = new Random();
            try {

                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }

            int value = random.nextInt(1000);
        }
    }

    public void addListener(OurDataHandler handler) {
        _handler = handler;
    }
}

abstract class OurDataHandler {
    private OurDataHandler _next;
    public OurDataHandler() {
        
    }
    public OurDataHandler(OurDataHandler next) {
        _next = next;
    }

    public final void handle(int value) {
        if (!canHandleEvent(value)) {
            handleEvent(value);
        } else {
            if (_next != null) _next.handle(value);
        }
    }
    protected abstract boolean canHandleEvent(int value);
    protected abstract boolean handleEvent(int value);
}

class AboveThresholdHandler extends Handler  {
    private int _threshold;
    public AboveThresholdHandler(int threshold) {
        super();
        _threshold = threshold;
    }
    public AboveThresholdHandler(int threshold, Handler next) {
        super(next);
        _threshold = threshold;
    }
    @Override
    public void handleEvent(int value) {
        System.out.println("Value " + value + " exceeded the threshold " + _threshold);
    }
    @Override
    public boolean canHandle(int value) {
        return value <  _threshold;
    }
}
class BelowThresholdHandler extends OurDataHandler {
    private int _threshold;
    public BelowThresholdHandler(int threshold) {
        super();
        _threshold = threshold;
    }
    public BelowThresholdHandler(int threshold, Handler next) {
        super(next);
        _threshold = threshold;
    }
    @Override
    public void handleEvent(int value) {
        System.out.println("Value " + value + " is below the threshold " + _threshold);
    }
    @Override
    public boolean canHandle(int value) {
        return value <  _threshold;
    }
}

class EvenValueHandler extends OurDataHandler {
    public EvenDataHandler() {
        super();
    }
    public EvenDataHandler(OurDataHandler next) {
        super(next);
    }
    @Override
    public void handleEvent(int value) {
        System.out.println("Value " + value + " is even");
    }
    @Override
    public boolean canHandle(int value) {
        return value % 2 == 0; 
    }
}


public class App {
    public static void main(String[] args) throws Exception {
        
        OurDataSource ourDataSource = new OurDataSource();
        
        OurDataHandler aboveThresholdHandler = new AboveThresholdHandler(900);
        OurDataHandler evenValueHandler = new EvenValueHandler(aboveThresholdHandler);
        OurDataHandler belowThresholdHandler = new BelowThresholdHandler(100, evenValueHandler);

        ourDataSource.addListener(belowThresholdHandler);

        ourDataSource.start();

    }
}

