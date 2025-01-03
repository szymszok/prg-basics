class TV:
    def __init__(self,channel):
      self.is_on = False
      self.channel = channel
    def turn_off(self):
      self.is_on = False
    def turn_on(self):
        self.is_on = True
    def channel_no(self):
        return self.channel
    '''def set_channel(self, new_channel_no):
        if self.is_on:
            self.channel = new_channel_no
            return f'Channel set to {self.channel}'
        else:
            return 'Cannot change channel tv is off' '''
    def show_status(self):
        if self.is_on:
            return f'TV in on, channel {self.channel}'
        else:
            return 'TV is off'
    def set_channels(self, channels_list):
        self.channels = channels_list

    
    def show_channels(self):
        if self.channels:
            for i in range(len(self.channels)):
                return f'Available channels:\n '+ '\n'.join(f'{i}. {channel}')
        else:
            return 'No channels available'





  
