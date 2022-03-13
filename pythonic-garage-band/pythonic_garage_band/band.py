from abc import ABC ,abstractmethod

class Band:
    instances=[]

    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.instances.append(self)

    
   
    def play_solos(self):
        solo_array=[]
        for member in self.members:
            solo_array.append(member.play_solo())
        return solo_array

    @classmethod
    def to_list(cls):
        return cls.instances


    def __str__(self):
        return f"The Band name is : {self.name}"

    def __repr__(self):
        return f"Band instance name is : {self.name},members ={self.members}"

class Musician(ABC) :
    """
    this class represents Musician (ABSTRACT)
    methods: play_solo()
    """
    def __init__(self,name):
        self.name=name
       
         

    def __str__(self):
        return f'my name is : {self.name} and i play on this instrument : {self.instrument}'

    def __repr__(self):
         return f'{self.role} instance , name is : {self.name}'

    def get_instrument(self):
        return f'{self.instrument}'

    def play_solo(self):
        return f'{self.solo}'



class Guitarist(Musician):

    def get_instrument(self):
        return "guitar"

    
    def play_solo(self):
        return "face melting guitar solo"

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
     
class Bassist(Musician):

    def get_instrument(self):
        return "bass"

    
    def play_solo(self):
        return "bom bom buh bom"

    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
     


class Drummer(Musician):

     def get_instrument(self):
        return "drums"

    
     def play_solo(self):
        return "rattle boom crash"

     def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
     def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

 
     





  
