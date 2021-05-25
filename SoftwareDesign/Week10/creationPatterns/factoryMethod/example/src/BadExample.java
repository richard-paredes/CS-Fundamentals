class FlightBooking {
    @Override
    public String toString() {
        return "Economy flight";
    }
}
class HotelReservation {
    @Override
    public String toString() {
        return "3* hotel";
    }
}
class CarRental {
    @Override
    public String toString() {
        return "Economy car";
    }
}
class Employee {
    HotelReservation _hotel;
    FlightBooking _flight;
    CarRental _car;

    public void GetReadyForTravel() {
        _car = new CarRental();
        _flight = new FlightBooking();
        _hotel = new HotelReservation();

    }

    @Override
    public String toString() {
        return String.format("%s %s %s %s", getClass(), _flight, _hotel, _car);
    }
}

class Developer extends Employee {}
class SalesExecutive extends Employee {}
public class BadExample {
    public static void PrepareEmployeeForTravel(Employee employee) {
        employee.getReadyForTravel();
        System.out.println(employee);
    }
    public static void main(String[] args) throws Exception {
        Developer developer = new Developer();
        prepareEmployeeForTravel(developer);

        // Sales guy is mad!
        SalesExecutive salesGuy = new SalesExecutive();
        prepareEmployeeForTravel(salesGuy);
    }
}
