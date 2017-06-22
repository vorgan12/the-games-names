calc_select = ''
        
def miles_per_gallon():
    
    miles_driven = float(input("\nEnter miles driven: "))

    gallons_used = float(input("\nEnter gallons used: "))

    mpg = miles_driven / gallons_used

    print("\nMiles per gallon:", mpg)

def trap_area():

    trap_height = float(input('\nEnter Trapezoid Height: '))

    trap_top = float(input('\nEnter Trapezoid Top Length: '))

    trap_bot = float(input('\nEnter Trapezoid Bottom Length: '))

    area = (.5 * (trap_top + trap_bot) * trap_height)

    print('Area of the Trapezoid: ', area)

def re_run():
    
    more = input('\nReturn to Menu? (y/n):')

    if more == 'y':

        print('\n' * 100)

        start_calc()

def start_calc():
    calc_select = input('Select Calculator:\n' + '1: MPG\n' + '2: Area of Trapezoid\n' + ('\n' * 5) + '>')

    print('\n' * 5)
                                  
    while calc_select == '1':
                                  
        miles_per_gallon()
                                  
        re_run()
                                  
    while calc_select == '2':
                                  
        trap_area()
                                  
        re_run()

    if calc_select == 'exit' or calc_select == 'quit' or calc_select == 'close':

        exit()

while calc_select == '':
    
    start_calc()

