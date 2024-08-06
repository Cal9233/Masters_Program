import os
import csv

class User:
    def __init__(self, username):
        self.user = username
        self.music_collection = Music_Collection()

class Music_Collection:
    def __init__(self):
        self.playlist = {}

    def add_song(self, title, artist):
        """
        Adds a song to the playlist.

        Args:
            title (str): The title of the song
            artist (str): The artist of the song

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mc.add_song("Judas", "Lady Gaga")
        'Song Judas is already in your playlist.'
        >>> mc.add_song("", "")
        'Invalid input. Title and artist cannot be empty.'
        """
        if not title or not artist:
            return "Invalid input. Title and artist cannot be empty."
        if title in self.playlist:
            return f"Song {title} is already in your playlist."
        self.playlist[title] = artist
        return f"{title} by {artist} was added to your playlist."

    def delete_song(self, title):
        """
        Deletes a song from the playlist.

        Args:
            title (str): The title of the song

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mc.delete_song("Judas")
        'Judas was deleted from your playlist.'
        >>> mc.delete_song("Judas")
        'Judas does not exist in your playlist.'
        >>> mc.delete_song("")
        'Invalid input. Title cannot be empty.'
        """
        if not title:
            return "Invalid input. Title cannot be empty."
        if title not in self.playlist:
            return f"{title} does not exist in your playlist."
        del self.playlist[title]
        return f"{title} was deleted from your playlist."

    def get_song_details(self, title):
        """
        Gets song details from playlist.

        Args:
            title (str): The title of the song

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mc.get_song_details("Judas")
        'Judas is by Lady Gaga.'
        >>> mc.get_song_details("Bad Romance")
        'Bad Romance does not exist in your playlist.'
        """
        artist = self.playlist.get(title)
        if artist:
            return f"{title} is by {artist}."
        else:
            return f"{title} does not exist in your playlist."

    def update_song_details(self, title, new_artist):
        """
        Updates song details in playlist.

        Args:
            title (str): The title of the song
            new_artist (str): The updated artist of the song

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mc.update_song_details("Judas", "Linkin Park")
        'Updated Judas to be by Linkin Park.'
        >>> mc.update_song_details("Bad Romance", "Lady Gaga")
        'Bad Romance does not exist in your playlist.'
        """
        if title in self.playlist:
            self.playlist[title] = new_artist
            return f"Updated {title} to be by {new_artist}."
        else:
            return f"{title} does not exist in your playlist."

    def display_all_songs(self):
        """
        Display all songs from playlist.

        >>> mc = Music_Collection()
        >>> mc.add_song("Judas", "Lady Gaga")
        'Judas by Lady Gaga was added to your playlist.'
        >>> mc.add_song("In the End", "Linkin Park")
        'In the End by Linkin Park was added to your playlist.'
        >>> mc.display_all_songs()
        'These are your current songs in your playlist:\\nJudas by Lady Gaga\\nIn the End by Linkin Park'
        >>> mc = Music_Collection()
        >>> mc.display_all_songs()
        'You currently have no songs in your playlist.'
        """
        if not self.playlist:
            return "You currently have no songs in your playlist."
        else:
            songs = [f"{title} by {artist}" for title, artist in self.playlist.items()]
            return "These are your current songs in your playlist:\n" + "\n".join(songs)

