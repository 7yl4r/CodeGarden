#created: 2012-06-25 01:05:54

#imports

#read in input file & parse into array of vars
inFile = open('./../input.txt', 'r')
i = 0;
for line in inFile:
    inVars[i] = float(line)	#all variables are floating-point
    i += 1
#Vars needed for multiple-input dependance:
#windowSize = i/10
#currentLocation = windowSize
currentLocation = 0
for currentLocation in inVars:
	#var = inVars[currentLocation+randbtwn(-windowSize,+windowSize)] || output[randbtwn(0,output.size) || rand(const) 
	#opr = + || - || * || /
	#output[rand()] = inVars[currentLocation+randbtwn(-windowSize,+windowSize)]

	#mutations of the form:
	#output[count] = <input||output||const> <operator> <input||output||const>

	# === mutatable code ===============================

	# === end mutable code =============================

#write output to file
outFile = open('./output.txt','w')

