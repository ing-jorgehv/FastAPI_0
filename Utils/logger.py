from datetime import datetime
from Utils.error_handle import LoggerError



class LocalLogger:
    def __init__(self, log_file, initial_message):
        self.log_file = log_file
        self.create_log_file(log_file, initial_message)

    def create_log_file(self, file_name, initial_message):
        try:
            now = datetime.now()
            timestamp = now.strftime("%Y-%b-%d %H:%M:%S")
            with open(file_name, 'w') as log_file:
                log_file.write(f"{timestamp}: {initial_message}\n")
        except Exception as e:
            raise LoggerError(f'Error in create_log_file: {e}')

    def add_log(self, file_name, message):
        try:
            now = datetime.now()
            timestamp = now.strftime("%Y-%b-%d %H:%M:%S")
            with open(file_name, 'a') as log_file:  
                log_file.write(f"{timestamp}: {message}\n")
        except Exception as e:
            raise LoggerError(f'Error in add_log: {e}')
    
    def info(self, message):
        self.add_log(self.log_file, f"INFO: {message}")

    def error(self, message):
        self.add_log(self.log_file, f"ERROR: {message}")
