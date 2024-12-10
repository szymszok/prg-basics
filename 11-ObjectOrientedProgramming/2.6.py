class Phone():
    def __init__(self,battery_level,storage,isTurn):
        self.battery = battery_level
        self.storage = storage
        self.isTurn = isTurn

    def make_call(self, phone_number):
        print(f'Calling on number: {phone_number}, please wait')

    def send_mess(self,phone_number,message):
        print(f'Sending message: "{message}" to number: {phone_number}')

    def install_app(self,app_name,space_app):
        self.storage -= space_app
        print(f'Installing {app_name} on your device, please wait ... Current storage capacity is {self.storage}GB')

    def display_state(self):
        print('Current state of your phone: ')
        print(f'Battery level: {self.battery}%')
        print(f'Your current storage capacity is: {self.storage}GB')
        if self.isTurn == True:
            print('Your device is turned on')
        else:
            print('Your device is turned off')
        
def main():
    phone1 = Phone(89,128,True)
    phone1.make_call('530-753-327')
    phone1.send_mess('530-753-327', "Hello it's me GINES")
    phone1.install_app('Revolut', 8)
    phone1.install_app('Facebook',10)
    print()
    phone1.display_state()



main()
    

