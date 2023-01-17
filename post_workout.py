from datetime import datetime
from setup import PostEvent

now = datetime.now()


def get_date():
    input_q = input("Use Today's Date?: y/n: ").lower()
    if input_q == "y":
        date_string = now.strftime("%Y%m%d")
        return date_string
    elif input_q == 'n':
        short_date = input("Enter date in MMdd: ").lower()
        date = f"2023{short_date}"
        return date


TYPE = input("Enter workout type: c for cycling-w for others: ").lower()

post = PostEvent(workout=TYPE, date=get_date())
post.create_post()
