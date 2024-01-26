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
    return (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** term) / ((1 + monthly_interest_rate) ** term - 1);
    

def monthly_maintenance_cost(yearly_maintenance_budget):
    return yearly_maintenance_budget / 12;

def monthly_gas_price(car_usage, fuel_consumption, state):
    gas = gas_price.gas_prices[state]
    print(gas)
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
            break
    
    print("INFO: Gas price in {} is ${}".format(state.title(), gas_price.gas_prices[state]))

    loan_principal = int(input('\nPlease enter the principal amount of the loan:\n'));

    loan_interest_rate = float(input('\nPlease enter the yearly interest rate of the loan (i.e: if the interest is 3.2% then enter 3.2):\n'));
    try:
        1/loan_interest_rate;
        1/(loan_interest_rate + math.sqrt(loan_interest_rate ** 2));
    except:
        print("ERROR: please try again with interest rate being a positive number greater than 0");
        exit();
    finally:
        loan_interest_rate * 0.01;

    loan_term = int(input('\nPlease enter the loan term (amount of months):\n'));

    maintenance_budget = int(input('\nEnter yearly budget for car maintenance:\n'));
    
    print(monthly_loan_payment(loan_principal, loan_interest_rate, loan_term))

    brand1 = input('\nSelect Brand for car#1:\n').lower();
    lst_car1.append(brand1);

    type1 = input('\nSelect Type for car#1:\n').lower();
    lst_car1.append(type1);

    while True:
        colour1 = input('\nEnter your colour:\n').lower();

        if colour1 not in  car_properties.car_colours:
            print('This is not an available colour, please pick another');
            continue
        else:
            lst_car1.append(colour1);
            break

    print(lst_car1)
   # car2 = input('Enter a car option2(brand, type, colour): ');
    print('You selected a {} {} in {}'.format(*lst_car1));
    #print('You also selected a {} {} in {}'.format(*lst_car2));

if __name__ == '__main__':
    main ()

