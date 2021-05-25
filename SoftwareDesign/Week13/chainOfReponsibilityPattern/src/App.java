import java.util.Random;

class OurDataSource {
    private AboveThresholdHandler _handler;
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

    public void addListener(AboveThresholdHandler handler) {
        _handler = handler;
    }
}

class AboveThresholdHandler {
    private int _threshold;
    public AboveThresholdHandler(int threshold) {
        _threshold = threshold;
    }
    public void Handle(int value) {
        if (value > _threshold) {
            System.out.println("Value " + value + " exceeded the threshold " + _threshold);
        }
    }
}
class AboveThresholdHandler {
    private int _threshold;
    public AboveThresholdHandler(int threshold) {
        _threshold = threshold;
    }
    public void Handle(int value) {
        if (value < _threshold) {
            System.out.println("Value " + value + " is below the threshold " + _threshold);
        }
    }
}


public class App {
    public static void main(String[] args) throws Exception {
        
        OurDataSource ourDataSource = new OurDataSource();
        
        /** FAILS OCP */
        // AboveThresholdHandler aboveThresholdHandler = new AboveThresholdHandler(900);
        // BelowThresholdHandler belowThresholdHandler = new BelowThresholdHandler(100);

        // ourDataSource.addListener(aboveThresholdHandler);
        // ourDataSource.addListener(belowThresholdHandler);

        ourDataSource.start();

    }
}

