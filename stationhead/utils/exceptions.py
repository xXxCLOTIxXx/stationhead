from json import loads

class UnknownError(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)

class InvalidEmailOrPassword(Exception):
	def __init__(*args, **kwargs):
		Exception.__init__(*args, **kwargs)



errors = {
	"2050": InvalidEmailOrPassword,
}

def checkException(data):
	try:
		data = loads(data)
		code = data["error"]["code"]
	except:
		raise UnknownError(data)
	if code in errors: raise errors[code](data)
	else:raise UnknownError(data)