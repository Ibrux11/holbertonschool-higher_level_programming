class Rectangle:
	"""
	A class used to represent a Rectangle

	Attributes
	----------
	number_of_instances : int
		Class attribute that counts the number of instances
	print_symbol : any
		Class attribute used as the symbol for string representation

	Methods
	-------
	__init__(self, width=0, height=0)
		Initializes the rectangle with optional width and height
	width(self)
		Getter for the width attribute
	width(self, value)
		Setter for the width attribute
	height(self)
		Getter for the height attribute
	height(self, value)
		Setter for the height attribute
	area(self)
		Returns the area of the rectangle
	perimeter(self)
		Returns the perimeter of the rectangle
	__str__(self)
		Returns a string representation of the rectangle
	__repr__(self)
		Returns a string representation for recreating the instance
	__del__(self)
		Prints a message when an instance is deleted
	bigger_or_equal(rect_1, rect_2)
		Static method that returns the biggest rectangle based on the area
	square(cls, size=0)
		Class method that returns a new Rectangle instance with width == height == size
	"""

	number_of_instances = 0
	print_symbol = "#"

	def __init__(self, width=0, height=0):
		"""
		Initializes the rectangle with optional width and height

		Parameters
		----------
		width : int, optional
			The width of the rectangle (default is 0)
		height : int, optional
			The height of the rectangle (default is 0)
		"""
		self.width = width
		self.height = height
		Rectangle.number_of_instances += 1

	@property
	def width(self):
		"""Getter for the width attribute"""
		return self.__width

	@width.setter
	def width(self, value):
		"""
		Setter for the width attribute

		Parameters
		----------
		value : int
			The new width of the rectangle

		Raises
		------
		TypeError
			If the width is not an integer
		ValueError
			If the width is less than 0
		"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Getter for the height attribute"""
		return self.__height

	@height.setter
	def height(self, value):
		"""
		Setter for the height attribute

		Parameters
		----------
		value : int
			The new height of the rectangle

		Raises
		------
		TypeError
			If the height is not an integer
		ValueError
			If the height is less than 0
		"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

	def area(self):
		"""
		Returns the area of the rectangle

		Returns
		-------
		int
			The area of the rectangle
		"""
		return self.width * self.height

	def perimeter(self):
		"""
		Returns the perimeter of the rectangle

		Returns
		-------
		int
			The perimeter of the rectangle, or 0 if width or height is 0
		"""
		if self.width == 0 or self.height == 0:
			return 0
		return 2 * (self.width + self.height)

	def __str__(self):
		"""
		Returns a string representation of the rectangle

		Returns
		-------
		str
			The rectangle represented with the character stored in print_symbol
		"""
		if self.width == 0 or self.height == 0:
			return ""
		return "\n".join([str(self.print_symbol) * self.width for _ in range(self.height)])

	def __repr__(self):
		"""
		Returns a string representation for recreating the instance

		Returns
		-------
		str
			A string representation of the rectangle
		"""
		return f"Rectangle({self.width}, {self.height})"

	def __del__(self):
		"""
		Prints a message when an instance is deleted
		"""
		print("Bye rectangle...")
		Rectangle.number_of_instances -= 1

	@staticmethod
	def bigger_or_equal(rect_1, rect_2):
		"""
		Returns the biggest rectangle based on the area

		Parameters
		----------
		rect_1 : Rectangle
			The first rectangle
		rect_2 : Rectangle
			The second rectangle

		Returns
		-------
		Rectangle
			The rectangle with the bigger area, or rect_1 if both have the same area

		Raises
		------
		TypeError
			If rect_1 or rect_2 is not an instance of Rectangle
		"""
		if not isinstance(rect_1, Rectangle):
			raise TypeError("rect_1 must be an instance of Rectangle")
		if not isinstance(rect_2, Rectangle):
			raise TypeError("rect_2 must be an instance of Rectangle")
		if rect_1.area() >= rect_2.area():
			return rect_1
		return rect_2

	@classmethod
	def square(cls, size=0):
		"""
		Returns a new Rectangle instance with width == height == size

		Parameters
		----------
		size : int, optional
			The size of the new rectangle (default is 0)

		Returns
		-------
		Rectangle
			A new instance of Rectangle with width and height equal to size
		"""
		return cls(size, size)