from datetime import datetime, timedelta, date
import calendar
from collections import defaultdict

def get_birthdays_per_week(users):
    '''returns users' birthdays for 7 days including today'''
    cur_day = datetime.now().replace(minute=0, hour=0, second=0, microsecond=0)
    cur_day_idx = cur_day.weekday() 
    last_day = cur_day + timedelta(days=7)
    res = defaultdict(list)
    #print("Cur weekday", cur_day.weekday(), "last weekday:", last_day.weekday(), last_day)
    for user in users:
        name = user["name"]
        birthday = user["birthday"]
        birthday_cur = birthday.replace(year=cur_day.year)
        if cur_day <= birthday_cur < last_day:
            birthday_weekday_idx = birthday_cur.weekday() if birthday_cur.weekday() < 5 else 0
            res[birthday_weekday_idx].append(name)
    res = sorted(res.items(), key = lambda it: it[0] if it[0] >= cur_day_idx else it[0] + 7)
    for day_idx, user_names in res:
        print(f"{calendar.day_name[day_idx]}:", ", ".join(user_names).strip(", "))


test_users = [{"name": "Bill", "birthday": datetime(1988, 7, 30)},  # Sun: this
      {"name": "Jill",  "birthday": datetime(1995, 7, 31)},         # Mon: next
      {"name": "Kim",   "birthday": datetime(2003, 8, 1)},          # Tue: next 
      {"name": "Jan",   "birthday": datetime(1977, 7, 31)},         # Sun: this 
      {"name": "Julia", "birthday": datetime(1980, 9, 2)},          # other
      {"name": "Peter", "birthday": datetime(1984, 6, 2)},          # other
      {"name": "Robby", "birthday": datetime(1989, 7, 29)},         # Sat: this
      {"name": "Willy", "birthday": datetime(1989, 7, 28)},         # Fri: this
      {"name": "Molly", "birthday": datetime(2007, 8, 2)},          # Wed: next
      {"name": "Tim",   "birthday": datetime(1976, 7, 26)},         # Wed: this
      {"name": "Glory", "birthday": datetime(1966, 8, 3)},          # Thur: next
      {"name": "Tor",   "birthday": datetime(2006, 7, 27)}          # Thur: this
]

get_birthdays_per_week(test_users)


