class TV:
   def __init__(self,channel_no):
      self.is_on = False
      self.chanel_no = channel_no
      self.chanel_no = 1
   def turn_off(self):
      self.is_on = False
   def turn_on (self):
      self.is_on = True
   def show_status(self):
      if self.is_on:     
         return True, self.chanel_no
      else:
         return False
   def set_channel(number):
      self.channel_no
      