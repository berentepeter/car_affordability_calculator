import car_properties
import gas_price
import states
import math

def monthly_loan_payment(principal, interest_rate, term):
    # loan amortization formula: M = P⋅r⋅(1+r)^n / (1+r)^n−1 
    # M is the monthly payment,
    # P is the remaining loan principal,
    # r is the monthly interest rate (annual interest rate divided by 12), and
    # n is the total number of payments.
    monthly_interest_rate = interest_rate / 12;
    payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** term) / ((1 + monthly_interest_rate) ** term - 1);
    return round(payment, 2)

def monthly_maintenance_cost(yearly_maintenance_budget):
    return yearly_maintenance_budget / 12;

def monthly_gas_price(car_usage, fuel_consumption, state):
    gas = gas_price.gas_prices[state]
    #print(gas)
    return ((car_usage * 30) / fuel_consumption) * gas;


def monthly_total_payment():
    pass



def main ():
    lst_car1 = [];
    lst_car2 = [];

    while True:
        state = input('Which state do you live in?\n').lower();
        if state not in states.states:
            print('Invalid state. Please select from the states of USA');
            continue
        else:
            lst_car1.append(state);
            lst_car2.append(state);
            print("INFO: Gas price in {} is ${}".format(state.title(), gas_price.gas_prices[state]));
            break
    

    loan_principal = int(input('\nPlease enter the principal amount of the loan:\n'));

    loan_interest_rate = float(input('\nPlease enter the yearly interest rate of the loan (i.e: if the interest is 3.2% then enter 3.2):\n'));
    try:
        1/loan_interest_rate;
        1/(loan_interest_rate + math.sqrt(loan_interest_rate ** 2));
    except:
        print("ERROR: please try again with interest rate being a positive number greater than 0");
        exit();
    finally:
        loan_interest_rate = loan_interest_rate * 0.01;

    print("interest rate: {}".format(loan_interest_rate))
    loan_term = int(input('\nPlease enter the loan term (amount of months):\n'));

    while True:
        type = input('\nPlease select a car type\n').lower();
        if type not in car_properties.car_type:
            print('WARNING: Unavailable car type. Please select from the following list: \n Sedan, SUV, Hatchback, Coupe, Convertible, Minivan, Pickup, Sports, Electric, Hybrid, Luxury, Compact, Wagon, 4x4 ');
            continue
        else:
            lst_car1.append(type);
            break
    print("type: {}".format(type))
    
    while True:
        brand = input('\nPlease select a car brand\n').lower();
        if brand not in car_properties.car_brand:
            print('WARNING: Unavailable car brand. Please select from the following list: \n   Mercedes-Benz, Audi, BMW, Lexus, Cadillac, Infiniti, Acura, VolksWagen, Kia, Subaru, Toyota, Nissan, Hyundai, Mazda, Honda, Jeep, GMC, RAM, Ford, Chevrolet');
            continue
        else:
            lst_car1.append(brand);
            break
    
    print("brand: {}".format(brand))

    print('monthly loan payment: ${}'.format(monthly_loan_payment(loan_principal, loan_interest_rate, loan_term)))

    price = car_properties.car_brand.get(brand).get('price');
    print("price: ${}".format(price));
    maintenance = car_properties.car_brand.get(brand).get('maintenance');
    print("yearly maintenance: ${}".format(maintenance));
    seat = car_properties.car_type.get(type).get('seats');
    print("number of seats: {}".format(seat));
    consumption = car_properties.car_type.get(type).get('consumption');
    print("consumption: {}".format(consumption));
    comfort = car_properties.car_type.get(type).get('comfort');
    print("comfort: {}".format(comfort));


    while True:
        colour = input('\nEnter car colour:\n').lower();

        if colour not in  car_properties.car_colour:
            print('This is not an available colour, please pick another');
            continue
        else:
            lst_car1.append(colour);
            break

    print(lst_car1)
   # car2 = input('Enter a car option2(brand, type, colour): ');
    print('You selected a {} {} in {}'.format(*lst_car1));
    #print('You also selected a {} {} in {}'.format(*lst_car2));

if __name__ == '__main__':
    main ()

