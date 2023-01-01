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
graphs_url = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "workouts2023"
graph_config = {
    "id": f"{graph_id}",
    "name": "Workout Graph",
    "unit": "Completed",
    "type": "int",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# post_body {
#     "date": DATE,
#     "quantity": HOURS
# }
DATE = input("Use Today's Date?: y/n").lower()


def create_graph():
    post = requests.post(url=graphs_url, json=graph_config, headers=header)
    print(post.text)
    webbrowser.open_new_tab(graphs_url + f"/{graph_id}.html")


def get_date(date: str):
    if date == "y":
        date_string = now.strftime("%Y%m%d")
        return date_string
    elif date == 'n':
        short_date = input("Enter date in MMdd: ").lower()
        date = f"2022{short_date}"
        return date


WORKOUT = input("Enter '1' if completed a workout today. '0' if did not: ")


def complete_workout(workout_bool: str):
    return workout_bool


def post_body(date: str, did_workout: str):
    post_body = {
        "date": date,
        "quantity": did_workout
    }
    return post_body


def create_post():
    post = requests.post(url=graph_endpoint, json=post_body(the_date, did_workout), headers=header)
    print(post.text)
    webbrowser.open_new_tab(graph_endpoint + ".html")


the_date = get_date(DATE)
did_workout = complete_workout(WORKOUT)
# create_graph()
create_post()
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)
