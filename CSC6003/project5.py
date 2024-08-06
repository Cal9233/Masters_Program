#User Class that sets username and Users Music_Collection class
class User:
    def __init__(self, username):
        self.user = username
        self.music_collection = Music_Collection()

#Music_Collection class with methods for Users playlist
class Music_Collection:
    def __init__(self):
        self.playlist = {}

    #User adds song with some condtions
    def add_song(self, title, artist):
        if title in self.playlist:
            print(f"Song {title} is already in your playlist.")
        else:
            self.playlist[title] = artist
            print(f"{title} by {artist} was added to your playlist.")

    #User deletes song with some condtions
    def delete_song(self, title):
        if title not in self.playlist:
            print(f"{title} does not exist in your playlist.")
        else:
            del self.playlist[title]
            print(f"{title} was deleted from your playlist.")

    #User gets song details with some condtions
    def get_song_details(self, title):
        artist = self.playlist.get(title)
        if artist:
            print(f"{title} is by {artist}.")
        else:
            print(f"{title} does not exist in your playlist.")

    #User updates song details with some condtions
    def update_song_details(self, title, new_artist):
        if title in self.playlist:
            self.playlist[title] = new_artist
            print(f"Updated {title} to be by {new_artist}.")
        else:
            print(f"{title} does not exist in your playlist.")

    #User displays all songs with some condtions
    def display_all_songs(self):
        if not self.playlist:
            print(f"You currently have no songs in your playlist.")
        else:
            print("These are your current songs in your playlist:")
            for title, artist in self.playlist.items():
                print(f"{title} by {artist}")

#Music_Collection_Organizer Class which contains all User data and playlist data
class Music_Collection_Organizer:
    def __init__(self):
        self.users = {}
        self.current_user = None

    #Creates User with some conditions
    def add_user(self, name):
        if name in self.users:
            print(f"User {name} already exists.")
        else:
            self.users[name] = User(name)
            self.current_user = self.users[name]
            print(f"User {name} created and set as the current user.")

    #Changes User with some conditions
    def change_user(self, name):
        if self.current_user and self.current_user.user == name:
            print(f"You're already logged in as this User.")
        elif name in self.users:
            self.current_user = self.users[name]
            print(f"Changed to user '{name}'.")
        else:
            print(f"User {name} does not exist.")

    #Adds song based off of User with some conditions
    def add_song(self, title, artist):
        if self.current_user:
            self.current_user.music_collection.add_song(title, artist)
        else:
            print("No user selected. Please change to a user first.")

    #Retrieves song details based off of User with some conditions
    def retrieve_song_details(self, title):
        if self.current_user:
            self.current_user.music_collection.get_song_details(title)
        else:
            print("No user selected. Please change to a user first.")

    #Updates song details based off of User with some conditions
    def update_song_details(self, title, new_artist):
        if self.current_user:
            self.current_user.music_collection.update_song_details(title, new_artist)
        else:
            print("No user selected. Please change to a user first.")

    #Deletes songs based off of User with some conditions
    def delete_song(self, title):
        if self.current_user:
            self.current_user.music_collection.delete_song(title)
        else:
            print("No user selected. Please change to a user first.")

    #Displays all songs based off of User with some conditions
    def display_all_songs(self):
        if self.current_user:
            self.current_user.music_collection.display_all_songs()
        else:
            print("No user selected. Please change to a user first.")

def main():
    #Initiates Music_Collection_Organizer class
    organizer = Music_Collection_Organizer()
    while True:
        #Starts program by first creating a user
        if not organizer.current_user:
            print('Please create a user to use the Music Collection')
            username = input("Enter username: ").strip()
            if len(username) == 0 :
                print("Please input a valid username.")
            else: 
                organizer.add_user(username)
        else:            
            # Check if playlist is empty before showing update options
            playlist = organizer.current_user.music_collection.playlist
            user_list = organizer.users
            print("\nOptions (You can input the numbers for a shorter input): \n 1: add_user, \n 2: change_user, \n 3: add_song, \n 4: retrieve_song_details, \n 5: update_song_details, \n 6: delete_song, \n 7: display_all_songs, \n 8: quit")
            option = input("Choose an option: ").strip().lower()

            # Created to allow user input shortcut by using integers
            if option.isdigit():
                option = int(option)

            #List of User commands

            #add user command
            if option == 1 or option == "add_user":
                username = input("Enter username: ").strip()
                if len(username) == 0 :
                    print("Please input a valid username.")
                else: 
                    organizer.add_user(username)

            #change user command
            elif option == 2 or option == "change_user":
                if len(user_list.values()) <= 1:
                    print("No other Users to change to.")
                else:
                    username = input("Enter username: ").strip()                
                    if len(username) == 0 :
                        print("Please input a valid username.")
                    else: 
                        organizer.change_user(username)

            #add song command
            elif option == 3 or option == "add_song":
                title = input("Enter song title: ").strip()
                artist = input("Enter artist: ").strip()
                if len(title) == 0 or len(artist) == 0:
                    print("Please input a valid song or artist.")
                else: 
                    organizer.add_song(title, artist)

            #retrieve song details command
            elif option == 4 or option == "retrieve_song_details":
                if playlist:  # Double-check if playlist is not empty before proceeding
                    title = input("Enter song title: ").strip()
                    if len(title) == 0:
                        print("Please input a valid song.")
                    else: 
                        organizer.retrieve_song_details(title)
                else:
                    print("Your playlist is empty. There are no songs details to retrieve from.") 

            #update song details command
            elif option == 5 or option == "update_song_details":
                if playlist:  # Double-check if playlist is not empty before proceeding
                    title = input("Enter song title: ").strip()
                    new_artist = input("Enter new artist: ").strip()
                    if len(title) == 0 or len(new_artist) == 0:
                        print("Please input a valid song or artist.")
                    else:
                        organizer.update_song_details(title, new_artist)
                else:
                    print("Your playlist is empty. There are no songs to update.")

            #delete song command
            elif option == 6 or option == "delete_song":
                if playlist:  # Double-check if playlist is not empty before proceeding
                    title = input("Enter song title: ").strip()
                    if len(title) == 0:
                        print("Please input a valid song.")
                    else: 
                        organizer.delete_song(title)
                else:
                    print("Your playlist is empty. There are no songs to delete.")
                    
            #display all songs command
            elif option == 7 or option == "display_all_songs":
                if playlist:  # Double-check if playlist is not empty before proceeding
                    organizer.display_all_songs()
                else:
                    print("Your playlist is empty. There are no songs to display.")

            #quit command
            elif option == 8 or option == "quit":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
#main program
if __name__ == "__main__":
    main()