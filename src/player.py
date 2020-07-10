# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, current_room):
    self.name = name
    self.current_room = current_room
    self.items = []

  def __str__(self):
    return f"{self.current_room}"

  def move(self, command):
    attribute = f"{command[0]}_to"

    if hasattr(self.current_room, attribute):
      self.current_room = getattr(self.current_room, attribute)
    else:
      print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!\n  You can't go that way!\n!!!!!!!!!!!!!!!!!!!!!!!!!!!")


  def list_items(self):
    if len(self.items) == 0:
      print('\n !!! You are not carrying any items !!!')
    else:
      print(f"\n  Items you're carrying:")
      for i in self.items:
        print(f"    - {i}")


  def take_item(self, item):
    self.items.append(item)
  
  def drop_item(self, item):
    self.items.remove(item)
