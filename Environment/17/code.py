#created: 2012-06-26 00:10:49
EnvironmentDir = './Environment/'
progDir = './Environment/17/'
#read in input file & parse into array of vars
inFile = open(EnvironmentDir + '../input.txt', 'r')
i = 0;
inVars = []
outputs = []
for line in inFile:
    inVars.append(float(line))	#all variables are floating-point
    i += 1
inFile.close()
for inVar in inVars:
	outVar = 0
	# === mutatable code ===============================

	# === end mutable code =============================
	outputs.append(outVar)
#write output to file
outFile = open(progDir + 'output.txt','w')
for outputLine in outputs:
    outFile.write(str(outputLine) + '\n')
outFile.close()
