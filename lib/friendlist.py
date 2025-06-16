from datetime import datetime, timedelta


class FriendList:
    def __init__(self):
        self.friends = []

    def add_friend(self, name, dob):
        try:
            dob_as_datetime = datetime.strptime(dob, "%Y-%m-%d")
        except Exception:
            raise Exception('dob must be in "YYYY-MM-DD format"')
        self.friends.append({'name': name, 'dob': dob_as_datetime})

    def update_dob(self, name, dob):
        updated_friends = []
        for friend in self.friends:
            if friend["name"] == name:
                updated_friends.append({**friend, "dob": dob})
            else:
                updated_friends.append(friend)
        self.friends = updated_friends

    def update_name(self, old_name, new_name):
        updated_friends = []
        for friend in self.friends:
            if friend["name"] == old_name:
                updated_friends.append({**friend, "name": new_name})
            else:
                updated_friends.append(friend)
        self.friends = updated_friends

    def upcoming_birthdays(self, days_in_advance):
        upcoming_friends_birthdays = []
        today = datetime.now()
        for friend in self.friends:
            upcoming_birthday = friend["dob"].replace(year=datetime.now().year)
            if upcoming_birthday - today <= timedelta(days_in_advance):
                upcoming_age = (today.year - friend["dob"].year)
                upcoming_friends_birthdays.append({**friend, "upcoming_age": upcoming_age})
        return upcoming_friends_birthdays
