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
        self.score = 0

    def home_value_score(self):
        # TODO Replace with value function, then update self.score with it.
        self.assertEqual(True, False)


def read_from_file_pandas():
    houses_read = pandas.read_csv('houses.csv')
    houses_read = houses_read.sort_values('Price')
    houses_processing_list = houses_read.values.tolist()
    houses_list = []
    # print(house_address)
    for h in houses_processing_list:
        address = h[0]
        city = h[1]
        state = h[2]
        price = h[3]
        num_beds = h[4]
        num_baths = h[5]
        sq_footage = h[6]
        year_built = h[8]
        garage = h[9]
        backyard = h[10]
        basement = h[11]
        houses_list.append(HouseNode(address, city, state, price, num_beds, num_baths, sq_footage, year_built, garage, backyard, basement))

    return houses_list



