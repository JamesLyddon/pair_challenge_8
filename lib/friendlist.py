from datetime import datetime, timedelta

class FriendList:
    def __init__(self):
        self.friends = []

    # helper functions
    def validate_name(self, name):
        if any(friend['name'].lower() == name.lower() for friend in self.friends):
            raise ValueError(f"You already have a friend named {name.title()}!")
        return name.title()

    def validate_dob(self, dob):
        try:
            return datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            raise ValueError('dob must be in "YYYY-MM-DD format"')

    def calculate_age_on(self, dob, date):
        return date.year - dob.year

    def next_birthday(self, dob):
        today = datetime.now()
        bday = dob.replace(year=today.year)
        if bday < today:
            bday = bday.replace(year=today.year + 1)
        return bday

    # CRUD functions
    def add_friend(self, name, dob):
        self.friends.append({'name': self.validate_name(name), 'dob': self.validate_dob(dob)})

    def update_dob(self, name, dob):
        self.friends = [{**friend, 'dob': self.validate_dob(dob)} if friend['name'] == name else friend for friend in self.friends]

    def update_name(self, old_name, new_name):
        self.friends = [{**friend, 'name': new_name} if friend['name'] == old_name else friend for friend in self.friends]

    def upcoming_birthdays(self, days_in_advance):
        today = datetime.now()
        end_date = today + timedelta(days_in_advance)
        upcoming = []
        for friend in self.friends:
            bday_this_year = self.next_birthday(friend['dob'])
            if today <= bday_this_year <= end_date:
                upcoming.append({**friend, "upcoming_age": self.calculate_age_on(friend['dob'], bday_this_year)})
        return upcoming
