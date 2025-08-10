class ConfigManage:
    _instance = None
    _initialization = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print(f"Created new instance")
            cls._instance = super(ConfigManage, cls).__new__(cls)
        return cls._instance

    def __init__(self, settings:dict):

        if not self._initialization:
            self.settings = settings
            self._initialization = True
            print(f"ConfigManager init")

    def get_settings(self, key:str):
        return self.settings.get(key)

    def update_settings(self, key:str, value):
        self.settings[key] = value
        print(f"Updated. {key} has {value}")

config1 = ConfigManage({"font": "Arial", "font-size": 14})
print(config1.get_settings("font"))

config2 = ConfigManage({"db_host": "localhost"})
print(config1.get_settings("font"))
print(config2.get_settings("db_host"))

config2.update_settings("color", "red")
print(config1.get_settings("color"))