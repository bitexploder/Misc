def pretty_format_hex(s, bytes_per_line):
	"""
	Returns a human readable dump of the hex, like hexdump -C
	"""
	# something fun
	the_hex = binascii.hexlify(s)
	the_hex_list = []

	# Convert input string into list of ascii hex representations
	for byte in range(0, len(the_hex)/2):
		the_hex_list.append(the_hex[byte*2:byte*2+2])

	cool_ascii = ''
	cool_hex = ''
	final_out = ''
	cnt_line = 0
	cnt_total = 0

	for byte in the_hex_list:
		# Clean up the ASCII representation
		new_char = chr(int(byte, 16)) # Convert to ascii from hex string
		if ord(new_char) < 32 or ord(new_char) > 126:
			new_char = '.'
		if new_char in ['\t', ' ']:
			new_char = '.'
		
		cool_ascii += new_char
		cool_hex += byte + ' '

		# Append a line to final_out
		if cnt_line == bytes_per_line-1 or cnt_total == len(the_hex_list)-1:
			pad_bytes = bytes_per_line - len(cool_ascii)
			cool_ascii = cool_ascii + ' ' * (pad_bytes-1)
			final_out += "%s   %s|%s|\n" % (
				cool_hex, '   ' * pad_bytes, cool_ascii)
			cool_hex = ''
			cool_ascii = ''
			cnt_line = 0

		cnt_line += 1
		cnt_total += 1

	return final_out
