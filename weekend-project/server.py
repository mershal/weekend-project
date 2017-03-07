from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer


PORT_NUMBER = 9999

with open('Web.txt', 'r') as input_file:
    web = input_file.read()
    print web

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print self.path
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(web)
        return

try:
    server = HTTPServer(('', PORT_NUMBER), RequestHandler)
    print 'Started httpserver on port', PORT_NUMBER

    server.serve_forever()
except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
