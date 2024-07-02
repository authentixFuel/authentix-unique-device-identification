import json
import os

class DeviceStorage:
    def __init__(self, storage_path='device_storage.json'):
        self.storage_path = storage_path
        self.devices = self.load_devices()

    def load_devices(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def save_devices(self):
        with open(self.storage_path, 'w') as file:
            json.dump(self.devices, file)

    def add_device(self, user_id, device_id):
        if user_id in self.devices:
            self.devices[user_id].append(device_id)
        else:
            self.devices[user_id] = [device_id]
        self.save_devices()

    def is_device_registered(self, user_id, device_id):
        return user_id in self.devices and device_id in self.devices[user_id]
