
def headers(sid: str = None):
	headers = {
		"app-platform": "android",
		"app-version": "1.2.48",
		"content-type": "application/json"
	}
	if sid:headers["authorization"] = sid

	return headers