import car_properties
import gas_price
import states
import math

kids_number = -1;

'''
loan amortization formula: M = P⋅r⋅(1+r)^n / (1+r)^n−1 
M is the monthly payment,
P is the remaining loan principal,
r is the monthly interest rate (annual interest rate divided by 12), and
n is the total number of payments.
'''
def monthly_loan_payment(principal, interest_rate, term):
    monthly_interest_rate = interest_rate / 12;
    payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** term) / ((1 + monthly_interest_rate) ** term - 1);
    return round(payment, 2)

def monthly_maintenance_cost(yearly_maintenance_budget):
    return round(yearly_maintenance_budget / 12, 2);

def monthly_gas_price(car_usage, fuel_consumption, state):
    gas = gas_price.gas_prices[state]
    return round(((car_usage * 4.3) / fuel_consumption) * gas, 2);


def size_compare(dict1, dict2):
    if dict1['seat'] + dict1['comfort']> dict2['seat'] + dict2['comfort']:
        return dict1;
    elif dict1['seat'] + dict1['comfort']< dict2['seat'] + dict2['comfort']:
        return dict2;
    else: 
        return None;

def compare_and_select(dict1, dict2):
    global kids_number

    sum_dict1 = sum(value for value in dict1.values() if isinstance(value, int)) - dict1['consumption'];
    sum_dict2 = sum(value for value in dict2.values() if isinstance(value, int)) - dict2['consumption'];

    if kids_number > 0: 
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


def get_user_input(prompt, valid_options, warning_message):
    while True:
        user_input = input(prompt).lower()
        if user_input not in valid_options:
            print(warning_message)
            continue
        return user_input


def main ():

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

    state = get_user_input('Which state do you live in?\n', states.states, 'Invalid state. Please select from the states of USA')
    gas = gas_price.gas_prices[state];
    print("INFO: Gas price in {} is ${}".format(state.title(), gas_price.gas_prices[state]));

    intereset_list_float = [str(i / 10) for i in range(0, 1001)];
    intereset_list_int = [str(i) for i in range(101)];
    intereset_list = intereset_list_float + intereset_list_int;

    loan_interest_rate = get_user_input('\nPlease enter the yearly interest rate of the loan (i.e: if the interest is 3.2% then enter 3.2):\n', intereset_list, "Invalid answer: please try again with interest rate being a positive number greater than 0");
    loan_interest_rate = float(loan_interest_rate) * 0.01;
    
    loan_term = int(input('\nPlease enter the loan term (amount of months):\n'));

    down_payment_q = input('\nDo you want to pay down-payment?')
    if down_payment_q in ('yes', 'y', 'sure', 'ocf'):
        down_payment_a = int(input('How much?'))
    else:
        down_payment_a = 0

    km_list_float = [str(i / 10) for i in range(0, 10001)];
    km_list_int = [str(i) for i in range(1001)];
    km_list = km_list_float + km_list_int;

    usage_workdays_1 = get_user_input('\nPlease tell us how many km you drive daily on a workday(Monday-Friday):\n', km_list, 'Invalid answer: Please enter a positive integer');
    usage_weekends_1 = get_user_input('\nPlease tell us how many km you drive daily on weekend(Saturday-Sunday):\n', km_list, 'Invalid answer: Please enter a positive integer');
    usage_all_week = (float(usage_workdays_1) * 5) + (float(usage_weekends_1) * 2);

    kids = get_user_input('\nDo you have kids?\n', ('yes', 'y', 'sure', 'ocf', 'no', 'n', 'nope', 'maybe'), '\ninvalid answer\n')
    if kids in ('yes', 'y', 'sure', 'ocf'):
        kids_number = int(input('How many? (under 18)\n'));
    elif kids in ('no', 'n', 'nope', 'maybe'):
        kids_number = 0;

