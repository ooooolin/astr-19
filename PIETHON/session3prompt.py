def Printfunction(x):
	return x**3+8

def main():
	x = 9
	print (Printfunction(x))

	if Printfunction(x) > 27:
		print ("YAY!")

if __name__=="__main__":
	main()