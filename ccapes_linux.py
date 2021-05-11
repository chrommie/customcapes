# sudo apt-get -y install python3-pip authbind
# export PATH="$HOME/.local/bin:$PATH"
# pip3 install Flask
# sudo chown YOURUSER /etc/hosts
# sudo touch /etc/authbind/byport/80
# sudo chmod 777 /etc/authbind/byport/80
# ---- reopen the terminal and run with python3 ccapes_linux.py ----

from flask import *
import os
from flask import send_file

with open(r'/etc/hosts', "w") as f:
	f.write("""

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

127.0.0.1 s.optifine.net
		"""
		)

import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/capes/<username>.png")
def cape(username):
	if os.path.isfile(f"capes/{username}.png"):
		return send_file(f"capes/{username}.png", mimetype='image/gif')

	# To remove capes for everyone else, comment out the next two lines
	else:
		return send_file("capes/veteran.png", mimetype='image/gif')
	return('200')

app.run(host="127.0.0.1", port=80)