class Music_Collection_Organizer:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.users_file = "users.csv"
        self.playlists_file = "playlists.csv"
        self.load_users_and_playlists()

    def load_users_and_playlists(self):
        """
        Loads users and their playlists from CSV files.
        """
        self.load_users()
        self.load_playlists()

    def load_users(self):
        """
        Loads users from the users CSV file.
        """
        try:
            with open(self.users_file, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username = row[0]
                    self.users[username] = User(username)
        except FileNotFoundError:
            print(f"Users file not found. Starting with an empty user list.")

    def load_playlists(self):
        """
        Loads playlists for all users from the playlists CSV file.
        """
        try:
            with open(self.playlists_file, 'r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    username, title, artist = row
                    if username in self.users:
                        self.users[username].music_collection.playlist[title] = artist
        except FileNotFoundError:
            print(f"Playlists file not found. Starting with empty playlists.")

    def save_users_and_playlists(self):
        """
        Saves all users and their playlists to CSV files.
        """
        self.save_users()
        self.save_playlists()

    def save_users(self):
        """
        Saves all users to the users CSV file.
        """
        with open(self.users_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for username in self.users:
                writer.writerow([username])

    def save_playlists(self):
        """
        Saves playlists for all users to the playlists CSV file.
        """
        with open(self.playlists_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for username, user in self.users.items():
                for title, artist in user.music_collection.playlist.items():
                    writer.writerow([username, title, artist])

    def add_user(self, name):
        """
        Create new User and add to Users list.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_user("Cal")
        'User Cal already exists.'
        """
        if name in self.users:
            return f"User {name} already exists."
        else:
            self.users[name] = User(name)
            self.current_user = self.users[name]
            self.save_users_and_playlists()
            return f"User {name} created and set as the current user."

    def change_user(self, name):
        """
        Change User from Users list.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_user("Al")
        'User Al created and set as the current user.'
        >>> mco.change_user("Cal")
        'Changed to user Cal.'
        >>> mco.change_user("Zach")
        'User Zach does not exist.'
        >>> mco.change_user("Al")
        "You're already logged in as this User."
        """
        if self.current_user and self.current_user.user == name:
            return "You're already logged in as this User."
        elif name in self.users:
            self.current_user = self.users[name]
            return f"Changed to user '{name}'."
        else:
            return f"User {name} does not exist."

    def add_song(self, title, artist):
        """
        Adds a song to the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_song("Imagine", "John Lennon")
        'Imagine by John Lennon was added to your playlist.'
        >>> mco.add_user("Bob")
        'User Bob created and set as the current user.'
        >>> mco.add_song("Hey Jude", "The Beatles")
        'Hey Jude by The Beatles was added to your playlist.'
        """
        if self.current_user:
            result = self.current_user.music_collection.add_song(title, artist)
            self.save_playlists()
            return result
        else:
            return "No user selected. Please change to a user first."

    def retrieve_song_details(self, title):
        """
        Retrieves song details from the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_song("Imagine", "John Lennon")
        'Imagine by John Lennon was added to your playlist.'
        >>> mco.retrieve_song_details("Imagine")
        'Imagine is by John Lennon.'
        >>> mco.retrieve_song_details("Hey Jude")
        'Hey Jude does not exist in your playlist.'
        """
        if self.current_user:
            return self.current_user.music_collection.get_song_details(title)
        else:
            return "No user selected. Please change to a user first."

    def update_song_details(self, title, new_artist):
        """
        Updates song details in the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_song("Imagine", "John Lennon")
        'Imagine by John Lennon was added to your playlist.'
        >>> mco.update_song_details("Imagine", "The Beatles")
        'Updated Imagine to be by The Beatles.'
        >>> mco.update_song_details("Hey Jude", "The Beatles")
        'Hey Jude does not exist in your playlist.'
        """
        if self.current_user:
            result = self.current_user.music_collection.update_song_details(title, new_artist)
            self.save_playlists()
            return result
        else:
            return "No user selected. Please change to a user first."

    def delete_song(self, title):
        """
        Deletes a song from the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_song("Imagine", "John Lennon")
        'Imagine by John Lennon was added to your playlist.'
        >>> mco.delete_song("Imagine")
        'Imagine was deleted from your playlist.'
        >>> mco.delete_song("Imagine")
        'Imagine does not exist in your playlist.'
        """
        if self.current_user:
            result = self.current_user.music_collection.delete_song(title)
            self.save_playlists()
            return result
        else:
            return "No user selected. Please change to a user first."

    def display_all_songs(self):
        """
        Displays all songs in the current user's playlist.

        >>> mco = Music_Collection_Organizer()
        >>> mco.add_user("Cal")
        'User Cal created and set as the current user.'
        >>> mco.add_song("Imagine", "John Lennon")
        'Imagine by John Lennon was added to your playlist.'
        >>> mco.add_song("Hey Jude", "The Beatles")
        'Hey Jude by The Beatles was added to your playlist.'
        >>> mco.display_all_songs()
        'These are your current songs in your playlist:\\nImagine by John Lennon\\nHey Jude by The Beatles'
        """
        if self.current_user:
            return self.current_user.music_collection.display_all_songs()
        else:
            return "No user selected. Please change to a user first."

def main():
    #Initiates Music_Collection_Organizer class
    organizer = Music_Collection_Organizer()
    while True:
        #Starts program by first creating a user
            if not organizer.current_user:
                print('Please create a user to use the Music Collection')
                username = input("Enter username: ").strip()
                if len(username) == 0:
                    print("Please input a valid username.")
                else: 
                    result = organizer.add_user(username)
                    print(result)
            else:            
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