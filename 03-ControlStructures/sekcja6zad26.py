pin = "0805"
attempts = 3

while attempts > 0:
    entered_pin = input(f'Enter the PIN code: ')
    attempts -= 1
    if entered_pin == pin:
        print('PIN code correct!')
        break
    else:
        print('PIN code incorrect')
else:
    print('Sorry, your payment card has been blocked.')

  
        
     
    


    