### CAR #1
    type_1 = get_user_input('\nPlease select a type for car#1\n', car_properties.car_type, 'WARNING: Unavailable car type. Please select from the following list: \n Sedan, SUV, Hatchback, Coupe, Convertible, Minivan, Pickup, Sports, Electric, Hybrid, Luxury, Compact, Wagon, 4x4');
    dct_car1.update(type=type_1);

    brand_1 = get_user_input('\nPlease select a brand for car#1\n', car_properties.car_brand, 'WARNING: Unavailable car brand. Please select from the following list: \n   Mercedes-Benz, Audi, BMW, Lexus, Cadillac, Infiniti, Acura, VolksWagen, Kia, Subaru, Toyota, Nissan, Hyundai, Mazda, Honda, Jeep, GMC, RAM, Ford, Chevrolet');
    dct_car1.update(brand=brand_1);

    colour_1 = get_user_input('\nEnter car colour:#1\n', car_properties.car_colour, 'This is not an available colour, please pick another');
    dct_car1.update(colour=colour_1); 

    price_1 = car_properties.car_brand.get(brand_1).get('price') - down_payment_a;
    maintenance_1 = car_properties.car_brand.get(brand_1).get('maintenance');
    seat_1 = car_properties.car_type.get(type_1).get('seats');
    consumption_1 = car_properties.car_type.get(type_1).get('consumption');
    comfort_1 = car_properties.car_type.get(type_1).get('comfort');
    loan_1 = monthly_loan_payment(price_1, loan_interest_rate, loan_term);
    gas_1 = monthly_gas_price(usage_all_week, consumption_1, state);

    dct_car1.update(price=price_1, maintenance=maintenance_1, seat=seat_1, consumption=consumption_1, comfort=comfort_1, colour=colour_1, loan=loan_1, gas=gas_1);

###CAR #2
    type_2 = get_user_input('\nPlease select a type for car#2\n', car_properties.car_type, 'WARNING: Unavailable car type. Please select from the following list: \n Sedan, SUV, Hatchback, Coupe, Convertible, Minivan, Pickup, Sports, Electric, Hybrid, Luxury, Compact, Wagon, 4x4');
    dct_car2.update(type=type_2);

    brand_2 = get_user_input('\nPlease select a brand for car#2\n', car_properties.car_brand, 'WARNING: Unavailable car brand. Please select from the following list: \n   Mercedes-Benz, Audi, BMW, Lexus, Cadillac, Infiniti, Acura, VolksWagen, Kia, Subaru, Toyota, Nissan, Hyundai, Mazda, Honda, Jeep, GMC, RAM, Ford, Chevrolet');
    dct_car2.update(brand=brand_2);

    colour_2 = get_user_input('\nEnter car colour:#2\n', car_properties.car_colour, 'This is not an available colour, please pick another');
    dct_car2.update(colour=colour_2); 

    price_2 = car_properties.car_brand.get(brand_2).get('price') - down_payment_a;
    maintenance_2 = car_properties.car_brand.get(brand_2).get('maintenance');
    seat_2 = car_properties.car_type.get(type_2).get('seats');
    consumption_2 = car_properties.car_type.get(type_2).get('consumption');
    comfort_2 = car_properties.car_type.get(type_2).get('comfort');
    loan_2 = monthly_loan_payment(price_2, loan_interest_rate, loan_term);
    gas_2 = monthly_gas_price(usage_all_week, consumption_2, state);

    dct_car2.update(price=price_2, maintenance=maintenance_2, seat=seat_2, consumption=consumption_2, comfort=comfort_2, colour=colour_2, loan=loan_2, gas=gas_2);

    result_dict = compare_and_select(dct_car1, dct_car2)

    if result_dict:
        print(" ");
        print(f"\nBetter choice for you:");
        print(f"type: {result_dict['type']}");
        print(f"brand: {result_dict['brand']}");
        print(f"monthly loan payment: ${result_dict['loan']}");
        print(f"price: ${result_dict['price']}");
        print(f"monthly maintenance: ${monthly_maintenance_cost(result_dict['maintenance'])}");
        print(f"number of seats: {result_dict['seat']}");
        print(f"consumption: {result_dict['consumption']}L/100km");
        print(f"estimated monthly gas price: ${result_dict['gas']}")
        print(f"comfort: {car_properties.car_comfort.get(str(result_dict['comfort']))}");
        print(f"colour: {result_dict['colour']}");
    else:
        print("Both car you selected could be a good choice.")

if __name__ == '__main__':
    main ()
