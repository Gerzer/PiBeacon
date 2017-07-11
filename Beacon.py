from wsgiref.simple_server import make_server
import os
import urlparse

class RequestMatcher(object):
	def __init__(self, paths, methods):
		self.paths = paths
		self.methods = methods

	def check_request(self, request):
		return (request.path in self.paths) and (request.method in self.methods)

class RequestBridge(object):
	def __init__(self, environment):
		self.path = environment["PATH_INFO"]
		self.method = environment["REQUEST_METHOD"]
		self.query_string = environment["QUERY_STRING"]

def router(environment, start_response):
	global enabled
	response = ""
	request = RequestBridge(environment)
	status_matcher = RequestMatcher(["/status"], ["GET"])
	enable_matcher = RequestMatcher(["/enable"], ["GET", "POST"])
	disable_matcher = RequestMatcher(["/disable"], ["GET", "POST"])
	update_matcher = RequestMatcher(["/update"], ["GET"])
	if status_matcher.check_request(request):
		if enabled:
			response = "Enabled"
		else:
			response = "Disabled"
	elif enable_matcher.check_request(request):
		os.system("sudo hciconfig hci0 leadv")
		enabled = True
		response = "Success"
	elif disable_matcher.check_request(request):
		os.system("sudo hciconfig hci0 noleadv")
		enabled = False
		response = "Success"
	elif update_matcher.check_request(request):
		query_dict = dict(urlparse.parse_qsl(request.query_string))
		major_file = open("Major.txt", "w")
		minor_file = open("Minor.txt", "w")
		major_file.write(query_dict["major"][:2] + " " + query_dict["major"][2:])
		minor_file.write(query_dict["minor"][:2] + " " + query_dict["minor"][2:])
		major_file.close()
		minor_file.close()
		set_packet_data()
		response = "Success"
	start_response("200 OK", [("Content-type", "text/plain")])
	return response

def set_packet_data():
	major_file = open("Major.txt", "r")
	minor_file = open("Minor.txt", "r")
	os.system("sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 61 84 96 F1 C2 0A 4E 8F BA 2A A0 0C CE E4 45 65 " + major_file.read() + " " + minor_file.read() + " C8 00")
	major_file.close()
	minor_file.close()

set_packet_data()
os.system("sudo hciconfig hci0 leadv")
global enabled
enabled = True
make_server("", 80, router).serve_forever()
