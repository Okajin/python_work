def make_albums(artist_name, album_title, number_of_songs=None):
    album = {'name': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


nightwish = make_albums('Nightwish', 'Angels Fall First')
print(nightwish)
epica = make_albums('Epica', 'Cry For The Moon')
print(epica)
within_temptation = make_albums('Within Temptation', 'Resist', number_of_songs=25)
print(within_temptation)
