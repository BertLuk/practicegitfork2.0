"""
This program generates passages that are generated in mad-lib format
Author: Luke 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
print "It's time for Madlibs my BOIS"
name = raw_input("Name:")
noun = raw_input("First Noun:")
noun_1 = raw_input("Second Noun:")
adjective = raw_input("First Adjective:")
adjective_1 = raw_input("Second Adjective:")
adjective_2 = raw_input("Third Adjective:")
animal = raw_input("Animal:")
food = raw_input("Food:")
verb = raw_input("Verb:")
fruit = raw_input("Fruit:")
superhero = raw_input("Superhero:")
country = raw_input("Country:")
dessert = raw_input("Dessert:")
year = raw_input("Year:")

print STORY % (name, adjective, adjective_1, animal, food, verb, noun, fruit, adjective_2, name, superhero, name, country, name, dessert, name, year, noun_1)