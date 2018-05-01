class Route:
    def __init__(self, from_city, to_city, length, color):
        self.from_city = from_city
        self.to_city = to_city
        self.length = int(length)
        self.color = color
        self.claimed = ''  # one/two of 'bgkoprwy' or '-'

    def claim(self, color):
    	self.claimed += color
    	return True

    def occupied(self):
    	return len(self.color) == len(self.claimed)

    def __str__(self):
        return "%s => %s, %s (%s)" % (self.from_city, self.to_city, self.length, self.color)
