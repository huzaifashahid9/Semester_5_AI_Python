import random


class Environment:

    def __init__(self, state='Low Battery'):
        self.state = state

    def getPercept(self):
        return self.state

    def chargeBattery(self):
        self.state = "Fully Charged"
        return 10

    def noActionReward(self):
        return 0


class LearningBaseAgent:

    def __init__(self, actions):
        self.Q = {}
        self.actions = actions

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1

    def getQValue(self, state, action):
        return self.Q.get((state, action), 0.0)

    def selectAction(self, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)
        else:
            return max(
                self.actions, key=lambda action: self.getQValue(state, action)
            )

    def learn(self, state, action, reward, next_state):
        oldQ = self.getQValue(state, action)
        bestQ = max(
            self.getQValue(next_state, action) for action in self.actions
        )

        newQ = oldQ + self.alpha * (reward + self.gamma * bestQ - oldQ)
        self.Q[state, action] = newQ

    def act(self, state):
        return self.selectAction(state)


def runAgent(agent, environment, steps):
    for step in range(steps):
        percept = environment.getPercept()
        action = agent.act(percept)

        if percept == "Low Battery" and action == "Drive to Charger":
            reward = environment.chargeBattery()
        elif percept == "Low Battery" and action == "Continue Driving":
            reward = 0
        elif percept == "Fully Charged" and action == "Continue Driving":
            reward = environment.noActionReward()
        else:
            reward = 0

        nextPercept = environment.getPercept()
        agent.learn(percept, action, reward, nextPercept)

        print(
            f"Step {step+1}: "
            f"State = {percept} | "
            f"Action = {action} | "
            f"Reward = {reward}"
        )


agent = LearningBaseAgent(["Drive to Charger", "Continue Driving"])
environment = Environment()
runAgent(agent, environment, 5)

print("\n--- Learned Q Values ---")
for (state, action), qValue in agent.Q.items():
    print(
        f"State = {state} | "
        f"Action = {action} | "
        f"Q-Value = {qValue : .2f}"
    )