def fibNums():
	n = 10
	print "printing the first %d fibonacci numbers" %n
	fibonacci = []
	fibonacci = [1, 1]
	print "%d " %fibonacci[0]
	print "%d " %fibonacci[1]
	for i in range (2, n):
		fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
		print "%d " %fibonacci[i]

def main():
	print "main function"
	print "calling function fibNums"
	fibNums()		
	
if __name__== "__main__":
  main()
else:
	print "nhp"  


