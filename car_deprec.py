####################################################
##           Developed by James W. Blood          ##
##             jamesblood1986@gmail.com           ##
##               v0.1     August 2017             ##
####################################################





class Vehicle:
    'Value of car after x number of years'

    def __init__(self, value, business_pct, depreciation_pct, yrs_since_val):
        self.first_val = float(value)
        self.business_pct = float(business_pct)
        self.depreciation_pct = float(depreciation_pct)
        self.yrs_since_val = float(yrs_since_val)
        self.value = self.current_val(self.first_val)

    def current_val(self, value):
        'works out the current value of the car'
        value = self.first_val * (
            1 - self.depreciation_pct)**self.yrs_since_val
        return value

    def claim_amount(self):
        'how much can you claim?'
        if self.yrs_since_val < 1:
            return 'You cannot claim anything'
        else:
            val_lst_yr = self.first_val * (1 - self.depreciation_pct)**(
                self.yrs_since_val - 1)
            val_this_yr = self.first_val * (
                1 - self.depreciation_pct)**self.yrs_since_val
            diff = val_lst_yr - val_this_yr
            return ''.join([
                'You can claim £', str(round(self.business_pct * (val_lst_yr -
                                                            val_this_yr),2))
            ])


print(
    'This code tells you the current value of your car according to HMRC and how much tax you can claim for last year.\n\n\n'
)
val = input('How much is your car worth? (Numbers only) ')
print('\n')
dep = input('What is the rate of deprecation? (Percentage / 100 e.g. 18% = 0.18) ')
print('\n')
bus_use = input(
    'What percentage of your use is for your business? (Percentage / 100 e.g. 95% = 0.95) ')
print('\n')
val_date = input(
    'How many years ago was your vehicle last valued? (Integers only) ')
print('\n')
my_car = Vehicle(val, bus_use, dep, val_date)
print('Your car is currently worth £' + str(round(my_car.value,2)))
print('\n')
print(my_car.claim_amount())