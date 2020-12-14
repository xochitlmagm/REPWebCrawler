import ProcessInput
import UserInterface

if __name__ == '__main__':
    houses = ProcessInput.read_from_file_pandas()
    for l in houses:
        print(l.address)
    UserInterface.BuildUI()

