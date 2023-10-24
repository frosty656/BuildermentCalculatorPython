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