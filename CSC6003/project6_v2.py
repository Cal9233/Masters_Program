import csv
import os
import tempfile

def setup_test_environment():
    # Create a temporary directory
    test_dir = tempfile.mkdtemp()
    
    # Create a temporary CSV file
    test_csv_path = os.path.join(test_dir, "music_collection.csv")
    with open(test_csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test_User", "Venom", "Eminem"])
    
    # Set the working directory to the test directory
    original_dir = os.getcwd()
    os.chdir(test_dir)
    
    return original_dir, test_dir

def teardown_test_environment(original_dir, test_dir):
    # Change back to the original directory
    os.chdir(original_dir)
    
    # Remove the temporary directory and its contents
    for root, dirs, files in os.walk(test_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(test_dir)

# User Class that sets username and Users Music_Collection class
class User:
    def __init__(self, username):
        """Initialize a user with a username and an associated music collection."""
        self.user = username
        self.music_collection = Music_Collection(username)

# Music_Collection class with methods for Users playlist
class Music_Collection:
    def __init__(self, username):
        """
        Initialize a music collection for a user.

        Parameters:
        username (str): The username associated with this music collection.
        """
        self.username = username
        self.playlist = {}
        self.load_songs_from_file()

    # Loads playlists
    def load_songs_from_file(self):
        """
        Load songs from a CSV file into the user's playlist.
        
        This method will populate the playlist for a given user based on the CSV file content.
        """
        try:
            if os.path.exists("music_collection.csv"):
                with open("music_collection.csv", "r", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        if len(row) > 0:  # Ensure we have username, title, artist
                            user, title, artist = row
                            if user == self.username:
                                self.playlist[title] = artist
        except FileNotFoundError:
            print("The music collection file does not exist.")
        except csv.Error as e:
            print(f"CSV error while loading songs: {e}")
        except Exception as e:
            print(f"An error occurred while loading songs: {e}")

    # Save playlists
    def save_songs_to_file(self):
        """
        Save songs from the user's playlist to a CSV file.

        This method writes the current user's playlist to a CSV file,
        updating any existing records for that user.
        """
        try:
            # Read all data first
            all_data = []
            if os.path.exists("music_collection.csv"):
                with open("music_collection.csv", "r", newline="") as file:
                    reader = csv.reader(file)
                    all_data = list(reader)

            # Update only the current user's data
            updated_data = []
            for row in all_data:
                user, title, artist = row
                if user == self.username and title not in self.playlist:
                    # Skip songs that are deleted from the current user's playlist
                    continue
                updated_data.append(row)

            # Append the current user's updated playlist
            for title, artist in self.playlist.items():
                updated_data.append([self.username, title, artist])

            # Write the updated data back
            with open("music_collection.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
        except FileNotFoundError:
            print("The music collection file does not exist.")
        except csv.Error as e:
            print(f"CSV error while saving songs: {e}")
        except Exception as e:
            print(f"An error occurred while saving songs: {e}")

    # User adds song with some conditions
    def add_song(self, title, artist):
        """
        Add a song to the user's playlist.

        Parameters:
        title (str): The title of the song.
        artist (str): The artist of the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User1")
        User Test_User1 created and set as the current user.
        >>> organizer.add_song("Numb", "Linkin Park")
        Numb by Linkin Park was added to your playlist.
        """
        try:
            if title in self.playlist:
                print(f"Song {title} is already in your playlist.")
            else:
                self.playlist[title] = artist
                self.save_songs_to_file()
                print(f"{title} by {artist} was added to your playlist.")
        except Exception as e:
            print(f"An error occurred while adding the song: {e}")

    # User deletes song with some conditions
    def delete_song(self, title):
        #This is the failed doc test requirement
        """
        Delete a song from the user's playlist.

        Parameters:
        title (str): The title of the song to be deleted.

        Example:
        >>> organizer.delete_song("Energy")
        Energy was deleted from your playlist.
        """
        try:
            if title not in self.playlist:
                print(f"{title} does not exist in your playlist.")
            else:
                del self.playlist[title]
                self.save_songs_to_file()
                print(f"{title} was deleted from your playlist.")
        except NameError:
            print("Purposely failed the doctest.")
        except Exception as e:
            print(f"An error occurred while deleting the song: {e}")

    # User gets song details with some conditions
    def retrieve_song_details(self, title):
        """
        Retrieve details of a song in the user's playlist.

        Parameters:
        title (str): The title of the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User3")
        User Test_User3 created and set as the current user.
        >>> organizer.add_song("Umbrella", "Rihanna")
        Umbrella by Rihanna was added to your playlist.
        >>> organizer.retrieve_song_details("Umbrella")
        Umbrella is by Rihanna.
        """
        try:
            artist = self.playlist.get(title)
            if artist:
                print(f"{title} is by {artist}.")
            else:
                print(f"{title} does not exist in your playlist.")
        except Exception as e:
            print(f"An error occurred while retrieving song details: {e}")

    # User updates song details with some conditions
    def update_song_details(self, title, new_artist):
        """
        Update the artist of a song in the user's playlist.

        Parameters:
        title (str): The title of the song to be updated.
        new_artist (str): The new artist for the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User4")
        User Test_User4 created and set as the current user.
        >>> organizer.add_song("Mortals", "Warrior")
        Mortals by Warrior was added to your playlist.
        >>> organizer.update_song_details("Mortals", "Warriyo")
        Updated Mortals to be by Warriyo.
        """
        try:
            if title in self.playlist:
                self.playlist[title] = new_artist
                self.save_songs_to_file()
                print(f"Updated {title} to be by {new_artist}.")
            else:
                print(f"{title} does not exist in your playlist.")
        except Exception as e:
            print(f"An error occurred while updating song details: {e}")

    # User displays all songs with some conditions
    def display_all_songs(self):
        """
        Display all songs in the user's playlist.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User5")
        User Test_User5 created and set as the current user.
        >>> organizer.add_song("Can you hear the music", "Ludwig Goransson")
        Can you hear the music by Ludwig Goransson was added to your playlist.
        >>> organizer.display_all_songs()
        These are your current songs in your playlist:
        Can you hear the music by Ludwig Goransson
        """
        try:
            if not self.playlist:
                print("You currently have no songs in your playlist.")
            else:
                print("These are your current songs in your playlist:")
                for title, artist in self.playlist.items():
                    print(f"{title} by {artist}")
        except Exception as e:
            print(f"An error occurred while displaying all songs: {e}")

class Music_Collection_Organizer:
    def __init__(self):
        """Initialize a music collection organizer to manage users and their playlists."""
        self.users = {}
        self.current_user = None
        self.load_users()

    # Load users from playlists
    def load_users(self):
        """Load users from the CSV file."""
        try:
            if os.path.exists("music_collection.csv"):
                with open("music_collection.csv", "r", newline="") as file:
                    reader = csv.reader(file)
                    for row in reader:
                        username = row[0]
                        if username not in self.users:
                            self.users[username] = User(username)
        except FileNotFoundError:
            print("The music collection file does not exist.")
        except csv.Error as e:
            print(f"CSV error while loading users: {e}")
        except Exception as e:
            print(f"An error occurred while loading users: {e}")

    # Add users
    def add_user(self, name):
        """
        Add a new user.

        Parameters:
        name (str): The username of the new user.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("newuser")
        User newuser created and set as the current user.
        """
        try:
            if name in self.users:
                print(f"User {name} already exists.")
            else:
                self.users[name] = User(name)
                self.current_user = self.users[name]
                print(f"User {name} created and set as the current user.")
        except Exception as e:
            print(f"An error occurred while adding a user: {e}")

    # Change users
    def change_user(self, name):
        """
        Change the current user.

        Parameters:
        name (str): The username of the user to switch to.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User11")
        User Test_User11 created and set as the current user.
        >>> organizer.add_user("user2")
        User user2 created and set as the current user.
        >>> organizer.change_user("Test_User11")
        Changed to user 'Test_User11'.
        """
        try:
            if self.current_user and self.current_user.user == name:
                print("You're already logged in as this User.")
            elif name in self.users:
                self.current_user = self.users[name]
                print(f"Changed to user '{name}'.")
            else:
                print(f"User {name} does not exist.")
        except Exception as e:
            print(f"An error occurred while changing users: {e}")

    # User adds song with some conditions
    def add_song(self, title, artist):
        """
        Add a song to the current user's playlist.

        Parameters:
        title (str): The title of the song.
        artist (str): The artist of the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User6")
        User Test_User6 created and set as the current user.
        >>> organizer.add_song("Fireworks", "Katy Perry")
        Fireworks by Katy Perry was added to your playlist.
        """
        try:
            if self.current_user:
                self.current_user.music_collection.add_song(title, artist)
            else:
                print("No user selected. Please change to a user first.")
        except Exception as e:
            print(f"An error occurred while adding a song: {e}")

    # Retrieve song details
    def retrieve_song_details(self, title):
        """
        Retrieve details of a song in the current user's playlist.

        Parameters:
        title (str): The title of the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User7")
        User Test_User7 created and set as the current user.
        >>> organizer.add_song("Memory Reboot", "VOJ")
        Memory Reboot by VOJ was added to your playlist.
        >>> organizer.retrieve_song_details("Memory Reboot")
        Memory Reboot is by VOJ.
        """
        try:
            if self.current_user:
                self.current_user.music_collection.retrieve_song_details(title)
            else:
                print("No user selected. Please change to a user first.")
        except Exception as e:
            print(f"An error occurred while retrieving song details: {e}")

    # Update song details
    def update_song_details(self, title, new_artist):
        """
        Update the artist of a song in the current user's playlist.

        Parameters:
        title (str): The title of the song to be updated.
        new_artist (str): The new artist for the song.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User8")
        User Test_User8 created and set as the current user.
        >>> organizer.add_song("Glory", "Rihanna")
        Glory by Rihanna was added to your playlist.
        >>> organizer.update_song_details("Glory", "Ogryzek")
        Updated Glory to be by Ogryzek.
        """
        try:
            if self.current_user:
                self.current_user.music_collection.update_song_details(title, new_artist)
            else:
                print("No user selected. Please change to a user first.")
        except Exception as e:
            print(f"An error occurred while updating song details: {e}")

    # Delete songs
    def delete_song(self, title):
        """
        Delete a song from the current user's playlist.

        Parameters:
        title (str): The title of the song to be deleted.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User9")
        User Test_User9 created and set as the current user.
        >>> organizer.add_song("Sleepyhead", "Jutes")
        Sleepyhead by Jutes was added to your playlist.
        >>> organizer.delete_song("Sleepyhead")
        Sleepyhead was deleted from your playlist.
        """
        try:
            if self.current_user:
                self.current_user.music_collection.delete_song(title)
            else:
                print("No user selected. Please change to a user first.")
        except Exception as e:
            print(f"An error occurred while deleting the song: {e}")

    # Display all songs
    def display_all_songs(self):
        """
        Display all songs in the current user's playlist.

        Example:
        >>> organizer = Music_Collection_Organizer()
        >>> organizer.add_user("Test_User10")
        User Test_User10 created and set as the current user.
        >>> organizer.add_song("TELESCOPE", "TWXN")
        TELESCOPE by TWXN was added to your playlist.
        >>> organizer.display_all_songs()
        These are your current songs in your playlist:
        TELESCOPE by TWXN
        """
        try:
            if self.current_user:
                self.current_user.music_collection.display_all_songs()
            else:
                print("No user selected. Please change to a user first.")
        except Exception as e:
            print(f"An error occurred while displaying all songs: {e}")

def main():
    """
    Main function to run the music collection program.

    >>> original_dir, test_dir = setup_test_environment()
    >>> organizer = Music_Collection_Organizer()
    >>> organizer.add_user("Calvin")
    User Calvin created and set as the current user.
    >>> organizer.add_song("Numb", "Linkin Park")
    Numb by Linkin Park was added to your playlist.
    >>> organizer.add_song("Fireworks", "Katy Perry")
    Fireworks by Katy Perry was added to your playlist.
    >>> organizer.display_all_songs()
    These are your current songs in your playlist:
    Numb by Linkin Park
    Fireworks by Katy Perry
    >>> teardown_test_environment(original_dir, test_dir)
    """
    organizer = Music_Collection_Organizer()

    while True:
        try:
            #Checks if there is an existing user in csv file, if not create one
            if not organizer.current_user:
                username = input("Enter username: ").strip()
                if len(username) == 0:
                    print("Please input a valid username.")
                else:
                    if username in organizer.users:
                        organizer.change_user(username)
                    else:
                        print(f"User {username} does not exist. Creating a new user.")
                        organizer.add_user(username)
            else:
            #Checks if there is an existing user in csv file, selects the last one that signed out
                playlist = organizer.current_user.music_collection.playlist
                user_list = organizer.users
                print("\nOptions (You can input the numbers for a shorter input): \n 1: add_user, \n 2: change_user, \n 3: add_song, \n 4: retrieve_song_details, \n 5: update_song_details, \n 6: delete_song, \n 7: display_all_songs, \n 8: quit")
                option = input("Choose an option: ").strip().lower()

                if option.isdigit():
                    option = int(option)

                if option == 1 or option == "add_user":
                    username = input("Enter username: ").strip()
                    if len(username) == 0:
                        print("Please input a valid username.")
                    else:
                        organizer.add_user(username)

                elif option == 2 or option == "change_user":
                    if len(user_list.values()) <= 1:
                        print("No other Users to change to.")
                    else:
                        username = input("Enter username: ").strip()
                        if len(username) == 0:
                            print("Please input a valid username.")
                        else:
                            organizer.change_user(username)

                elif option == 3 or option == "add_song":
                    title = input("Enter song title: ").strip()
                    artist = input("Enter artist: ").strip()
                    if len(title) == 0 or len(artist) == 0:
                        print("Please input a valid song or artist.")
                    else:
                        organizer.add_song(title, artist)

                elif option == 4 or option == "retrieve_song_details":
                    if playlist:
                        title = input("Enter song title: ").strip()
                        if len(title) == 0:
                            print("Please input a valid song.")
                        else:
                            organizer.retrieve_song_details(title)
                    else:
                        print("Your playlist is empty. There are no songs details to retrieve from.")

                elif option == 5 or option == "update_song_details":
                    if playlist:
                        title = input("Enter song title: ").strip()
                        new_artist = input("Enter new artist: ").strip()
                        if len(title) == 0 or len(new_artist) == 0:
                            print("Please input a valid song or artist.")
                        else:
                            organizer.update_song_details(title, new_artist)
                    else:
                        print("Your playlist is empty. There are no songs to update.")

                elif option == 6 or option == "delete_song":
                    if playlist:
                        title = input("Enter song title: ").strip()
                        if len(title) == 0:
                            print("Please input a valid song.")
                        else:
                            organizer.delete_song(title)
                    else:
                        print("Your playlist is empty. There are no songs to delete.")

                elif option == 7 or option == "display_all_songs":
                    if playlist:
                        organizer.display_all_songs()
                    else:
                        print("Your playlist is empty. There are no songs to display.")

                elif option == 8 or option == "quit":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
        #handling any errors with exceptions
        except KeyboardInterrupt:
            print(f'\nProgram terminated by user.')
            break
        except AttributeError:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"\nAn error occurred in the main loop: {e}")

if __name__ == "__main__":
    import doctest
    original_dir, test_dir = setup_test_environment()
    doctest.testmod()
    teardown_test_environment(original_dir, test_dir)
    main()