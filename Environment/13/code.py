#created: 2012-06-28 15:37:53
EnvironmentDir = './Environment/'
progDir = './Environment/13/'
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
	outVar=0.658244716634*outVar
	outVar=-9.46637754065+-9.46637754065
	outVar=inVar+7.26161155955
	outVar=outVar*outVar
	outVar=inVar*-8.55171125804

	# === end mutable code =============================
	outputs.append(outVar)
#write output to file
outFile = open(progDir + 'output.txt','w')
for outputLine in outputs:
    outFile.write(str(outputLine) + '\n')
outFile.close()
