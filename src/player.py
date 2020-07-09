# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room

  def __str__(self):
    return f"{self.current_room}"

  def move(self, command):
    attribute = f"{command}_to"

    if hasattr(self.current_room, attribute):
      self.current_room = getattr(self.current_room, attribute)
    else:
      print("\nYou can't go that way!\n")
