import re
import pandas as pd


class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients


class Ingredient:
    def __init__(self, name, mention, quantity, energy):
        self.name = name
        self.mention = mention
        self.quantity = quantity
        self.energy = energy


def read_recipes(file_name):
    recipes = []

    with open(f'files/{file_name}') as file:
        recipe = None

        for line in file:
            # beginning of a new recipe
            line = line.strip()
            if line.startswith('Varianta'):
                if recipe is not None:
                    recipes.append(recipe)
                recipe = Recipe(line.split(":", 1)[1].strip(' -:'))
            # otherwise it means it is an ingredient
            else:
                line = line.strip(' -')
                mention = re.search('\\((.*)\\)', line)
                if mention is not None:
                    mention = mention.group(1).strip()
                    line = line.replace(mention, '')
                name = line.split('-', 1)[0].strip(' ()')
                quantity = line.split('-', 1)[1]
                if quantity.__contains__('='):
                    quantity = quantity.split('=', 1)[0]
                energy = re.search('=(.*)', line)
                if energy is not None:
                    energy = energy.group(1).strip()

                recipe.add_ingredient(Ingredient(name, mention, quantity, energy))

    return recipes


def write_recipes_to_sheet(recipes, sheet, writer):
    data = {'Recipe': [], 'Ingredient': [], 'Mentiuni': [], 'Cantitate': [], 'Energie': []}
    for recipe in recipes:
        for ingredient in recipe.ingredients:
            data['Recipe'].append(recipe.name)
            data['Ingredient'].append(ingredient.name)
            data['Mentiuni'].append(ingredient.mention)
            data['Cantitate'].append(ingredient.quantity)
            data['Energie'].append(ingredient.energy)

    df = pd.DataFrame(data=data)
    df.to_excel(writer, sheet)


with pd.ExcelWriter('files/Dieta.xlsx') as writer:
    write_recipes_to_sheet(read_recipes('mic_dejun.txt'), 'Mic_dejun', writer)
    write_recipes_to_sheet(read_recipes('pranz_cina.txt'), 'Pranz_cina', writer)
    write_recipes_to_sheet(read_recipes('gustari.txt'), 'Gustari', writer)

