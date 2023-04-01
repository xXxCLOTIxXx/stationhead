from .utils.requester import Requester
from .utils import objects, exceptions
from asyncio import get_event_loop, new_event_loop

from json import loads

class AsyncClient:
	def __init__(self):
		self.req = Requester()


	def __del__(self):
		try:
			loop = get_event_loop()
			loop.run_until_complete(self.close_session())
		except RuntimeError:
			loop = new_event_loop()
			loop.run_until_complete(self.close_session())

	async def close_session(self):
		if not self.req.asyncSession.closed: await self.req.asyncSession.close()


	async def login(self, email: str, password: str):

		data = {
			"clear_broadcast_data": True,
			"resalt": True,
			"password": password,
			"username": email
		}
		resp = await self.req.make_async_request(method="POST", endpoint="/login", body=data)
		resp = objects.profile(loads(await resp.text()))
		self.req.sid = resp.sid
		return resp


	async def register(self, email: str, password: str, nickname: str):

		data = {
			"email": email,
			"password": password,
			"handle": nickname
		}
		resp = await self.req.make_async_request(method="POST", endpoint="/user", body=data)
		return objects.profile(loads(await resp.text()))