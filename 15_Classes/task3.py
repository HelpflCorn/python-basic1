# Task 3

# TV controller

# Create a simple prototype of a TV controller in Python. It’ll use the following commands:

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

# The default channel turned on before all commands is №1.

# Your task is to create the TVController class and methods described above.

# '''


class TvController:
    def __init__(self, channels):
        self.channels = channels
        self.channel_index = None

    def first_channel(self):
        self.channel_index = 0
        return self.channels[0]
    
    def last_channel(self):
        self.channel_index = -1
        return self.channels[-1]
    
    def turn_channel(self, n):
        self.channel_index = n
        if n < 1 or n>len(self.channels):
            print(f"there's no such channel, you can only go from 1 to {len(self.channels)}")
        self.current_channel = n - 1
        print(f"you're now on channel {self.current_channel+1}")
        return self.channels[self.current_channel]

    def next_channel(self):
        self.channel_index +=1
        return self.channels[self.channel_index]
    
    def previous_channel(self):
        self.channel_index -= 1
        return self.channels[self.channel_index]
    
    def now_playing(self): #had to rename it as there's both method and a class atrribute with the same name
        if self.channel_index != None:
            return f"This is the current channel {self.channels[self.channel_index]}"
        else:
            return "there's nothing playing"

    def is_exist(self, channel_name):
        if channel_name in self.channels:
            return channel_name
        else:
            print("Your channel does not exist")

controller1 = TvController(["BBC", "Discovery", "TV1000"])
print(controller1.first_channel())
print(controller1.now_playing())
print(controller1.next_channel())
print(controller1.previous_channel())
print(controller1.turn_channel(2))
print(controller1.is_exist("UT1"))


# CHANNELS = ["BBC", "Discovery", "TV1000"]

#  class TVController:

# pass

#  controller = TVController(CHANNELS)

# controller.first_channel() == "BBC"

# controller.last_channel() == "TV1000"

# controller.turn_channel(1) == "BBC"

# controller.next_channel() == "Discovery"

# controller.previous_channel() == "BBC"

# controller.current_channel() == "BBC"

# controller.is_exist(4) == "No"

# controller.is_exist("BBC") == "Yes"

# '''