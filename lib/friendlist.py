from datetime import datetime

class FriendList:
    def __init__(self):
        self.friends = []

    def add_friend(self, name, dob):
        try:
            dob_as_datetime = datetime.strptime(dob, "%Y-%m-%d")
        except:
            print('dob must be in "YYYY-MM-DD format"')
            return None
        self.friends.append({'name': name, 'dob': dob_as_datetime})

    # def update_dob(self, name, dob):
    #     # Parameters:
    #     #   name: string representing friend's name
    #     #   dob: string representing date of birth
    #     # Side-effects:
    #     #   finds and changes dob of friend
    #     # Returns:
    #     #   none
    #     pass # No code here yet

    # def update_name(self, old_name, new_name):
    #     # Parameters:
    #     #   old_name: string representing friend's existing name
    #     #   new_name: string representing friend's new name
    #     # Side-effects:
    #     #   finds and changes name of friend
    #     # Returns:
    #     #   none
    #     pass # No code here yet

    # def upcoming_birthdays(self, days_in_advance):
    #     # Parameters:
    #     #   days_in_advance: int representing number of days to look for birthdays
    #     # Side-effects:
    #     #   none
    #     # Returns:
    #     #   list of friends with birthdays that fall in the next however many days with their upcoming age {name, dob, upcoming_age}
    #     pass # No code here yet