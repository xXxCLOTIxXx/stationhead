from .utils.requester import Requester
from .utils import objects, exceptions


from json import loads

class Client:
	def __init__(self):
		self.req = Requester()


	def login(self, email: str, password: str):

		data = {
			"clear_broadcast_data": True,
			"resalt": True,
			"password": password,
			"username": email
		}
		resp = objects.profile(loads(self.req.make_request(method="POST", endpoint="/login", body=data).text))
		self.req.sid = resp.sid
		return resp


	def register(self, email: str, password: str, nickname: str):

		data = {
			"email": email,
			"password": password,
			"handle": nickname
		}

		resp = objects.profile(loads(self.req.make_request(method="POST", endpoint="/user", body=data).text))
		return resp