package facadePattern;

class HotelReservation {

    public void reserveRoom() {
    }

}
public class App 
{
    public static void main( String[] args )
    {
        HotelReservation hotelReservation = new HotelReservation();
        hotelReservation.reserveRoom(checkIn, checkOut, bedSize, smokingPreference, breakfastIncluded);

        FlightReservation flightReservation = new FlightReservation();
        flightReservation.reserve(travelDate, isRoundTrip, returnDate, classFare, origin, destination, loyaltyProgramNumber);

        CarReservation carReservation = new CarReservation();
        carReservation.reserveCar(type, travelDate, returnDate, location, insuranceCoverage, gasOptions, rewardProgram);
        
        // OR:
        // what if we default most of these configurations?
        // ex: default configs based on previously used / most commonly used
        TravelAgent travelAgent = TravelAgent.getInstance();
        Reservation reservation = travelAgent.reserve(travelDate, returnDate, origin, destination); 
    }
}
