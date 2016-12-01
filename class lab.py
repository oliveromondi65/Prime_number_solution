class Car(object): #creating the class Car
  
  def __init__(self, name='General', model='GM', vehicle_type=None):
    self.name = name
    self.model = model
    self.vehicle_type = vehicle_type
    self.speed = 0 #the speed when not moving is 0
    self.num_of_wheels = 4
    self.num_of_doors = 4


    if self.name in ['Porshe', 'Koenigsegg']: #testing if carname is either porshe or Koenigsegg
      self.num_of_doors = 2 #porshe or Koenigsegg should have 2 doors
   

    if self.vehicle_type == 'trailer': #trailers have more than 4 wheels
      self.num_of_wheels = 8
    


  

  def is_saloon(self): #if the cat type is not a trailer, then the car type is a saloon
    if self.vehicle_type is not 'trailer':
        self.vehicle_type == 'saloon'
        return True
    return False
  
  
  
  
  def drive(self, moving_speed): #testing whether the vehicle is moving
    if moving_speed == 3:
      self.speed = 1000
    elif moving_speed == 7:
      self.speed = 77

    return self
    
  