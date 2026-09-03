class Environment:

    def __init__(self):
        self.grid = [
            'Empty', 'Empty', 'Trap', 'Empty',
            'Empty', 'Treasure', 'Empty', 'Trap',
            'Trap', 'Empty', 'Empty', 'Empty',
            'Empty', 'Empty', 'Trap', 'Empty'
        ]

    def get_percept(self, position):
        return self.grid[position]

    def collect_treasure(self, position):
        self.grid[position] = 'Empty'

    def display_grid(self, agent_position):

        grid_with_agent = self.grid[:]
        grid_with_agent[agent_position] = 'A'

        print("\nCurrent Grid:")

        for i in range(0, 16, 4):
            print(" | ".join(grid_with_agent[i:i + 4]))


class SimpleReflexAgent:

    def act(self, percept):

        if percept == "Treasure":
            return "Collect Treasure"

        elif percept == "Trap":
            return "Avoid Trap"

        else:
            return "Move Forward"


def run_agent(agent, environment):

    for position in range(16):

        print("\n========================")

        percept = environment.get_percept(position)

        action = agent.act(percept)

        print("Agent Position:", position)
        print("Percept:", percept)
        print("Action:", action)

        if action == "Collect Treasure":
            environment.collect_treasure(position)
            print("Treasure collected!")

        # environment.display_grid(position)



environment = Environment()
agent = SimpleReflexAgent()

run_agent(agent, environment)