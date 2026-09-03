class Environment:
    def __init__(self, restaurants):
        self.restaurants = restaurants

    def get_perception(self):
        return self.restaurants


class UtilityBaseAgent:

    def __init__(self, hungerFactor):
        self.hungerFactor = hungerFactor

    def utility(self, rating):
        return rating * self.hungerFactor

    def act(self, percept):
        bestRestaurant = "None"
        highestUtility = float("-inf")

        for restaurant, rating in percept.items():
            currentUtility = self.utility(rating)
            print(
                f"{restaurant} : Rating = {rating}," 
                f"Utility = {currentUtility : .2f}"
            )

            if currentUtility > highestUtility:
                highestUtility = currentUtility
                bestRestaurant = restaurant

        return bestRestaurant, highestUtility


def runAgent(agent, environment):

    percept = environment.get_perception()
    selectedRestaurant, utilityVal = agent.act(percept)

    print("\n---Agent Decision---")
    print("Selected Restaurant:", selectedRestaurant)
    print("Highest Utility:", f"{utilityVal : .2f}")


environment = Environment({
    "Restaurant A": 7,
    "Restaurant B": 8,
    "Restaurant C": 10
})

agent = UtilityBaseAgent(hungerFactor=0.8)
runAgent(agent, environment)