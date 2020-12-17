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
        # testing = TestingPreferences()
        testing = home_preferences
        running_score = 0
        # Bedroom Scoring
        bedroom_scoring = - (self.num_beds - testing.num_beds)
        if bedroom_scoring == 0:
            running_score = running_score + 1
        elif bedroom_scoring > 1:
            running_score = running_score + .5
        elif bedroom_scoring < 1:
            running_score = running_score + .75

        # Bathroom Scoring
        bathroom_scoring = - (self.num_baths - testing.num_baths)
        if bathroom_scoring == 0:
            running_score = running_score + 1
        elif bathroom_scoring > 1:
            running_score = running_score + .5
        elif bathroom_scoring < 1:
            running_score = running_score + .75

        # SqFoot Score
        sqfoot_scoring = - (self.sq_footage - testing.sq_footage)
        if sqfoot_scoring == 0:
            running_score = running_score + 1
        elif sqfoot_scoring > 500:
            running_score = running_score + .8
        elif sqfoot_scoring > 1000:
            running_score = running_score + .75

        # Basement
        if self.basement == testing.basement:
            running_score = running_score + 1
        else:
            running_score = running_score + .3

        # Garage
        if self.garage == testing.garage:
            running_score = running_score + 1
        else:
            running_score = running_score + .3

        # Backyard
        if self.backyard == testing.backyard:
            running_score = running_score + 1
        else:
            running_score = running_score + .3

        running_normalized = running_score / 6
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
        sq_footage = h[5]
        garage = h[7]
        backyard = h[8]
        basement = h[9]
        houses_list.append(HouseNode(address, city_state, price, num_beds, num_baths, sq_footage, garage, backyard, basement))
    return houses_list



