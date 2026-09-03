class HealthcareAgent:

    def __init__(self, agentId, patientName, status):
        self.agentId = agentId
        self.patientName = patientName
        self.status = status


class HeartMonitoringAgent(HealthcareAgent):

    def monitor_heart_rate(self):
        print(self.patientName, "heart rate is being monitored.")


class MedicineReminderAgent(HealthcareAgent):

    def remind_medicine(self):
        print("Medicine reminder sent to", self.patientName)


class HealthPredictionAgent(HealthcareAgent):

    def predict_health_risk(self):
        print("Health risk is being analyzed for", self.patientName)


heart = HeartMonitoringAgent(1, "Ali", "Active")
medicine = MedicineReminderAgent(2, "Huzaifa", "Active")
prediction = HealthPredictionAgent(3, "Sara", "Active")


heart.monitor_heart_rate()
medicine.remind_medicine()
prediction.predict_health_risk()