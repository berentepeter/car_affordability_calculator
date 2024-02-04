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
    return round(yearly_maintenance_budget / 12, 2);

def monthly_gas_price(car_usage, fuel_consumption, state):
    gas = gas_price.gas_prices[state]
    #print(gas)
    return ((car_usage * 4.3) / fuel_consumption) * gas;


def size_compare(dict1, dict2):
    if dict1['seat'] + dict1['comfort']> dict2['seat'] + dict2['comfort']:
        return dict1;
    elif dict1['seat'] + dict1['comfort']< dict2['seat'] + dict2['comfort']:
        return dict2;
    else: 
        return None;

def compare_and_select(dict1, dict2):
    #sum_dict1 = sum(dict1.values())
    #sum_dict2 = sum(dict2.values())
    sum_dict1 = sum(value for value in dict1.values() if isinstance(value, int));
    sum_dict2 = sum(value for value in dict2.values() if isinstance(value, int));

    if kids_number > 0: #bele kell irni a dicitonary-be, vagy utananezni globalis valtozoknak!!
        try: size_compare(dict1, dict2)
        except: 
            print("Both cars have same (size+comfort) index")
            kids_number = 0
            compare_and_select(dict1, dict2)
    elif sum_dict1 > sum_dict2:
        return dict1;
    elif sum_dict2 > sum_dict1:
        return dict2;
    else:
        return None; # if they are equal

'''
###TEST function 
def iterate_dict(dict_to_iterate):
    for key, value in dict_to_iterate.items():
        if type(value) == dict:
            print(key)
            iterate_dict(value)
        else:
            print(key + ":" + str(value))
'''


def main ():

### TEST function call
### iterate_dict(car_properties.car_brand);

    dct_car1 = {
        "type" : "string",
        "brand" : "string",
        "price" : 1,
        "maintenance" : 1,
        "consumption" :1,
        "seat" : 1,
        "comfort" : 1,
        "colour" : "string",
        "loan" : 1,
        "gas" : 1
    };

    dct_car2 = {
        "type" : "string",
        "brand" : "string",
        "price" : 1,
        "maintenance" : 1,
        "consumption" :1,
        "seat" : 1,
        "comfort" : 1,
        "colour" : "string",
        "loan" : 1,
        "gas" : 1
    };

    gas = 0;
    loan = 0;
    kids_number = -1;
    while True:
        state = input('Which state do you live in?\n').lower();
        if state not in states.states:
            print('Invalid state. Please select from the states of USA');
            continue
        else:
            gas = gas_price.gas_prices[state];
            print("INFO: Gas price in {} is ${}".format(state.title(), gas_price.gas_prices[state]));
            break
    '''
    while True:
        loan_principal = int(input('\nPlease enter the principal amount of the loan:\n (cheapest car available is $20.000)\n'));
        if loan_principal < 20000:
            print('WARNING: Please inout a number greater than 20.000 \n');
            continue
        else:
            break
    '''

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

    #loan = monthly_loan_payment(loan_principal, loan_interest_rate, loan_term);

    while True:
        usage_workdays_1 = float(input('\nPlease tell us how many km you drive daily on a workday(Monday-Friday):\n'));
        usage_weekends_1 = float(input('\nPlease tell us how many km you drive daily on weekend(Saturday-Sunday):\n'));
        if usage_workdays_1 < 0 or usage_weekends_1 < 0:
            print('Please enter a positive number ');
            continue
        else:
            usage_all_week = (usage_workdays_1 * 5) + (usage_weekends_1 * 2);
            break 

    while True:
        kids = input('\nDo you have kids?\n').lower();
        if kids in ('yes', 'y', 'sure', 'ocf'):
            kids_number = int(input('\nHow many? (under 18)\n'));
            break
        elif kids in ('no', 'n', 'nope', 'maybe'):
            kids_number = 0;
            break
        else:
            print('\ninvalid answer\n');
            continue
            

