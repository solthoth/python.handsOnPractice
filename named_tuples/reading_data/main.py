from csv import reader
from collections import namedtuple


def main():
    #add code here
    #read data/Customer.csv
    with open("data/customer.csv", "r") as r:
        read = reader(r)
        Person = namedtuple("Person", next(read))
        for line in read:
            person = Person(*line)            # pprint(person)
            print(person)
    #Create workable objects with each line
    

if __name__ == "__main__":
    main()