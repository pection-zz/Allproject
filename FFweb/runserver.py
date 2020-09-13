import SocketServer
import SimpleHTTPServer

import requests
import multiprocessing

# Variables
PORT = 8000
URL = 'localhost:{port}'.format(port=PORT)

# Setup simple sever
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print ("Serving at port", PORT)

# start the server as a separate process
server_process = multiprocessing.Process(target=httpd.serve_forever)
server_process.daemon = True
server_process.start()

# Getting HTML from the target page
values = {
    'name': 'Thomas Anderson',
    'location': 'unknown'
}

r = requests.post(URL, data=values)
r.text

# stop the server
server_process.terminate()