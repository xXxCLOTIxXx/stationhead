import stationhead
import asyncio

email = "email@gmail.com" #account email
password = "password" #account password

client = stationhead.AsyncClient()

async def main():
	info = await client.login(email=email, password=password)
	print(info.json)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())