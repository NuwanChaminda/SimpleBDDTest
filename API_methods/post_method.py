import requests
import allure
import logging
import requests
import json


class post_requests:

    def post_request(self, url, body, headers):
        response = requests.request("POST", url, headers=headers, data=json.dumps(body))
        response_status_code = response.status_code
        response_json = response.json()
        return response_status_code, response_json