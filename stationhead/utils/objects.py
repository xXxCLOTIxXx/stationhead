

class profile:
	def __init__(self, data: dict):
		self.json = data
		self.sid = self.json.get("", None)
		self.tipping_salt = self.json.get("tipping_salt", None)
		self.id = self.json.get("id", None)
		self.email = self.json.get("email", None)
		self.contact_email = self.json.get("contact_email", None)
		self.is_premium = self.json.get("is_premium", None)
		self.country = self.json.get("country", None)
		self.type = self.json.get("type", None)
		self.response_timestamp = self.json.get("response_timestamp", None)
		self.suspension = self.json.get("suspension", None)
		self.timezone = self.json.get("timezone", None)
		self.spotify_client_id = self.json.get("spotify_client_id", None)
		self.app_data = self.json.get("app_data", {})