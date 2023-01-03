from datetime import datetime
from setup import PostEvent

now = datetime.now()


def get_date(date: str):
    if date == "y":
        date_string = now.strftime("%Y%m%d")
        return date_string
    elif date == 'n':
        short_date = input("Enter date in MMdd: ").lower()
        date = f"2022{short_date}"
        return date


DATE = input("Use Today's Date?: y/n: ").lower()

TYPE = input("Enter workout type: c for cycling-w for others: ").lower()

the_date = get_date(DATE)
post = PostEvent(workout=TYPE, date=the_date)
post.create_post()


