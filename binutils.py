import binascii

def frmthex(s, bytes_per_line=16):
	"""
	Returns a human readable dump of the hex, like hexdump -C
	"""

	output = ""
	ascii_line = ""

	line_cnt = 0
	line_bytes = 0
	total_bytes = 0

	output += "00000000  "
	for byte in s:
		line_bytes += 1
		total_bytes += 1

		output += binascii.hexlify(byte) + " "
		if line_bytes == bytes_per_line / 2:
			output += " " 

		new_char = byte
		if ord(new_char) < 32 or ord(new_char) > 126:
			new_char = '.'
		if new_char in ['\t', ' ']:
			new_char = '.'
		ascii_line += new_char

		if line_bytes == bytes_per_line or total_bytes == len(s):
			pad = ""

			if total_bytes == len(s):

				pad = "" # for the extra space put in the middle
				if line_bytes < (bytes_per_line/2):
					pad += " "

				pad += "   " * (bytes_per_line - line_bytes)

			output += "{}    |{:<{}}|\n".format(pad, ascii_line, bytes_per_line)

			if total_bytes != len(s):
				output += "%08x  " % ((line_cnt+1)*bytes_per_line)

			ascii_line = ""
			line_bytes = 0
			line_cnt += 1
		

	return output
