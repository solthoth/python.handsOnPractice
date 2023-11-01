from collections import namedtuple


def main():
    #add code here
    #create a driver with a name, car type, and car capacity
    Driver = namedtuple("Driver", ["name", "type", "capacity"])
    #an example you can use to practice: "Iris", "Toyota Prius", 7
    driver = Driver("Iris", "Toyota Prius", 7)
    #check if they can take a certain order, given their car's capacity.
    if driver.capacity <= 10:
        print("Driver {0} can make all deliveries in their {1}".format(driver.name, driver.type))
    else:
        print("Driver {0} cannot make all deliveries in their {1}".format(driver.name, driver.type))

if __name__ == "__main__":
    main()