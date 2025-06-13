
## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class FriendList:
    # User-facing properties:
    #   friends: list of dictionaries

    def __init__(self, name):
        # Parameters:
        #   friends: list
        # Side effects:
        #   none
        pass # No code here yet

    def add_friend(self, name, dob):
        # Parameters:
        #   name: string representing friend's name
        #   dob: string representing date of birth
        # Side-effects
        #   Adds freind to friends list
        # Returns:
        #   None
        pass # No code here yet

    def update_dob(self, name, dob):
        # Parameters:
        #   name: string representing friend's name
        #   dob: string representing date of birth
        # Side-effects:
        #   finds and changes dob of friend
        # Returns:
        #   none
        pass # No code here yet

    def update_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string representing friend's existing name
        #   new_name: string representing friend's new name
        # Side-effects:
        #   finds and changes name of friend
        # Returns:
        #   none
        pass # No code here yet

    def upcoming_birthdays(self, days_in_advance):
        # Parameters:
        #   days_in_advance: int representing number of days to look for birthdays
        # Side-effects:
        #   none
        # Returns:
        #   list of friends with birthdays that fall in the next however many days with their upcoming age {name, dob, upcoming_age}
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name and dob
We can add a friend to our friends list
"""
friendlist = FriendList()
friendlist.add_friend('Bill', '1990-08-13')
friendlist.friends[0] # => {'name': 'Bill', 'dob': '1990-08-13'}

"""
Given a new dob
We can update an existing friend's dob
"""
friendlist = FriendList()
friendlist.add_friend('Bill', '1990-08-13')
friendlist.update_dob('Bill', '1990-09-13')
friendlist.friends[0] # => {'name': 'Bill', 'dob': '1990-09-13'}

"""
Given a new name
We can update an existing friend's name
"""
friendlist = FriendList()
friendlist.add_friend('Bill', '1990-08-13')
friendlist.update_name('Bill', 'Phil')
friendlist.friends[0] # => {'name': 'Phil', 'dob': '1990-08-13'}

"""
Given a FriendList
We can request upcoming birtdays in the following 'x' days
"""
friendlist = FriendList()
friendlist.add_friend('Bill', '1990-08-13')
friendlist.add_friend('Bob', '1990-06-17')
friendlist.add_friend('Jeff', '1990-11-20')
friendlist.upcoming_birthdays(30) # => [{'name': 'Bob', 'dob': '1990-06-17', 'upcoming_age': 35}]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
