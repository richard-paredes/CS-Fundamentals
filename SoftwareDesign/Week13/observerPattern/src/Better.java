
import java.util.Observable;
// Observable is from a java.util.* 
class Stock extends Observable {
    
    private void sleep(int ms) {
        try {
            Thread.sleep(ms);
        } catch (InterruptedException ex) {
            e.printStackTrace();
        }
    }
    public void generatePrice() {
        while (true) {
            sleep(1000);
            double value = Math.random();
            notifyObservers(value);
            setChange();
        }
    }
    public void start() {
        Thread th = new Thread(() -> generatePrice());
        th.start();
    }

}

class DisplayStock implements Observer {
    public void display(double value) {
        System.out.println(value);
    }
    @Override
    public void update(Observable observable, Object data) {
        System.out.println("Stock value: " + data);
    }
}

class DisplaySelectStock implements Observer {
    private double _threshold;

    public DisplaySelectStock(double threshold) {
        _threshold = threshold;
    }

    @Override
    public void update(Observable observable, Object data) {
        double value = (double) data;
        if (value > _threshold) {
            System.out.println("Stock value exceeds the threshold: " + values);
        }
    }
}

class DisplaySelectStockAlt {
    private double _threshold;

    public DisplaySelectStockAlt(double threshold) {
        _threshold = threshold;
    }

    public void display(Object data) {
        double value = (double) data;
        if (value > _threshold) {
            System.out.println("Stock value exceeds the threshold: " + values);
        }
    }

    public void displayWithObservable(Observable observable, Object data) {
        double value = (double) data;
        if (value > _threshold) {
            System.out.println("Stock value exceeds the threshold: " + values);
        }
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        Stock stock = new Stock();
        DisplayStock display = new DisplayStock();
        DisplaySelectStock selectDisplay = new DisplaySelectStock(0.8);
        DisplaySelectStockAlt selectDisplayAlt = new DisplaySelectStockAlt(0.5);
        
        stock.start();
        stock.addObserver(display);
        stock.addObserver(selectDisplay);

        // since an Observer is a functional interface in Java:
        // we can use lambdas instead of creating a full class!
        stock.addObserver((observable, data) -> System.out.println(data));
        // or alternatively
        stock.addObserver((observable, data) -> displaySelectStockAlt.display(data));
        // or even more simplified (withotu inheriting from the Observable)
        stock.addObserver(displaySelectStockAlt::display);
    }
}
