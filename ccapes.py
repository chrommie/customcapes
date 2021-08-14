from flask import *
import os
from flask import send_file

with open(r'C:\Windows\System32\drivers\etc\hosts', "a") as f:
	f.write("""127.0.0.1 s.optifine.net""")


import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True

@app.route("/capes/<username>.png")
def cape(username):
	if os.path.isfile(f"capes/{username}.png"):
		return send_file(f"capes/{username}.png", mimetype='image/gif')

	# To remove capes for everyone else, comment out the next two lines
	#else:
	#	return send_file("capes/veteran.png", mimetype='image/gif')
	return('200')

app.run(host="127.0.0.1", port=80)
