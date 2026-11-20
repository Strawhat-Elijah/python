class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self):
# Create the default settings
    self.__status = False
    self.__muted = False
    self.__volume = self.MIN_VOLUME
    self.__channel = self.MIN_CHANNEL

  def power(self):
# Turn the TV on or off
    self.__status = not self.__status

  def mute(self):
# Mute and unmute the tv
    if self.__status:
      self.__muted = not self.__muted

  def channel_up(self):
# Increase the channel and wrap it to the min
    if self.__status:
      if self.__channel == self.MAX_CHANNEL:
        self.__channel == self.MIN_CHANNEL
    else:
      self.__channel += 1

  def channel_down(self):
# Decrease the channel and wrap it to the max
    if self.__status:
      if self.__status == self.MIN_CHANNEL:
        self.__channel == self.MAX_CHANNEL
      else:
        self.__channel -= 1

  def volume_up(self):
# Increase the volume and unmute the tc
    if self.__status:
      self.__muted = False
      if self.__volume < self.MAX_VOLUME:
        self.__volume += 1

  def volume_down(self):
# decrease the volume and unmute the tv
    if self.__status:
      self.__muted = False
      if self.__volume > self.MIN_VOLUME:
        self.__volume -= 1

  def __str__(self):
# Return the current tv settetings
    if self .__muted:
      volume = self.MIN_VOLUME
    else:
      volume = self.__volume

    return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'
