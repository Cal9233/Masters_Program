import os
import json

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
        """
        Adds a song to the playlist.

        Args:
            title (str): The title of the song
            artist (str): The artist of the song

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        Judas by Lady Gaga was added to your playlist.
        >>> mc.add_song("Judas", "Lady Gaga")
        Song Judas is already in your playlist.
        """
        if title in self.playlist:
            print(f"Song {title} is already in your playlist.")
        else:
            self.playlist[title] = artist
            print(f"{title} by {artist} was added to your playlist.")

    #User deletes song with some condtions
    def delete_song(self, title):
        """
        Deletes a song to the playlist.

        Args:
            title (str): The title of the song

        >>> mc = Music_Collection()
        >>> mc.delete_song("Judas")
        Judas was deleted from your playlist.
        >>> mc.delete_song("Judas")
        Judas does not exist in your playlist.
        """
        if title not in self.playlist:
            print(f"{title} does not exist in your playlist.")
        else:
            del self.playlist[title]
            print(f"{title} was deleted from your playlist.")

    #User gets song details with some condtions
    def get_song_details(self, title):
        """
        Gets song details from playlist.

        Args:
            title (str): The title of the song

        >>> mc = Music_Collection()
        >>> mc.get_song_details("Judas")
        Judas is by Lady Gaga.
        >>> mc.get_song_details("Judas")
        Judas does not exist in your playlist.
        """
        artist = self.playlist.get(title)
        if artist:
            print(f"{title} is by {artist}.")
        else:
            print(f"{title} does not exist in your playlist.")

    #User updates song details with some condtions
    def update_song_details(self, title, new_artist):
        """
        Updates song details from playlist.

        Args:
            title (str): The title of the song
            new_artist (str): The updated artist of the song

        >>> mc = Music_Collection()
        >>> mc.update_song_details("Judas", "Linkin Park")
        Updated Judas to be by Linkin Park.
        >>> mc.update_song_details("Judas", "Linkin Park")
        Judas does not exist in your playlist.
        """
        if title in self.playlist:
            self.playlist[title] = new_artist
            print(f"Updated {title} to be by {new_artist}.")
        else:
            print(f"{title} does not exist in your playlist.")

    #User displays all songs with some condtions
    def display_all_songs(self):
        """
        Display all songs from playlist.

        >>> mc = Music_Collection()
        >>> mc.display_all_songs()
        These are your current songs in your playlist:
        Judas by Lady Gaga
        >>> mc.display_all_songs()
        You currently have no songs in your playlist.
        """
        if not self.playlist:
            print(f"You currently have no songs in your playlist.")
        else:
            print("These are your current songs in your playlist:")
            for title, artist in self.playlist.items():
                print(f"{title} by {artist}")

    def load_playlist(self, filename):
        """
        Loads the playlist from a JSON file.
        
        Args:
            filename (str): The name of the file to load the playlist from.

        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        ...     tf.write('{"Judas": "Lady Gaga"}')
        ...     temp_filename = tf.name
        >>> mc = Music_Collection()
        >>> mc.load_playlist(temp_filename)
        >>> mc.playlist
        {'Judas': 'Lady Gaga'}
        >>> import os
        >>> os.unlink(temp_filename)
        >>> mc.load_playlist("non_existent_file.json")
        'File non_existent_file.json not found. Starting with an empty playlist.'
        """
        try:
            with open(filename, 'r') as file:
                self.playlist = json.load(file)
        except FileNotFoundError:
            return f"File {filename} not found. Starting with an empty playlist."
        except json.JSONDecodeError:
            return f"File {filename} is not a valid JSON file. Starting with an empty playlist."

    def save_playlist(self, filename):
        """
        Saves the playlist to a JSON file.
        
        Args:
            filename (str): The name of the file to save the playlist to.

        >>> import tempfile
        >>> import os
        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        ...     temp_filename = tf.name
        >>> mc.save_playlist(temp_filename)
        >>> with open(temp_filename, 'r') as f:
        ...     saved_content = f.read()
        >>> saved_content
        '{"Judas": "Lady Gaga"}'
        >>> os.unlink(temp_filename)
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.playlist, file)
        except IOError:
            return f"Error writing to file {filename}."

#Music_Collection_Organizer Class which contains all User data and playlist data
class Music_Collection_Organizer:
    def __init__(self):
        self.users = {}
        self.current_user = None

    #Creates User with some conditions
    def add_user(self, name):
        """
        Create new User and add to Users list.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_user("Cal")
        User Cal already exists.
        """
        if name in self.users:
            print(f"User {name} already exists.")
        else:
            self.users[name] = User(name)
            self.current_user = self.users[name]
            self.load_user_playlist(name)
            print(f"User {name} created and set as the current user.")

    #Changes User with some conditions
    def change_user(self, name):
        """
        Change User from Users list.

        >>> mco = Music_Collection_Organizer()
        >>> mco.change_user("Al")
        Changed to user 'Al'.
        >>> mco.change_user("Zach")
        User Zach does not exist.
        >>> mco.change_user("Cal")
        You're already logged in as this User.
        """
        if self.current_user and self.current_user.user == name:
            print(f"You're already logged in as this User.")
        elif name in self.users:
            self.save_user_playlist(self.current_user.user)
            self.current_user = self.users[name]
            print(f"Changed to user '{name}'.")
        else:
            print(f"User {name} does not exist.")

    #Adds song based off of User with some conditions
    def add_song(self, title, artist):
        """
        Adds a song to the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_song("Imagine", "John Lennon")
        Imagine by John Lennon was added to your playlist.
        >>> mco.change_user("Bob")
        User Bob does not exist.
        >>> mco.add_user("Bob")
        User Bob created and set as the current user.
        >>> mco.add_song("Hey Jude", "The Beatles")
        Hey Jude by The Beatles was added to your playlist.
        """
        if self.current_user:
            self.current_user.music_collection.add_song(title, artist)
        else:
            print("No user selected. Please change to a user first.")

    #Retrieves song details based off of User with some conditions
    def retrieve_song_details(self, title):
        """
        Retrieves song details from the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_song("Imagine", "John Lennon")
        Imagine by John Lennon was added to your playlist.
        >>> mco.retrieve_song_details("Imagine")
        Imagine is by John Lennon.
        >>> mco.retrieve_song_details("Hey Jude")
        Hey Jude does not exist in your playlist.
        """
        if self.current_user:
            self.current_user.music_collection.get_song_details(title)
        else:
            print("No user selected. Please change to a user first.")

    #Updates song details based off of User with some conditions
    def update_song_details(self, title, new_artist):
        """
        Updates song details in the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_song("Imagine", "John Lennon")
        Imagine by John Lennon was added to your playlist.
        >>> mco.update_song_details("Imagine", "The Beatles")
        Updated Imagine to be by The Beatles.
        >>> mco.update_song_details("Hey Jude", "The Beatles")
        Hey Jude does not exist in your playlist.
        """
        if self.current_user:
            self.current_user.music_collection.update_song_details(title, new_artist)
        else:
            print("No user selected. Please change to a user first.")

    #Deletes songs based off of User with some conditions
    def delete_song(self, title):
        """
        Deletes a song from the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_song("Imagine", "John Lennon")
        Imagine by John Lennon was added to your playlist.
        >>> mco.delete_song("Imagine")
        Imagine was deleted from your playlist.
        >>> mco.delete_song("Imagine")
        Imagine does not exist in your playlist.
        """
        if self.current_user:
            self.current_user.music_collection.delete_song(title)
        else:
            print("No user selected. Please change to a user first.")

    #Displays all songs based off of User with some conditions
    def display_all_songs(self):
        """
        Displays all songs in the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        User Cal created and set as the current user.
        >>> mco.add_song("Imagine", "John Lennon")
        Imagine by John Lennon was added to your playlist.
        >>> mco.add_song("Given Up", "Linkin Park")
        Given Up by Linkin Park was added to your playlist.
        >>> mco.add_song("Judas", "Lady Gaga")
        Judas by Lady Gaga was added to your playlist.
        >>> mco.display_all_songs()
        These are your current songs in your playlist:
        Imagine by John Lennon
        Given Up by Linkin Park
        Judas by Lady Gaga
        """
        if self.current_user:
            self.current_user.music_collection.display_all_songs()
        else:
            print("No user selected. Please change to a user first.")
    
    def save_user_playlist(self, username):
        """
        Saves the current user's playlist to a JSON file.

        Args:
            username (str): The username of the current user.
        
        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("TestUser")
        'User TestUser created and set as the current user.'
        >>> mco.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mco.save_user_playlist("TestUser")
        >>> import os
        >>> os.path.exists("TestUser_playlist.json")
        True
        >>> os.unlink("TestUser_playlist.json")
        """
        filename = f"{username}_playlist.json"
        return self.users[username].music_collection.save_playlist(filename)

    def load_user_playlist(self, username):
        """
        Loads the current user's playlist from a JSON file.

        Args:
            username (str): The username of the current user.
        
        >>> import tempfile
        >>> with tempfile.NamedTemporaryFile(mode='w', delete=False) as tf:
        ...     tf.write('{"Judas": "Lady Gaga"}')
        ...     temp_filename = tf.name
        >>> import os
        >>> os.rename(temp_filename, "TestUser_playlist.json")
        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("TestUser")
        'User TestUser created and set as the current user.'
        >>> mco.load_user_playlist("TestUser")
        >>> mco.current_user.music_collection.playlist
        {'Judas': 'Lady Gaga'}
        >>> os.unlink("TestUser_playlist.json")
        """
        filename = f"{username}_playlist.json"
        return self.users[username].music_collection.load_playlist(filename)

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
                if organizer.current_user:
                    organizer.save_user_playlist(organizer.current_user.user)
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
#main program
#import doc test
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()