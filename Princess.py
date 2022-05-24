class Princess():
  
  fake_database = [("Jasmine", "Agrabah"),
                 ("Ariel", "Atlantis"),
                 ("Belle", "France"),
                 ("Mulan", "China")]

  @staticmethod
  def static_all():
    return [Princess(*p) for p in Princess.fake_database]
  
  @classmethod
  def all(cls):
    # ...
    # princess = new Princess(...p)
    return [Princess(*p) for p in cls.fake_database]

  @classmethod
  def get_one_by_name(cls, name):
    match = list(filter(lambda x: x[0] == name, cls.fake_database))
    if len(match) == 1:
      return Princess(*match[0])
    else:
      raise Exception("No matching princess found.")

  def __init__(self, name, location):
    print("name", name)
    print("location", location)
    self.name = name
    self.location = location
    self.shape = "human"

  def transform(self, hideous_new_form):
    self.shape = hideous_new_form
    
  def __repr__(self):
    return f"Princess {self.name}"

print(Princess.all())
m = Princess.get_one_by_name("Mulan")
m.transform("frog")
print(m)
print(m.shape)
