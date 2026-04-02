from abc import ABC, abstractmethod

class Pizza:

    def __init__(self, name:str):
        self.name = name
    
    def __repr__(self):
        return f"{self.name}"
    


        