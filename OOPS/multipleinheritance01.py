class Phone:
    def feature(self):
        print("📞 Can make calls")
        super().feature()

class Camera:
    def feature(self):
        print("📸 Can take photos")
        super().feature()

class GPS:
    def feature(self):
        print("📍 Can navigate")
        super().feature()

class WiFi:
    def feature(self):
        print("📶 Can connect to internet")
        super().feature()

class End:
    def feature(self):
        print("✅ All features included")

class SmartDevice(Phone,GPS, Camera,  WiFi, End):
    def feature(self):
        print("🤖 SmartDevice combining all features:")
        super().feature()

sd = SmartDevice()
sd.feature()
