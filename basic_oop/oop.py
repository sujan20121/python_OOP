class Dog:
	def __init__(self,name="",height=0,weight=0):
		self.name = name
		self.height = height
		self.weight = weight

	def run(self):
		print("{} the dog runs".format(self.name))

def main():
	chuck = Dog("Chuck",22,11)
	chuck.run()
	saibon = Dog()

main()
