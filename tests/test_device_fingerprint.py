import unittest
from device_identification.device_fingerprint import DeviceFingerprint

class TestDeviceFingerprint(unittest.TestCase):
    def test_generate_device_id(self):
        fingerprint = DeviceFingerprint()
        device_id = fingerprint.get_device_id()
        self.assertIsNotNone(device_id)
        self.assertEqual(len(device_id), 64)

if __name__ == '__main__':
    unittest.main()
