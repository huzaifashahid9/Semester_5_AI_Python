class ResponseAgent:
    def execute_response(self):
        print("Executing response...")


class AlertAgent(ResponseAgent):
    def execute_response(self):
        print("Sending alert notification")


class BlockAgent(ResponseAgent):
    def execute_response(self):
        print("Blocking malicious activity")


class RecoverAgent(ResponseAgent):
    def execute_response(self):
        print("Restoring affected system")


agents = [AlertAgent(), BlockAgent(), RecoverAgent()]

for agent in agents:
    agent.execute_response()