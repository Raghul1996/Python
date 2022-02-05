import random

class password_generation():
    def __init__(self):
        pass
    
    @staticmethod
    def generate_password():
        lower='abcdefghijklmnopqrstuvwxyz'
        upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        number='1234567890'
        symbol='@#$%^&*()'
        all=lower+upper+number+symbol
        length=9
        password="".join(random.sample(all,length))
        print(f'The random password generated is {password}')

pass_obj=password_generation()
pass_obj.generate_password()