interface FlightBooking {}
public class EconomyFlightBooking implements FlightBooking {
    @Override
    public String toString() {
        return "Economy flight";
    }
}
public class FirstClassFlightBooking implements FlightBooking {
    @Override
    public String toString() {
        return "First class flight";
    }
}
interface HotelReservation {}
public class ThreeStarHotelReservation implements HotelReservation {
    @Override
    public String toString() {
        return "3* hotel";
    }
}
public class FiveStarHotelReservation implements HotelReservation {
    @Override
    public String toString() {
        return "5* hotel";
    }
}
interface CarRental {}
class EconomyCarRental implements CarRental {
    @Override
    public String toString() {
        return "Economy car";
    }
}
class LuxuryCarRental implements CarRental {
    @Override
    public String toString() {
        return "Luxury car";
    }
}
abstract class Employee {
    protected HotelReservation _hotel;
    protected FlightBooking _flight;
    protected CarRental _car;

    public void GetReadyForTravel() {
        _car = new EconomyCarRental();
        _flight = new EconomyFlightBooking();
        _hotel = new ThreeStarHotelReservation();

    }

    @Override
    public String toString() {
        return String.format("%s %s %s %s", getClass(), _flight, _hotel, _car);
    }
}

class Developer extends Employee {}
class SalesExecutive extends Employee {
    
    // Violates DRY
    @Override
    public void getReadyForTravel() {
        _car = new LuxuryCarRental();
        _flight = new FirstClassFlightBooking();
        _hotel = new FiveStarHotelReservation();
    }
}
public class ImprovedExample {
    public static void PrepareEmployeeForTravel(Employee employee) {
        employee.getReadyForTravel();
        System.out.println(employee);
    }
    public static void main(String[] args) throws Exception {
        Developer developer = new Developer();
        prepareEmployeeForTravel(developer);

        SalesExecutive salesGuy = new SalesExecutive();
        prepareEmployeeForTravel(salesGuy);
    }
}
