#Inheritence Practice
class Location:

    def __init__(self,name,year,population):
        self.year = year
        self.name = name
        self.population = population

    def get_population(self):
        return self.population

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    # TODO: add functionality for sorting location by year
    def sort_by_year(self):
        return False;
    
    # TODO: add functionality for sorting location by name alphabetically 
    def sort_by_name(self):
        return False;
    
    # TODO: add functionality for sorting location by population
    def sort_by_population(self):
        return False;

class State(Location):

    counties = []

    def __init__(self,name,year,population):
        super().__init__(name,year,population)
        
        #potentially change to dictionary
        self.cities = [] 
    
    #Decorator Example
    @classmethod
    def add_counties(cls,city):
        cls.counties.append(city)

    def __str__(self):
        return(f"State: {self.name} Year: {self.year} Population: {self.population} Counties: {State.counties} Cities: {self.cities}")


class County(Location):
    def __init__(self, name, year, population):
        super().__init__(name, year, population)
        self.cities = []
    
    def __str__(self):
        return(f"State: {self.name} Year: {self.year} Population: {self.population} Cities: {self.cities}")

class City(Location):
    def __init__(self, name, year, population):
        super().__init__(name, year, population)

# state = State("Idaho",2022,198000)
# print(state)
# state.add_counties("Ada")
# print(state)