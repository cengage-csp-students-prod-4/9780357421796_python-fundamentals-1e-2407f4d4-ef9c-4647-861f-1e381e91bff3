# Write your MoviePlayer class here
class MoviePlayer:
    firmware_version = 1.0
    current_movie = ""
    __movie_list = []

    def __init__(self):
        self.__movie_list = ["Surfs Up", "Beauty and the Beast", "Chicken Little"]

    def update_firmware(self, version):
        self.firmware_version = version

    def play(self):
        self.current_movie = self.__movie_list[0]

    def list_movies(self):
        print(self.__movie_list)



# The code below is used to test your class
if __name__ == '__main__':
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    print("Updated player firmware version to", player.firmware_version)

    player.play()
    print("Currently playing", f"'{player.current_movie}'")

