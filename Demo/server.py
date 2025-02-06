import http.server
import ssl

# Define server settings
HOST = "localhost"
PORT = 443 #TODO change me to 8080 for http!

# Create an HTTP server
httpd = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)

# Set up the SSL context
#TODO comment out for http!
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="localhost.crt", keyfile="localhost.key")

# Wrap the server's socket with the SSL context
# TODO comment out for http!
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTP/S on {HOST}:{PORT}")
httpd.serve_forever()