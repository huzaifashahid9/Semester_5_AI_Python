class GoalBasedAgent:

    def __init__(self):
        self.goal = 'No action needed'

    def formulate_goal(self, percept):

        if percept == 'Low':
            self.goal = 'Charge'
        else:
            self.goal = 'No action needed'

    def act(self, percept):

        self.formulate_goal(percept)

        if self.goal == 'Charge':
            return 'Start charging'
        else:
            return 'Battery is full'


class Environment:

    def __init__(self, state='Low'):

        self.state = state

    def get_percept(self):

        return self.state

    def charge_battery(self):

        self.state = 'Full'


def run_agent(agent, environment, steps):

    for step in range(steps):

        percept = environment.get_percept()

        action = agent.act(percept)

        print(f"Step {step + 1}")
        print("Percept    :", percept)
        print("Goal       :", agent.goal)
        print("Action     :", action)

        if action == 'Start charging':
            environment.charge_battery()

        print("Battery State :", environment.state)
        print("-" * 50)

agent = GoalBasedAgent()

environment = Environment()

run_agent(agent, environment, 5)