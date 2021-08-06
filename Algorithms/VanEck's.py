#Van Eck's Algorithm or Numberphile
# Python3 program to print Nth
# sequence is 0 0 1 0 2 0 2 2 1 6 0
# term of Van Eck's sequence
MAX = 1000
sequence = [0] * (MAX + 1)

# Utility function to compute
# Van Eck's sequence
def vanEckSequence() :

	# Initialize sequence array
	for i in range(MAX) :
		sequence[i] = 0

	# Loop to generate sequence
	for i in range(MAX) :
		
		# Check if sequence[i] has occurred
		# previously or is new to sequence
		for j in range(i - 1 , -1, -1) :
			if (sequence[j] == sequence[i]) :

				# If occurrence found
				# then the next term will be
				# how far back this last term
				# occurred previously
				sequence[i + 1] = i - j
				break

# Utility function to return
# Nth term of sequence
def getNthTerm(n) :

	return sequence[n]

# Driver code
if __name__ == "__main__" :

	# Pre-compute Van Eck's sequence
	vanEckSequence()

	n = int(input("Enter a index number at which the vanErc's number to be print: "))

	# Print nth term of the sequence
	print(getNthTerm(n))

