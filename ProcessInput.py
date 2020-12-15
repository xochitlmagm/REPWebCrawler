import pandas
import UserInterface


class HouseNode:
    def __init__(self, address, city, state, price, num_beds, num_baths, sq_footage, lot, backyard, garage, basement):
        self.address = address
        self.city = city
        self.state = state
        self.price = price
        self.num_beds = num_beds
        self.num_baths = num_baths
        self.sq_footage = sq_footage
        self.lot = lot
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

        # TODO Replace with value function, then update self.score with it.

        running_normalized = running_score / 6
        self.score = running_normalized
        return running_normalized


def read_from_file_pandas():
    houses_read = pandas.read_csv('houses.csv')
    houses_read = houses_read.sort_values('Price')
    houses_processing_list = houses_read.values.tolist()
    houses_list = []
    for h in houses_processing_list:
        address = h[1]
        city = h[2]
        state = h[3]
        price = h[4]
        num_beds = h[5]
        num_baths = h[6]
        sq_footage = h[7]
        year_built = h[9]
        garage = h[10]
        backyard = h[11]
        basement = h[12]
        houses_list.append(HouseNode(address, city, state, price, num_beds, num_baths, sq_footage, year_built, garage,
                                     backyard, basement))

    return houses_list



