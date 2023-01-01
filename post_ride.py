import requests
from datetime import datetime
import webbrowser
import config

USERNAME = config.USERNAME
TOKEN = config.TOKEN
GRAPH = config.CYCLING_GRAPH
pixela_endpoint = "https://pixe.la/v1/users"
now = datetime.now()

params = {
    'token': TOKEN,
    'username': USERNAME,
}

# response = requests.post(url=pixela_endpoint, json=params)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Hours",
#     "type": "float",
#     "color": "sora"
# }

header = {
    "X-USER-TOKEN": TOKEN
}

# post_body {
#     "date": DATE,
#     "quantity": HOURS
# }
DATE = input("Use Today's Date?: ").lower()


def get_date(date: str):
    if date == "y":
        date_string = now.strftime("%Y%m%d")
        return date_string
    elif date == 'n':
        shortdate = input("Enter date in MMdd: ").lower()
        date = f"2022{shortdate}"
        return date


HOURS = input("Enter time in hours ex: 1.5: ")


def get_hours(hours: str):
    return hours


def post_body(date: str, hours: str):
    post_body = {
        "date": date,
        "quantity": hours
    }
    return post_body


def create_post():
    post = requests.post(url=graph_endpoint, json=post_body(the_date, the_hours), headers=header)
    print(post.text)
    webbrowser.open_new_tab(graph_endpoint + ".html")


the_date = get_date(DATE)
the_hours = get_hours(HOURS)
create_post()

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
