# Coding exercises using While loop
"""
You need to create a simple playlist player program in Python that plays songs from a list one by one. 
The program should:
1. Start with the first song in the playlist.
2. After playing a song, ask the user for input: repeat, next, stop
3. If the user types repeat, play the same song again.
4. If the user types next, move on to the next song.
5. If the user types stop, end the program immediately.
6. If the user types anything else, print an error message asking for a valid command.
7. When the playlist reaches the last song and the user chooses next, the program should end with a friendly message.

Use a while loop to control the flow of the playlist.
"""

# List of songs in the playlist
playlist = [
    "Bohemian Rhapsody - Queen",
    "Billie Jean - Michael Jackson",
    "Shape of You - Ed Sheeran",
    "Blinding Lights - The Weeknd",
    "Hotel California - Eagles",
    "Rolling in the Deep - Adele",
    "Sweet Child O' Mine - Guns N' Roses",
    "Levitating - Dua Lipa"
]

current_song_index = 0  # Start with the first song (index 0)

print("Welcome to your Music Player!")
print("Type 'repeat' to play the same song again, 'next' to play the next song, or 'stop' to quit.")

# Use a while loop to control the playlist flow
while current_song_index < len(playlist):
    # Play the current song by printing its name
    print(f"Now playing: {playlist[current_song_index]}") # access the song name by its index
    print()
    
    # Ask the user for their command
    user_input = input("Type 'repeat', 'next', or 'stop': ")
    user_input = user_input.lower() # convert it to lowercase
    
    if user_input == "repeat":
        # Do nothing to current_song_index to play the same song again
        print("Repeating the same song...")
        
    elif user_input == "next":
        # Move to the next song
        current_song_index += 1
        
    elif user_input == "stop":
        # Exit the program immediately
        print("Stopping the playlist. Hope you enjoyed the music!")
        break  # Exit the while loop
        
    else:
        # User typed an invalid command
        print("Oops! Please type 'repeat', 'next', or 'stop'")

# This runs only if the user has gone through all songs
if current_song_index == len(playlist):
    print("You've reached the end of your playlist! Thanks for listening.")
