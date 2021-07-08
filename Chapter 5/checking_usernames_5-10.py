current_users = ['faerie', 'okajin', 'odrelia', 'sedokun', 'seb']
new_users = ['firia', 'okajin', 'odrelia', 'graven', 'watanka']
current_users_low = []

for current_user in current_users:
    current_user = current_user.lower()
    current_users_low.append(current_user)

for new_user in new_users:
    if new_user.lower() in current_users_low:
        print(f"the name: {new_user} is already taken, please choose another name.")
    else:
        print(f"the name: {new_user} is available.")
