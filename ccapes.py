from flask import *
import os
from flask import send_file

with open(r'C:\Windows\System32\drivers\etc\hosts', "w") as f:
	f.write("""

		# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost

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
