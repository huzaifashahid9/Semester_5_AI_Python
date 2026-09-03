class Environment:
    def __init__(self, door_status="Open"):
        self.door_status = door_status

    def get_percept(self):
        if self.door_status == "Open":
            return "Door Open"
        else:
            return "Door Closed"


class SimpleReflexAgent:
    def act(self, percept):
        if percept == "Door Open":
            return "Raise Security Alarm"
        else:
            return "Everything is Safe"


def run_agent(agent, environment):

    percept = environment.get_percept()

    action = agent.act(percept)

    print("Door Status:", environment.door_status)
    print("Percept:", percept)
    print("Action:", action)


environment = Environment("Open")

agent = SimpleReflexAgent()

run_agent(agent, environment)