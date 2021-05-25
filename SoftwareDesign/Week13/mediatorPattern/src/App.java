class Tire {
    private int _radius;
    private Wheel _wheel
    public Tire(Wheel wheel) {  
        _wheel = wheel;
        _wheel.setTire(this);
    }
    public int getRadius() {
        return _radius;
    }
    private void setRadius(int radius) {
        _radius = radius;
    }
    public boolean changeRadius(int radius) {
        return _wheel.setRadius(this, radius);
    }
    @Override
    public String toString() {
        return getClass().toString() + " radius: " + _radius;
    }
}
class Hub {
    private int _radius;
    private Wheel _wheel;
    public Hub(Wheel wheel) {
        _wheel = wheel;
        _wheel.setHub(this);
    }
    
    public int getRadius() {
        return _radius;
    }
    private void setRadius(int radius) {
        _radius = radius;
    }
    public boolean changeRadius(int radius) {
        return _wheel.setRadius(this, radius);
    }
    @Override
    public String toString() {
        return getClass().toString() + " radius: " + _radius;
    }
}
class Spoke {
    private int _size;
    private Wheel _wheel;
    public Spoke(Wheel wheel) {
        _wheel = wheel;
        wheel.setSpoke(this);
    }
    public int getSize() {
        return _size;
    }
    private void setSize(int size) {
        _size = size;
    }
    public boolean changeSize(int size) {
        return _wheel.setSize(this, size);
    }
    @Override
    public String toString() {
        return getClass().toString() + " size: " + _size;
    }
}

// The mediator class
class Wheel {
    private Tire _tire;
    private Hub _hub;
    private Spoke _spoke;
    public Tire setTire(Tire tire) {
        _tire = tire;
    }
    public Hub setHub(Hub hub) {
        _hub = hub;
    }
    public Spoke setSpoke(Spoke spoke) {
        _spoke = spoke;
    }
    public boolean setRadius(Tire tire, int radius) {
        if (_hub == null || _hub.getRadius() < radius) {
            _tire.setRadius(radius);
            _spoke.setSize(_tire.getRadius - _hub.getRadius());
            return true;
        }
        return false;
    }
    public boolean setRadius(Hub hub, int radius) {
        if (_tire == null || _tire.getRadius() > radius) {
            _hub.setRadius(radius);
            _spoke.setSize(_tire.getRadius - _hub.getRadius());
            return true;
        }
        return false;
    }
    public boolean setSize(Spoke spoke, int size) {
        if (_tire == null || _hub == null || _tire.getRadius() - _hub.getRadius() == size) {
            spoke.setSize(size);
            return true;
        }
        return false;
    }
}

public class App {
    public static void main(String[] args) throws Exception {
        Tire tire = new Tire();
        tire.changeRadius(100);

        Hub hub = new Hub();
        hub.changeRadius(20);

        // RULE: The hubs radius needs to be less than tire's radius.
        // How do we enforce this rule???

        // needs to know about each other. . . poor approach
        // tire.setHub()

        // if we add a spoke later, which also needs to be less than hub and tire. .. 
        Spoke spoke = new Spoke();
        spoke.changeSize(80);

        System.out.println(tire);
        System.out.println(hub);
        System.out.println(spoke);

        tire.changeRadius(10); // should not be allowed. tire.radius < hub.radius
    }
}
