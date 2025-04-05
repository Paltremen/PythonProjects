'''
def city_country(city, country):
    pair = (f"{city.title()}, {country.title()}")
    return pair
one = city_country("moscow", "russia")
print(one)

two = city_country("london", "great britain")
print(two)

three = city_country("washington", "united states of america")
print(three)
'''

def make_album(artist, title, songs = None):
    album = {"artist": artist.title(), "title": title.title()}
    if songs:
        album["songs"] = songs
    return album

while True:
    print(f"Insert the name and title (also number of songs). Type 'q' to quit.")
    input_artist = input("Artist name: ")
    if input_artist == "q":
        break
    input_title = input("Album title: ")
    if input_title == "q":
        break
    input_song = input("Number of songs (type nothing if you don't want to): ")
    if input_song == "q":
        break
    elif input_song == None:
        user_album = make_album(input_artist, input_title)
    else:
        try:
            num_songs = int(input_song)
            user_album = make_album(input_artist, input_title, input_song)
        except ValueError:
            print(f"Please enter a number.")
            continue
    print(user_album)