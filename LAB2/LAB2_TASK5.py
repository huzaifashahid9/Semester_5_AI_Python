class UAV:
    def __init__(self, uavID, model, batteryLevel):
        self.uavID = uavID
        self.model = model
        self.__batteryLevel = batteryLevel

    def set_batteryLevel(self, level):
        if 0 <= level <= 100:
            self.__batteryLevel = level
        else:
            print("Battery level must be between 0 and 100")

    def get_batteryLevel(self):
        return self.__batteryLevel

    def display_info(self):
        print("\nID:", self.uavID)
        print("Model:", self.model)
        print("Battery:", self.__batteryLevel, "%")


uav1 = UAV("U01", "DJI Mavic", 80)
uav2 = UAV("U02", "Autel EVO", 60)

uav1.set_batteryLevel(90)
uav2.set_batteryLevel(50)

print(uav1.get_batteryLevel())
print(uav2.get_batteryLevel())

uav1.display_info()
uav2.display_info()