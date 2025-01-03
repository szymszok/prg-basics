from tv import TV

def main():
    my_tv = TV(1)  
    sample_channels = ['TVP1', 'TVP2', 'DISCOVERY', 'POLSAT']
    my_tv.set_channels(sample_channels)
    while True:
        number = int(input('Decide what to do: (1-turn on TV, 2-turn off TV, 3-show status, 4-change channel, 5-add channel, 6-list of channels, 0-exit): '))
        channel_list = []
        
        if number == 0:
            print("Exiting the program.")
            break
        elif number == 1:
            my_tv.turn_on()
            print("You turned on the TV.")
        elif number == 2:
            my_tv.turn_off()
            print("You turned off the TV.")
        elif number == 3:
            print(my_tv.show_status())
        elif number == 4:
            channel = int(input('Enter channel number to change: '))
            my_tv.set_channel(channel)
        elif number == 5:
            channel_name = input('Enter channel name: ')
            channel_list.append(channel_name)
        

if __name__ == "__main__":
    main()