### CAR #1
    while True:
        type_1 = input('\nPlease select a type for car#1\n').lower();
        if type_1 not in car_properties.car_type:
            print('WARNING: Unavailable car type. Please select from the following list: \n Sedan, SUV, Hatchback, Coupe, Convertible, Minivan, Pickup, Sports, Electric, Hybrid, Luxury, Compact, Wagon, 4x4 ');
            continue
        else:
            dct_car1.update(type=type_1);
            break

    while True:
        brand_1 = input('\nPlease select a brand for car#1\n').lower();
        if brand_1 not in car_properties.car_brand:
            print('WARNING: Unavailable car brand. Please select from the following list: \n   Mercedes-Benz, Audi, BMW, Lexus, Cadillac, Infiniti, Acura, VolksWagen, Kia, Subaru, Toyota, Nissan, Hyundai, Mazda, Honda, Jeep, GMC, RAM, Ford, Chevrolet');
            continue
        else:
            dct_car1.update(brand=brand_1);
            break

    while True:
        colour_1 = input('\nEnter car colour:\n').lower();

        if colour_1 not in  car_properties.car_colour:
            print('This is not an available colour, please pick another');
            continue
        else:
            dct_car1.update(colour=colour_1);
            break   

    price_1 = car_properties.car_brand.get(brand_1).get('price');
    maintenance_1 = car_properties.car_brand.get(brand_1).get('maintenance');
    seat_1 = car_properties.car_type.get(type_1).get('seats');
    consumption_1 = car_properties.car_type.get(type_1).get('consumption');
    comfort_1 = car_properties.car_type.get(type_1).get('comfort');
    loan_1 = monthly_loan_payment(price_1, loan_interest_rate, loan_term);
    gas_1 = monthly_gas_price(usage_all_week, consumption_1, state);
    '''
    print('\nCAR #1:');
    print('monthly loan payment: ${}'.format(loan_1));
    print("car#1 type: {}".format(type_1));
    print("car#1 brand: {}".format(brand_1));
    print("price: ${}".format(price_1));
    print("monthly maintenance: ${}".format(monthly_maintenance_cost(maintenance_1)));
    print("number of seats: {}".format(seat_1));
    print("consumption: {}L/100km".format(consumption_1));
    print("estimated monthly gas price: ${}".format(gas_1))
    print("comfort: {}".format(comfort_1));
    print("colour: {}".format(colour_1));
    '''
    dct_car1.update(price=price_1, maintenance=maintenance_1, seat=seat_1, consumption=consumption_1, comfort=comfort_1, colour=colour_1, loan=loan_1, gas=gas_1);
    #print(dct_car1);

###CAR #2
    while True:
        type_2 = input('\nPlease select a type for car#2\n').lower();
        if type_2 not in car_properties.car_type:
            print('WARNING: Unavailable car type. Please select from the following list: \n Sedan, SUV, Hatchback, Coupe, Convertible, Minivan, Pickup, Sports, Electric, Hybrid, Luxury, Compact, Wagon, 4x4 ');
            continue
        else:
            dct_car2.update(type=type_2);
            break
    print("car#1 type: {}".format(type_2))

    while True:
        brand_2 = input('\nPlease select a brand for car#2\n').lower();
        if brand_2 not in car_properties.car_brand:
            print('WARNING: Unavailable car brand. Please select from the following list: \n   Mercedes-Benz, Audi, BMW, Lexus, Cadillac, Infiniti, Acura, VolksWagen, Kia, Subaru, Toyota, Nissan, Hyundai, Mazda, Honda, Jeep, GMC, RAM, Ford, Chevrolet');
            continue
        else:
            dct_car2.update(brand=brand_2);
            break
    while True:
        colour_2 = input('\nEnter car colour:\n').lower();

        if colour_2 not in  car_properties.car_colour:
            print('This is not an available colour, please pick another');
            continue
        else:
            dct_car2.update(colour=colour_2);
            break

    price_2 = car_properties.car_brand.get(brand_2).get('price');
    maintenance_2 = car_properties.car_brand.get(brand_2).get('maintenance');
    seat_2 = car_properties.car_type.get(type_2).get('seats');
    consumption_2 = car_properties.car_type.get(type_2).get('consumption');
    comfort_2 = car_properties.car_type.get(type_2).get('comfort');
    loan_2 = monthly_loan_payment(price_2, loan_interest_rate, loan_term);
    gas_2 = monthly_gas_price(usage_all_week, consumption_2, state);
    '''
    print('\nCAR #2:');
    print("car#1 type: {}".format(type_2));
    print("car#1 brand: {}".format(brand_2));
    print('monthly loan payment: ${}'.format(loan_2));    
    print("price: ${}".format(price_2));
    print("monthly maintenance: ${}".format(monthly_maintenance_cost(maintenance_2)));
    print("number of seats: {}".format(seat_2));
    print("consumption: {}L/100km".format(consumption_2));
    print("estimated monthly gas price: ${}".format(gas_2))
    print("comfort: {}".format(comfort_2));
    print("colour: {}".format(colour_2));
    '''
    dct_car2.update(price=price_2, maintenance=maintenance_2, seat=seat_2, consumption=consumption_2, comfort=comfort_2, colour=colour_2, loan=loan_2, gas=gas_2);
    #print(dct_car1);
    #print(dct_car2);

    result_dict = compare_and_select(dct_car1, dct_car2)

    if result_dict:
        print("\n ");
        print(f"\nBetter choice for you:");
        print(f"fcar#1 type: {result_dict['type']}");
        print(f"car#1 brand: {result_dict['brand']}");
        print(f"monthly loan payment: ${result_dict['loan']}");
        print(f"price: ${result_dict['price']}");
        print(f"monthly maintenance: ${monthly_maintenance_cost(result_dict['maintenance'])}");
        print(f"number of seats: {result_dict['seat']}");
        print(f"consumption: {result_dict['consumption']}L/100km");
        print(f"estimated monthly gas price: ${result_dict['gas']}")
        print(f"comfort: {result_dict['comfort']}");
        print(f"colour: {result_dict['colour']}");
    else:
        print("Both car you selected could be a good choice.")

if __name__ == '__main__':
    main ()

