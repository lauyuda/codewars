def cakes(recipe, available):
    minimum = 0
    for ingredient in recipe:
        if ingredient not in available:
            return 0
        elif available[ingredient] < recipe[ingredient]:
            return 0
        elif minimum == 0:
            minimum = available[ingredient] // recipe[ingredient]
        else:
            if available[ingredient] // recipe[ingredient] < minimum:
                minimum = available[ingredient] // recipe[ingredient]
    return minimum