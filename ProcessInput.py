import pandas


class HouseNode:
    def __init__(self, address, city_state, price, num_beds, num_baths, sq_footage, backyard, garage, basement):
        self.address = address
        self.city_state = city_state
        self.price = price
        self.num_beds = num_beds
        self.num_baths = num_baths
        self.sq_footage = sq_footage
        self.backyard = backyard
        self.garage = garage
        self.basement = basement
        self.score = 0.0

    def home_value_score(self, home_preferences):
        preferences = home_preferences
        running_score = 0
        # Bedroom Scoring

        bedroom_scoring = - (self.num_beds - preferences.num_beds)
        bedroom_score = 0
        if bedroom_scoring == 0:
            bedroom_score = 1
        elif bedroom_scoring > 1:
            bedroom_score = .75
        elif bedroom_scoring < 1:
            bedroom_score = .5

        if preferences.highestPreference == 'Bedrooms':
            bedroom_score = 3 * bedroom_score
        elif preferences.secondHighestPreference == 'Bedrooms':
            bedroom_score = 2 * bedroom_score
        running_score = running_score + bedroom_score

        # Bathroom Scoring
        bathroom_scoring = - (self.num_baths - preferences.num_baths)
        bathroom_score = 0
        if bathroom_scoring == 0:
            bathroom_score = 1
        elif bathroom_scoring > 1:
            bathroom_score = .75
        elif bathroom_scoring < 1:
            bathroom_score = .5

        if preferences.highestPreference == 'Bathrooms':
            bathroom_score = 3 * bathroom_score
        elif preferences.secondHighestPreference == 'Bathrooms':
            bathroom_score = 2 * bathroom_score
        running_score = running_score + bathroom_score

        # SqFoot Score
        sqfoot_scoring = - (self.sq_footage - int(preferences.sq_foot))
        sqfoot_score = 0;
        if sqfoot_scoring == 0:
            sqfoot_score = 1
        elif sqfoot_scoring > 500:
            sqfoot_score = .8
        elif sqfoot_scoring > 1000:
            sqfoot_score = .75

        if preferences.highestPreference == 'Sq Footage':
            sqfoot_score = 3 * sqfoot_score
        elif preferences.secondHighestPreference == 'Sq Footage':
            sqfoot_score = 2 * sqfoot_score
        running_score = running_score + sqfoot_score

        # Basement
        basement_score = 0
        if self.basement == preferences.basement:
            basement_score = 1
        else:
            basement_score = .5

        if preferences.highestPreference == 'Basement':
            basement_score = 3 * basement_score
        elif preferences.secondHighestPreference == 'Basement':
            basement_score = 2 * basement_score
        running_score = running_score + basement_score

        # Garage
        garage_score = 0
        if self.garage == preferences.garage:
            garage_score = 1
        else:
            garage_score = .5

        if preferences.highestPreference == 'Garage':
            garage_score = 3 * garage_score
        elif preferences.secondHighestPreference == 'Garage':
            garage_score = 2 * garage_score
        running_score = running_score + garage_score

        # Backyard
        backyard_score = 0
        if self.backyard == preferences.backyard:
            backyard_score = 1
        else:
            backyard_score = .5

        if preferences.highestPreference == 'Backayard':
            backyard_score = 3 * backyard_score
        elif preferences.secondHighestPreference == 'Backyard':
            backyard_score = 2 * backyard_score
        running_score = running_score + backyard_score

        running_normalized = running_score / (6 + 2 + 1)
        self.score = running_normalized
        return running_normalized


def read_house_list_from_file(filename):
    houses_read = pandas.read_csv(filename)
    houses_read = houses_read.sort_values('Price')
    houses_processing_list = houses_read.values.tolist()
    houses_list = []
    for h in houses_processing_list:
        address = h[1]
        city_state = h[2]
        price = h[3]
        num_beds = h[4]
        num_baths = h[6]
        sq_int = int(h[5].replace(',', ''))
        sq_footage = sq_int
        garage = h[7]
        backyard = h[8]
        basement = h[9]
        houses_list.append(
            HouseNode(address, city_state, price, num_beds, num_baths, sq_footage, garage, backyard, basement))
    return houses_list


class TestingPreferences:
    def __init__(self, num_beds, num_baths, sq_footage, backyard, garage, basement, pref1, pref2):
        self.num_beds = num_beds
        self.num_baths = num_baths
        self.sq_foot = sq_footage
        self.backyard = backyard
        self.garage = garage
        self.basement = basement
        self.highestPreference = pref1
        self.secondHighestPreference = pref2
