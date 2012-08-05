#created: 2012-06-28 15:37:53
EnvironmentDir = './Environment/'
progDir = './Environment/0/'
#read in input file & parse into array of vars
inFile = open(EnvironmentDir + '../Data/input.txt', 'r')
i = 0;
inVars = []
outputs = []
for line in inFile:
    inVars.append(float(line))	#all variables are floating-point
    i += 1
inFile.close()
for inVar in inVars:
	outVar = inVar
	# === mutatable code ===============================
	outVar=inVar+inVar
	outVar=-6.27475803201+outVar

	# === end mutable code =============================
	outputs.append(outVar)
#write output to file
outFile = open(progDir + 'output.txt','w')
for outputLine in outputs:
    outFile.write(str(outputLine) + '\n')
outFile.close()
