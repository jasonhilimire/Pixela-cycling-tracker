import config
import requests
import webbrowser


class PostEvent:
    header = {
        "X-USER-TOKEN": config.TOKEN
    }

    """
    ASK USER FOR WORKOUT TYPE
    ASK USER for date - update date as needed
    ASK USER for workout input - update workout input
    CREATE INSTANCE OF CLASS from response
    BASED ON TYPE - setup corresponding graph
    CREATE POST BODY
    POST
    OPEN WEBSITE
    """


    def __init__(self, workout, date):
        self.workout = workout
        self.date = date

    def workout_type(self):
        if self.workout == 'c':
            graph = config.CYCLING_GRAPH
            return graph
        elif self.workout == 'w':
            graph = config.WORKOUTS_GRAPH
            return graph
        else:
            print("Incorrect workout type entered")

    def workout_input(self):
        if self.workout == 'c':
            w_input = input("Enter time in hours ex: 1.5: ")
            return w_input
        elif self.workout == 'w':
            w_input = input("Enter the number of workouts for today. '0' for none: ")
            return w_input

    def post_body(self):
        post_body = {
            "date": self.date,
            "quantity": self.workout_input()
        }
        return post_body

    def build_url(self):
        return f"{config.ENDPOINT}/{config.USERNAME}/graphs/{self.workout_type()}"

    def create_post(self):
        url = self.build_url()
        body = self.post_body()
        post = requests.post(url=url, json=body, headers=self.header)
        print(post.text)
        webbrowser.open_new_tab(url + ".html")
