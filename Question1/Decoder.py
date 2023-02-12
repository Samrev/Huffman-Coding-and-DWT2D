from Rohan_Ayush_A1 import build_codewords, build_huffman_tree,Alphabet
from freq_generator import getchar , generate_freq


#this will generate freqency of all the characters in freq.txt 
generate_freq(0)

# Reading the frequency generated
file_freq = open("freq.txt" , 'r')
freq = []

#Creating a list of alphabet objects
for line in file_freq:
	alphafreq = list(line.split(" "))
	alpha = alphafreq[0]
	frequency = int(alphafreq[1])
	freq.append(Alphabet(alpha , frequency))
file_freq.close()

#Building the huffman tree from the list of alphabet objects
root = build_huffman_tree(freq)


#File to be decoded
encoded_file = open("encoded_text.txt" , 'r')

#File in which decoded text will be written
decoded_file = open("decoded_text.txt" , 'w')

#decoding
node = root
while True:
	#reading the file to be decoded, char by char
	char = encoded_file.read(1)

	#if we reach end of file, we break out of the loop
	if(not char):
		break

	# char=1 means right child(that's how the code has been generated)
	if(char == '1'):
		node = node.get_right()
	# char=0 means left child
	elif(char == '0'):
		node = node.get_left()

	#If nodename != 'inode', means it is leaf node and hence it corresponds to a character
	if(node.get_alpha() != 'inode'):
		#handling new line 
		if(node.get_alpha() == "newline"):
			decoded_file.write("\n")
		#Handling end of message
		elif(node.get_alpha() == "EOM"):
			break
		#handling space
		elif(node.get_alpha() == "space"):
			decoded_file.write(" ")
		#handling period
		elif(node.get_alpha() == "period"):
			decoded_file.write(".")
		#handling alphabets
		else:
			decoded_file.write(node.get_alpha())
		#reseting the node to the root of the huffman tree
		node = root