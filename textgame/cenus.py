class Person:
    def __init__(self,name,age,favorite_foods):
        self.name = name
        self.age = age
        self.favorite_foods = favorite_foods

    def birth_year(self):
        return 2020 - self.age

    def __str__(self): #Equivalent of overriding toString() in Java - NEAT!
        return "Name: {} Age: {} Favorite Food: {}".format(self.name,self.age,self.favorite_foods)


#Now create some objects
people = [Person("Ed",11,["hotdogs","jawbreakers"]), Person("Edd",11,["broccoli"]), Person("Eddy",12,["chunky puffs","jawbreakers"]) ]

age_sum = 0
year_sum = 0

for dude in people:
    age_sum = age_sum + dude.age
    year_sum = year_sum + dude.birth_year()

print("The average age is: " + str( int(age_sum / len(people) )))
print("The average birth year is: " + str( int(year_sum / len(people) ))  + "\n" )

print("These dumb ass kids:")
for dudes in people:
    print(dudes)