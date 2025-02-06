import http.server
import ssl

# Define server settings
HOST = "localhost"
PORT = 8080

# Create an HTTP server
httpd = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)

print(f"Serving HTTP on {HOST}:{PORT}")
httpd.serve_forever()