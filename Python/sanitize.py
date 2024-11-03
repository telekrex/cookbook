def sanitize(text):
	# remove non alpha-numeric
	# characters from the text
	for character in text:
		if character.isalnum():
			# ignore alphanumeric
			pass
		else:
			# remove non alphanumeric characters
			text = text.replace(character, '')
	# then force it to all lowercase
	# and remove trailing white space
	text = text.lower().strip()
	return text