class Student:
    school= "Akirachix"
    def __init__(self,name,age,country,first_name,last_name):
        self.name=name
        self.age=age
        self.country=country
        self.first_name=first_name
        self.last_name=last_name
    
    def greeting(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"

    def full_name(self):
        return f"Your name is {self.first_name} {self.last_name}"

    def year_of_birth(self):
        year=2022-self.age
        return f"You were born in {year}"

    def initials(self):
        initial=f"{self.first_name[0]}{self.last_name[0]}"
        return f"your initials are {initial}"
        
