import json

# Read the raw resources
with open('rawResources.json', 'r') as file:
    rawResources = json.load(file)

# Read the recipes
with open('Recipes.json', 'r') as file:
    recipes = json.load(file)

# Define all of our levels
workshopLevel = 1
furnaceLevel = 1
machineShopLevel = 1
industrialFactoryLevel = 1
forgeLevel = 1
manufacturerLevel = 1
extractorLevel = 1

# Track number of extractors
copperOreExtractor = 10
ironOreExtractor = 10
woodLogExtractor = 10
stoneExtractor = 10
coalExtractor = 10
wolframiteExtractor = 10

# We also want belt speed
beltItemsPerMinute = 420

def calculateResourceUsageForRecipe(recipeName, depth = 0):
    tabs = "  " * depth
    print(tabs, end="")
    print(f"{recipeName}")

    # Define our base case (prevent infinite loop)
    if recipeName in rawResources:
        return

    for recipe in recipes:
        if recipe["name"] == recipeName:
            for subRecipe in recipe["ingredientList"]:
                calculateResourceUsageForRecipe(subRecipe["name"], depth + 1)

# Actually start the script
resourceToMax = "Electromagnet" #input("Name of resource you would like to maximize: ")

for recipe in recipes:
    if recipe["name"] == resourceToMax:

        calculateResourceUsageForRecipe(recipe["name"])