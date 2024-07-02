import hashlib
import uuid

class DeviceFingerprint:
    def __init__(self):
        self.device_id = self.generate_device_id()

    def generate_device_id(self):
        node = uuid.getnode()
        mac = uuid.UUID(int=node).hex[-12:]
        device_id = hashlib.sha256(mac.encode()).hexdigest()
        return device_id

    def get_device_id(self):
        return self.device_id
