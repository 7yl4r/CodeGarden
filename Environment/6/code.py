#created: 2012-06-28 15:37:53
EnvironmentDir = './Environment/'
progDir = './Environment/6/'
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
	outVar=-6.10546480765+inVar
	outVar=outVar+outVar
	outVar=-0.928068095389+outVar
	outVar=outVar-4.35230787144

	# === end mutable code =============================
	outputs.append(outVar)
#write output to file
outFile = open(progDir + 'output.txt','w')
for outputLine in outputs:
    outFile.write(str(outputLine) + '\n')
outFile.close()
