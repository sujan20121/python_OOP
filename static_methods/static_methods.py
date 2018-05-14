#The static methods in Python don't have access to 'self'.
#The static methods don't require an object instantiation in order to work.

class car(object):
	def make_noise():
		print('honkkk...')
	#the method make_noise() is a static method
		
def main():
	car.make_noise()
	
main()