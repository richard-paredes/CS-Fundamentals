class Car:
    def __init__(self, initialDistance):
        self.distance = initialDistance
    
    def drive(self, dist):
        print("Driving...")
        self.distance += dist

    def getDistance(self):
        return self.distance

def main():
    car = Car(0)
    car.drive(5)
    dist = car.getDistance()
    print("Car has been driven", dist, "miles")

    car2 = Car(1)
    car2.drive(1)
    dist2 = car2.getDistance()
    print("Car 2 has been drive", dist2, "miles")

main()