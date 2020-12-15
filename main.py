import ProcessInput
import UserInterface


class TestingPreferences:
    def __init__(self, num_beds=3, num_baths=2, sq_footage=1900, backyard=True, garage=True, basement=False):
        self.num_beds = num_beds
        self.num_baths = num_baths
        self.sq_footage = sq_footage
        self.backyard = backyard
        self.garage = garage
        self.basement = basement


if __name__ == '__main__':
    houses = ProcessInput.read_from_file_pandas()

    # This is where we need to build the UI and get preferences from user
    # stored_preferences_from_user = UserInterface.BuildUI()

    # Once the user has filled out preferences, we want to determine the appropriate value score for the homes
    # we've have in our 'search'.
    for home in houses:
        preference_object = TestingPreferences();
        home.score = home.home_value_score(preference_object)
        # print(f'Address: {home.address}, Score: {home.score}')

    # Sorting houses by score in desc order
    houses.sort(reverse=True, key=lambda x: x.score)

    # Take the top results and display them for user!

    # TODO Remove this when the preferences are stored from the user input and not hard
    #  coded in
    UserInterface.BuildUI()

