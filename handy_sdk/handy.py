import requests

class HandyAPI:
    def __init__(self, connection_key):
        self.connection_key = connection_key
        self.base_url = "https://www.handyfeeling.com/api/handy/v2"
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
            "X-Connection-Key": self.connection_key
        }

    def set_hamp_mode(self):
        url = f"{self.base_url}/mode"
        data = {"mode": 0}
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def start_hamp(self):
        url = f"{self.base_url}/hamp/start"
        response = requests.put(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def stop_hamp(self):
        url = f"{self.base_url}/hamp/stop"
        response = requests.put(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def set_hamp_velocity(self, velocity):
        url = f"{self.base_url}/hamp/velocity"
        data = {"velocity": velocity}
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()

    def set_hamp_slide(self, min_value, max_value):
        url = f"{self.base_url}/slide"
        data = {"min": min_value, "max": max_value}
        response = requests.put(url, headers=self.headers, json=data)
        response.raise_for_status()
        return response.json()