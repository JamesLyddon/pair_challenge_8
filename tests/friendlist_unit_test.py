from lib.friendlist import FriendList
from datetime import datetime
import pytest


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

"""
Given a name and incorrect dob
We raise an exception with the message 'dob must be in "YYYY-MM-DD format"'
"""
def test_add_friend_incorrect_dob_raises_exception():
    with pytest.raises(Exception) as e:
        fl = FriendList()
        fl.add_friend('Bill', '13-08-13')
        datetime.strptime('13-08-13', "%Y-%m-%d")
    assert str(e.value) == 'dob must be in "YYYY-MM-DD format"'

"""
Given a FriendList
We raise a ValueError when adding a name that already exists
"""
def test_adding_existing_name():
    friendlist = FriendList()
    friendlist.add_friend('Bill', '1990-08-13')
    with pytest.raises(Exception) as e:
        friendlist.add_friend('bill', '1990-10-09')
    err_msg = str(e.value)
    assert err_msg == "You already have a friend named Bill!"

"""
Given a new dob
We can update an existing friend's dob
"""
def test_update_dob():
    friendlist = FriendList()
    friendlist.add_friend('Bill', '1990-08-13')
    friendlist.update_dob('Bill', '1990-09-13')
    dob = datetime.strptime('1990-09-13', "%Y-%m-%d")
    assert friendlist.friends[0] == {'name': 'Bill', 'dob': dob}

"""
Given a bad dob
We can't update an existing friend's dob but get an exception
"""
def test_update_bad_dob():
    friendlist = FriendList()
    friendlist.add_friend('Bill', '1990-08-13')
    with pytest.raises(Exception) as e:
        friendlist.update_dob('Bill', '1990,09,13')
    err_msg = str(e.value)
    assert err_msg == 'dob must be in "YYYY-MM-DD format"'

"""
Given a new name
We can update an existing friend's name
"""
def test_update_name():
    friendlist = FriendList()
    friendlist.add_friend('Bill', '1990-08-13')
    friendlist.update_name('Bill', "Phil")
    assert friendlist.friends[0] == {'name': 'Phil', 'dob': friendlist.friends[0]["dob"]}

"""
Given a FriendList
We can request upcoming birtdays in the following 'x' days
"""
def test_upcoming_birthdays():
    friendlist = FriendList()
    friendlist.add_friend('Bill', '1990-08-13')
    friendlist.add_friend('Bob', '1990-06-17')
    friendlist.add_friend('Jeff', '1990-11-20')
    dob_as_datetime = datetime.strptime('1990-06-17', "%Y-%m-%d")
    result = friendlist.upcoming_birthdays(30) 
    assert result == [{'name': 'Bob', 'dob': dob_as_datetime, 'upcoming_age': 35}]
