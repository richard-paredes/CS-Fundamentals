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

    // method itself is a factory!
    // in Factory Method, method is abstract
    // the methods are polymorphic
    protected abstract CarRental rentCar();
    protected abstract FlightBooking bookFlight();
    protected abstract HotelReservation reserveHotel();

    public void GetReadyForTravel() {
        _car = rentCar();
        _flight = bookFlight();
        _hotel = reserveHotel();

    }

    @Override
    public String toString() {
        return String.format("%s %s %s %s", getClass(), _flight, _hotel, _car);
    }
}
class Developer extends Employee {
    @Override
    protected CarRental rentCar() {
        return EconomyCarRental();
    }
    @Override
    protected FlightBooking bookFlight() {
        return EconomyFlightBooking();
    }
    @Override
    protected HotelReservation reserveHotel() {
        return ThreeStarHotelReservation();
    }
}
class SalesExecutive extends Employee {
    @Override
    protected CarRental rentCar() {
        return LuxuryCarRental();
    }
    @Override
    protected FlightBooking bookFlight() {
        return FirstClassFlightBooking();
    }
    @Override
    protected HotelReservation reserveHotel() {
        return FiveStarHotelReservation();
    }
}
class SalesEngineer extends Employee {
    @Override
    protected CarRental rentCar() {
        return LuxuryCarRental();
    }
    @Override
    protected FlightBooking bookFlight() {
        return EconomyFlightBooking();
    }
    @Override
    protected HotelReservation reserveHotel() {
        return ThreeStarHotelReservation();
    }
}
public class GoodExample {
    public static void PrepareEmployeeForTravel(Employee employee) {
        employee.getReadyForTravel();
        System.out.println(employee);
    }
    public static void main(String[] args) throws Exception {
        Developer developer = new Developer();
        prepareEmployeeForTravel(developer);

        SalesExecutive salesGuy = new SalesExecutive();
        prepareEmployeeForTravel(salesGuy);

        SalesEngineer salesEngineer = new SalesEngineer();
        prepareEmployeeForTravel(salesEngineer);
    }
}
