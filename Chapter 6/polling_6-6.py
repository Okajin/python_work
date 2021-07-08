favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

peoples = ['edward', 'seb', 'florient', 'sarah']

for people in peoples:
    if people not in favorite_languages.keys():
        print(f"{people.title()}, please take our poll")
    else:
        print(f"{people.title()}, thank your for taking the poll")
