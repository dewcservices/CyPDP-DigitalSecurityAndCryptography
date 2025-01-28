import http.server
import ssl

# Define server settings
HOST = "localhost"
PORT = 443

# Create an HTTP server
httpd = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)

# Set up the SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="localhost.crt", keyfile="localhost.key")

# Wrap the server's socket with the SSL context
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on {HOST}:{PORT}")
httpd.serve_forever()