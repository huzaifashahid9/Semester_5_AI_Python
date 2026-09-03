class AgriculturalThreat:

    def __init__(self, threat_id, name, severity):
        self.threat_id = threat_id
        self.name = name
        self.severity = severity


class CropDiseaseThreat(AgriculturalThreat):

    def detect_disease(self):
        print("Checking crops for disease.")


class PestThreat(AgriculturalThreat):

    def detect_pests(self):
        print("Checking crops for pests.")


class WaterStressThreat(AgriculturalThreat):

    def check_soil_moisture(self):
        print("Checking soil moisture.")


disease = CropDiseaseThreat(1, "Crop Disease", "High")
pest = PestThreat(2, "Pest Attack", "Medium")
water = WaterStressThreat(3, "Water Stress", "Low")

disease.detect_disease()
pest.detect_pests()
water.check_soil_moisture()