# Prefer Chrome, as it shows the certificate status clearly 

# Talk about the .crt file and the .key file, how they were generated

# Explain how adding the self-signed certificate is a requirement
# and how a trusted certificate would not need to be added to the keychain

# To access keychain on Macbook: lens -> Keychain access

# Show off nginx config file
code ./nginx.conf

# To restart nginx:
brew services restart nginx

# Navigate in Chrome to localhost:8080 and show that the information here is not encrypted

# Then, navigate to https://localhost and show that the information is encrypted

# stop nginx with 
brew services stop nginx

sudo python3 server.py
# Navigate to https://localhost
# Point out how it is a self signed certificate

# Either change server.py or run directly server_http.py and show how 
# Chrome is giving a warning that there is no certificate present
