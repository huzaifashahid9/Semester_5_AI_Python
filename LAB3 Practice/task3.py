class ModelBasedAgent:

    def __init__(self):

        self.model = {}

    def update_model(self, percept):

        self.model['current'] = percept
        print("Internal Model:", self.model)

    def predict_action(self):

        if self.model['current'] == 'Empty':
            return 'Start water pump'
        else:
            return 'Maintain current level'

    def act(self, percept):

        self.update_model(percept)
        return self.predict_action()


class Environment:

    def __init__(self, state='Empty'):

        self.state = state

    def get_percept(self):

        return self.state

    def fill_tank(self):

        self.state = 'Full'

def run_agent(agent, environment, steps):

    for step in range(steps):

        percept = environment.get_percept()

        action = agent.act(percept)

        print(f"Step {step + 1}: Percept - {percept}, Action - {action}")

        if percept == 'Empty':
            environment.fill_tank()

agent = ModelBasedAgent()

environment = Environment()

run_agent(agent, environment, 5)