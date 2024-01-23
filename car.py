import car_properties



def main ():
    lst_car1 = [];
    lst_car2 = [];

    brand1 = input('Select Brand for car#1:').lower();
    lst_car1.append(brand1);

    type1 = input('Select Type for car#1: ').lower();
    lst_car1.append(type1);

    ##colour1 = input('Select Colour for car#1:').lower();
    ##lst_car1.append(colour1)

    while True:
        colour1 = input('Enter your colour: ').lower();

        if colour1 not in  car_properties.car_colours:
            print('This is not an available colour, please pick another');
            continue
        else:
            lst_car1.append(colour1);
            break


    print(lst_car1)
   # car2 = input('Enter a car option2(brand, type, colour): ');
    print('You Entered:{} and {}'.format(lst_car1, lst_car2));

if __name__ == '__main__':
    main ()