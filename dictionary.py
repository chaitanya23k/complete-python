# 1 Create a user profile for your new game.
# This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# 2 iterate and print all the keys in the above user.

# 3 Add a new weapon to your user

# 4 Add a new key to include 'is_banned'. Set it to false

# 5 Ban the user by setting the previous key to True

# 6 create a new user2 my copying the previous user and update the age value and username value.

user_profile = {
    'age': 55,
    'username' : 'gamer',
    'weapons' : 'none',
    'is_active' : True,
    'clan' : 'india'
    }
# 2 iterate and print all the keys in the above user.
print(user_profile.keys())

# 3 Add a new weapon to your user

user_profile['weapons'] = 'sword'

# 4 Add a new key to include 'is_banned'. Set it to false
user_profile.update({'is_banned': False})

# 5 Ban the user by setting the previous key to True
user_profile['is_banned'] = True

# 6 create a new user2 my copying the previous user and update the age value and username value.
user2 = user_profile.copy()
user2.update({'age': 50, 'username': 'User2'})
print(user2)
print(user_profile)