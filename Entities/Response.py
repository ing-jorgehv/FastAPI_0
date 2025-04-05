class Response:
    def __init__(self, success, status_code, message):
        self.success = success
        self.message = message
        self.status_code = status_code
    
    @property
    def success(self):
        return self._success
    
    @success.setter
    def success(self, value):
        self._success = value
    
    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, value):
        self._message = value
    
    @property
    def status_code(self):
        return self._status_code
    
    @status_code.setter
    def status_code(self, value):
        self._status_code = value
    
    def reset_values(self):
        self._success = False
        self._message = ""
        self.status_code = ""
    
    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "status_code": self.status_code
        }
    