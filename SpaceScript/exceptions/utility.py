class Error(Exception):
	"""Parent class for all exceptions and errors in this module."""
	pass

class dimensionError(Error):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message
