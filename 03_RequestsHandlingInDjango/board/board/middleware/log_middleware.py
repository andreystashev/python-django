import os
import datetime


class LogWriter:
    def __init__(self, get_response):
        self.get_response = get_response
        self.log_file = 'log.txt'

    def __call__(self, request):
        log_path = os.path.join(os.getcwd(), self.log_file)
        response = self.get_response(request)
        with open(log_path, mode='a', encoding='utf8') as file:
            split_request = str(request).split(' ')
            file.write(f'{datetime.datetime.now()};  {split_request[1]}  {split_request[2][:-1]}\n')
        return response
