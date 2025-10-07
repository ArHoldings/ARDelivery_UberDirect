# exceptions.py
class JsonException(Exception):
    def __init__(self, json_data, status_code=400):
        super().__init__(str(json_data))
        self.json_data = json_data
        self.status_code = status_code
