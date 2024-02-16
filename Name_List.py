#This is first trial test

current_users = ['Don Bullion', 'Logical', 'Famous', 'Takyi', 'Adepa']
new_users = ['Tina', 'Don Bullion', 'Nisy', 'RUTH', 'Takyi']

for new_user in new_users:
    if new_user.lower() in (user.lower() for user in current_users):
        print(f"The username {new_user} is already taken. Please enter a new username.")
    else:
        print(f"The username {new_user} is available.")