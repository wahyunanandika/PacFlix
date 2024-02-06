from datetime import datetime
from dateutil.relativedelta import relativedelta

class pacflix():
    list_of_referral_code = []

    def __init__(self, user_name):
        self.user_name = user_name
        self.start_date = None
        self.end_date = None
        self.current_plan = None
        self.duration = 0

        pacflix.list_of_referral_code.append(self.user_name)
        print(f"Your Account Succesfully Created !, share this code '{self.user_name}' to your friend to get some benefit")

    def list_plan(self):
        print('List of Pacflix plan')
        print('1. Basic Plan.')
        print("SD, 1 Device, Movie, Rp. 120000")
        print()
        print('2. Standard Plan')
        print('HD, 2 Device, Movie+sports, Rp 160000')
        print('3. Prremium Plan')
        print('UHD, 4 Device, Movie + Sports+ original series, RP 200000')

    def check_plan(self):
        if (self.current_plan) == None:
            print('you do not have subs yet!')
        else:
            print(f"your current plan is {self.current_plan}")
            print(f'start subs at {self.start_date}')
            print(f'end subs at {self.end_date}')

    def purchase(self, new_plan, ref_code, duration):
        total_price = 0
        if((ref_code != None)and (ref_code in pacflix.list_of_referral_code)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)
            if(new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = 120000 * (96/100)
                print(f'Your are selected basic plan with referral code, price {total_price}')
            elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = 160000 * (96/100)
                print(f'Your are selected standard plan with referral code, price {total_price}')
            elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = 200000 * (96/100)
                print(f'Your are selected premium plan with referral code, price {total_price}')
            else:
                self.duration = 0
                self.start_date = None
                self.end_date = None
                print('Your selected plan is invalid')
        elif ((ref_code != None) and (ref_code not in pacflix.list_of_referral_code)):
            print('Your referral code invalid')
        elif ((ref_code == None)):
            self.duration = duration
            self.start_date = datetime.now()
            self.end_date = self.start_date + relativedelta(months=duration)
            if(new_plan == 'Basic Plan'):
                self.current_plan = 'Basic Plan'
                total_price = 120000
                print(f'Your are selected basic plan, price {total_price}')
            elif(new_plan == 'Standard Plan'):
                self.current_plan = 'Standard Plan'
                total_price = 160000 
                print(f'Your are selected standard plan, price {total_price}')
            elif(new_plan == 'Premium Plan'):
                self.current_plan = 'Premium Plan'
                total_price = 200000
                print(f'Your are selected premium plan, price {total_price}')
            else:
                self.duration = 0
                print('Your selected plan is invalid')
        else:
            pass
    
    def upgrade_plan(self, new_plan):
        subs_time = self.end_date - datetime.now()
        total_price = 0
        if(subs_time.days > 360):
            if (self.current_plan == 'Basic Plan'):
                if(new_plan == 'Standard Plan'):
                    self.current_plan = 'Standard Plan'
                    total_price = (120000 - (120000 * 0.5))
                    print(f'upgrade  to {self.current_plan}, price {total_price}')
                elif (new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200000 - (200000 * 0.5))
                    print(f'upgrade  to {self.current_plan}, price {total_price}')
                else:
                    print('Selected new plan is invalid')
            elif(self.current_plan == 'Standard Plan'):
                if (new_plan == 'Premium Plan'):
                    self.current_plan = 'Premium Plan'
                    total_price = (200000 - (200000 * 0.5))
                    print(f'upgrade  to {self.current_plan}, price{total_price}')
                else:
                    print('Selected new plan is invalid')
            else:
                print('you are in highest tier, you can not downgraded')
        else:
            pass