

class Band:
    instances=[]

    def __init__(self,name,members=None):
        self.name=name
        self.members=members
        Band.instances.append(name)

    
    def __str__(self):
        return f"The Band name is : {self.name}"

    def __repr__(self):
        return f"Band instance name is : {self.name},members ={self.members}"

    def play_solos(self):
        solo_array=[]
        for i in self.members:
            solo_array.append(i.play_solo())
        return solo_array

    @classmethod
    def to_list(cls):
        return cls.instances



class Musician :

    def __init__(self,name,instrument,role,solo):
        self.name=name
        self.instrument=instrument
        self.role=role
        self.solo=solo

    def __str__(self):
        return f'my name is : {self.name} and i play on this instrument : {self.instrument}'

    def __repr__(self):
         return f'{self.role} instance , name is : {self.name}'

    def get_instrument(self):
        return f'{self.instrument}'

    def play_solo(self):
        return f'{self.solo}'



class Guitarist(Musician):

    def __init__ (self,name):
        super.__init__(name,"guetar","Guitarist","  Reed MusicKen Murray ")


class Bassist(Musician):

    def __init__ (self,name):
        super.__init__(name,"bass","Bassist","Dragonetti 12 Waltzes sheet music for double-bass solo ")
 



class Drummer(Musician):

    def __init__ (self,name):
        super.__init__(name,"drums","Drummer","Guitarist","Tail Spin , Snare Drum Solo     ")


if __name__=="__main__":
    # test the classes here 

    print(Band.to_list()==[])
    Band("the nobody",[])
    eman=Guitarist("EMAN")
    print(Musician.to_all())





  
