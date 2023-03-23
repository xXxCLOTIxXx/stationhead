from .headers import *
from .exceptions import *

import requests
from json import dumps

class Requester:
	def __init__(self):
		self.api = "https://production1.stationhead.com"
		self.sid = None
		self.session = requests.Session()

	def make_request(self, method: str, endpoint: str, body: dict = None):

		response = self.session.request(method, f"{self.api}{endpoint}", data=dumps(body), headers=headers(sid=self.sid))
		return checkException(response.text) if response.status_code != 200 else response


	async def make_async_request(self, method: str, endpoint: str, body: dict = None):
		pass