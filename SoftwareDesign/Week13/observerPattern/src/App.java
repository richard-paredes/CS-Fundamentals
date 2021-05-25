// Stock fails OCP. If we try to add a display, need to modify the class. . .
class Stock {
    private DisplayStock _display; 
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
            _display.display(value);
        }
    }
    public void start() {
        Thread th = new Thread(() -> generatePrice());
        th.start();
    }
    public void setDisplay(StockDisplay display) {
        _display = display;
    }
}

class DisplayStock {
    public void display(double value) {
        System.out.println(value);
    }
}
public class App {
    public static void main(String[] args) throws Exception {
        Stock stock = new Stock();
        stock.start();

        DisplayStock display = new DisplayStock();
        stock.setDisplay(display);
    }
}
