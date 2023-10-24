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

def level_multiplier(level):
    if level == 1:
        return 1
    elif level == 2:
        return 1.5
    elif level == 3:
        return 2
    elif level == 4:
        return 3
    elif level == 5:
        return 4
    else:
        return 1
    
def get_building_level(name):
    name_lower = name.lower()
    
    if name_lower == "workshop":
        return workshopLevel
    elif name_lower == "furnace":
        return furnaceLevel
    elif name_lower == "machine shop":
        return machineShopLevel
    elif name_lower == "industrial factory":
        return industrialFactoryLevel
    elif name_lower == "forge":
        return forgeLevel
    elif name_lower == "manufacturer":
        return manufacturerLevel
    elif name_lower == "extractor":
        return extractorLevel
    elif name_lower == "earth transporter":
        return 1
    else:
        return 1

def get_extractor_count_by_resource(variable_name):
    variable_name_lower = variable_name.lower()

    if variable_name_lower == "copper ore":
        return copperOreExtractor
    elif variable_name_lower == "iron ore":
        return ironOreExtractor
    elif variable_name_lower == "wood log":
        return woodLogExtractor
    elif variable_name_lower == "stone":
        return stoneExtractor
    elif variable_name_lower == "coal":
        return coalExtractor
    elif variable_name_lower == "wolframite":
        return wolframiteExtractor
    else:
        return 1

def calculateResourceUsageForRecipe(recipeName, depth = 0):
    tabs = "  " * depth
    print(tabs, end="")
    print(f"{recipeName}")

    # Define our base case (prevent infinite loop)
    if recipeName in rawResources:
        # Get the number of extractors for specific resource
        numberOfExtractors = get_extractor_count_by_resource(recipeName)

        # Get the base production of the extractors
        baseProduction = numberOfExtractors * 7.5

        # Get the level of the extractor
        extractorLevel = get_building_level("extractor")

        # Get the output level multiplier
        levelMultiplier = level_multiplier(extractorLevel)

        # Apply for level multiplier
        finalProduction = baseProduction * levelMultiplier

        return finalProduction

    # Keep going down the ingredient list
    for recipe in recipes:
        if recipe["name"] == recipeName:
            # We want to know the potential output given an ingredient
            totalAmounts = []
            for subRecipe in recipe["ingredientList"]:
                # Get the amount of the ingredient we can hypothetically get
                incomingResources = calculateResourceUsageForRecipe(subRecipe["name"], depth + 1)

                # Get the potential yield for the given amount of the ingredient
                potentialYield = incomingResources / subRecipe["amount"]

                # Add it to the list of potential yields
                totalAmounts.append(potentialYield)
            
            # Since we can only make as much as our lowest resource allows return the yield from that
            return min(totalAmounts)

# Actually start the script
resourceToMax = "Copper Wire" #input("Name of resource you would like to maximize: ")

for recipe in recipes:
    if recipe["name"] == resourceToMax:
        result = calculateResourceUsageForRecipe(recipe["name"])
        print(f"{result} / min")
