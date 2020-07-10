# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  # def __init__(self, name, description, n_to, s_to, e_to, w_to):
  def __init__(self, name, description):
    self.name = name
    self.description = description
    self.items = []
    # self.n_to = None
    # self.s_to = None
    # self.e_to = None
    # self.w_to = None

  def __str__(self):
    return f"{self.name} {self.description}"

  def add_item(self, item):
    self.items.append(item)
  
  def remove_item(self, item):
    self.items.remove(item)

  def list_items(self):
    if len(self.items) == 0:
      print('\n !!! There are no items in this room !!!')
    else:
      print(f"\n  Items in {self.name}:")
      for i in self.items:
        print(f"    - {i}")
