from lib.friendlist import *
from datetime import datetime

def test_initialisation():
    fl = FriendList()
    assert isinstance(fl, FriendList)

"""
Given a name and dob
We can add a friend to our friends list
"""
def test_add_friend():
    fl = FriendList()
    fl.add_friend('Bill', '1990-08-13')
    dob_as_datetime = datetime.strptime('1990-08-13', "%Y-%m-%d")
    assert fl.friends[0] == {'name': 'Bill', 'dob': dob_as_datetime}

# """
# Given a name and incorrect dob
# We raise an exception with the message 'dob must be in "YYYY-MM-DD format"'
# """

# CONTINUE FROM HERE


# """
# Given a new dob
# We can update an existing friend's dob
# """
# friendlist = FriendList()
# friendlist.add_friend('Bill', '1990-08-13')
# friendlist.update_dob('Bill', '1990-09-13')
# friendlist.friends[0] # => {'name': 'Bill', 'dob': '1990-09-13'}

# """
# Given a new name
# We can update an existing friend's name
# """
# friendlist = FriendList()
# friendlist.add_friend('Bill', '1990-08-13')
# friendlist.update_name('Bill', 'Phil')
# friendlist.friends[0] # => {'name': 'Phil', 'dob': '1990-08-13'}

# """
# Given a FriendList
# We can request upcoming birtdays in the following 'x' days
# """
# friendlist = FriendList()
# friendlist.add_friend('Bill', '1990-08-13')
# friendlist.add_friend('Bob', '1990-06-17')
# friendlist.add_friend('Jeff', '1990-11-20')
# friendlist.upcoming_birthdays(30) # => [{'name': 'Bob', 'dob': '1990-06-17', 'upcoming_age': 35}]