import random

#opening a file for generating frequencies corresponding to characters of the sample file.
file = open("freq.txt" , 'w')

#function for manipulating the characters
def getchar(char):
	if(char.isalpha()):
		char = char.lower()
		return char
	elif(char == " "):
		return "space"
	elif(char == "."):
		return "period"
	elif(char == "\n"):
		return "newline"
	return None

#if rand==1 then this function will generate frequency randomly
#if rand==0 then this function will generate frquency corresponding to the sample text file.
def generate_freq(rand):
	if(rand):
		#freq for alphabets
		for i in range(26):
			fq = random.randint(30,1000)
			add = chr(i + ord('a')) + " " + str(fq) + "\n"
			file.write(add)

		#freq for space
		fq = random.randint(30,1000)
		add = "space" + " " + str(fq) + "\n"
		file.write(add)

		#freq for period
		fq = random.randint(30,1000)
		add = "period" + " " + str(fq) + "\n"
		file.write(add)

		#freq for newline
		fq = random.randint(30,1000)
		add = "newline" + " " + str(fq) + "\n"
		file.write(add)

		#freq for end of message
		fq = random.randint(30,1000)
		add = "EOM" + " " + str(fq) + "\n"
		file.write(add)

	else:
		#reading the file for which frequency is to be generated(sample.txt)
		textfile = open("sample.txt" , 'r')

		#making and intiallizing a dictionary
		freqs = dict()
		for i in range(26):
			freqs[chr(i + ord('a'))] = 0
		freqs["space"] = 0
		freqs["EOM"] = 0
		freqs["newline"] = 0
		freqs["period"] = 0

		#iterating through the text file
		while True:
			#reading the file character by character
			char = textfile.read(1)

			#when we reach end of file then char==0, so puttinf frequency of EOM=1 and breaking from loop
			if(not char):
				freqs["EOM"] += 1
				break

			#for alphabets, space, period and newline
			char = getchar(char)
			freqs[char] += 1

		#iterating through the dictionary and writing the (character name+" "+frequency) of each character to the output file(freq.txt)
		for char in freqs:
			add = char + " " + str(freqs[char]) + "\n"
			file.write(add)

	file.close()