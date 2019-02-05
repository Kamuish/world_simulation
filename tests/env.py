
import sys
import os

def set_env():
	# append module root directory to sys.path
	sys.path.append(
	    os.path.dirname(
	        os.path.dirname(
	            os.path.abspath(__file__)
	        )
	    )
	)