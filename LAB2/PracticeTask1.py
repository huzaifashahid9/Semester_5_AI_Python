class Light:
    def __init__(self, roomName):
        self.roomName = roomName
        self.status = "Off"

Light1 = Light("Living Room")
Light1.status = "On"
Light2 = Light("Dining Room")
Light2.status = "Off"
Light3 = Light("Kitchen Room")
Light3.status = "On"

lights = [Light1, Light2, Light3]
for light in lights:
    print(f"{light.roomName} light turned {light.status}")


