from .exceptions import *

from requests import Session
from aiohttp import ClientSession
from json import dumps

class Requester:
	def __init__(self):
		self.api = "https://production1.stationhead.com"
		self.sid = None
		self.session = Session()
		self.asyncSession = ClientSession()

	def headers(self):
		headers = {
			"app-platform": "android",
			"app-version": "1.2.48",
			"content-type": "application/json"
		}
		if self.sid:headers["authorization"] = self.sid

		return headers


	def make_request(self, method: str, endpoint: str, body: dict = None):

		response = self.session.request(method, f"{self.api}{endpoint}", data=dumps(body), headers=self.headers())
		return checkException(response.text) if response.status_code != 200 else response


	async def make_async_request(self, method: str, endpoint: str, body: dict = None):
		response = await self.asyncSession.request(method, f"{self.api}{endpoint}", data=dumps(body), headers=self.headers())
		return checkException(await response.text()) if response.status != 200 else response