def make_albums(artist_name, album_title, number_of_songs=None):
    album = {'name': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


while True:
    print("\nPlease enter the album information:")
    print("(enter 'q' to quit.) ")
    art_name = input("Artist Name: ")
    if art_name == 'q':
        break
    alb_name = input("Album Name: ")
    if alb_name == 'q':
        break

    album_information = make_albums(art_name, alb_name)
    print(f"The {album_information} was added.")
