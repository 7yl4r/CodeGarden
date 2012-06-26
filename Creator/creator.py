#/**************************************************
#          CodeGarden Creator
#    --------------------------------
#this program controlls the evolution of the programs in the codeGarden environment.
#***************************************************/

import os	#for directory operations
from time import gmtime, strftime	#for timestamps
import math	#for statistics computations
import shutil	#for directory deltions
import random	#for mutation chances

POPULATION_CAP = 20
MIN_POP = POPULATION_CAP/2
ENVIRONMENT_DIR = "./Environment"
FALSE = 0
TRUE = 1

MUTATION_RATE = .5
CHANCE_OF_ADDITION  = MUTATION_RATE
CHANCE_OF_COPYERROR = MUTATION_RATE
CHANCE_OF_DELETION  = MUTATION_RATE

clearDataOnRun = FALSE

#TODO: solutionComplexity = 1 #number of lines of code to allow in final solution

#initializes directory & returns name of new program's directory as string
def initNextProg():	
	createdFlag = FALSE
	n = 0
	while not createdFlag:
		progName = str(n)
		dirName = ENVIRONMENT_DIR + '/' + progName;
		try:
			os.makedirs(dirName)
			createdFlag = TRUE
		except:
			n += 1
	return str(dirName)

#generate initial organism program
def createProg():
	dirName = initNextProg()
	#create program code file
	f = open(dirName + '/code.py', 'w')
	code = generateCode(dirName)
	f.write(code)
	f.close()

#generate Header for organism program
def genHeader( pDir ):
    s = '#created: ' + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + '\n'
    s += "EnvironmentDir = './Environment/'\n"
    s += 'progDir = \'' + pDir + '/\'\n'
    s += "\
#read in input file & parse into array of vars\n\
inFile = open(EnvironmentDir + '../input.txt', 'r')\n\
i = 0;\n\
inVars = []\n\
outputs = []\n\
for line in inFile:\n\
    inVars.append(float(line))	#all variables are floating-point\n\
    i += 1\n\
inFile.close()\n\
for inVar in inVars:\n\
	outVar = inVar\n\
	# === mutatable code ===============================\n\
"
    return str(s)

def genFooter():
    s = "\n\
	# === end mutable code =============================\n\
	outputs.append(outVar)\n\
#write output to file\n\
outFile = open(progDir + 'output.txt','w')\n\
for outputLine in outputs:\n\
    outFile.write(str(outputLine) + '\\n')\n\
outFile.close()\n\
"
    return str(s)

#generate code to initialize organism program
def generateCode( progDir ):
    s = genHeader( progDir )
    #TODO add: s += genSeedCode()
    s += genFooter()
    return str(s)

#return randomly generated string of code
#mutations of the form:
#	var = inVars[currentLocation] || outVar || rand(const) || hiddenVar[hiddenVar.size()]
#	opr = + || - || * || /
#	var = var + opr + var
def generateMutation():
    potentialVars = ['inVar', random.uniform(10.0, -10.0), 'outVar']
    potentialOper = ['+', '-', '*']	#no division to avoid div-0 errors
    vL = str(potentialVars[random.randrange(2,len(potentialVars))])	#LHS must be outVar
    vR1= str(potentialVars[random.randrange(0,len(potentialVars))])
    o  = str(potentialOper[random.randrange(0,len(potentialOper))])
    vR2= str(potentialVars[random.randrange(0,len(potentialVars))])
    s = '\t' + vL + '=' + vR1 + o + vR2 + '\n'
    return str(s)

#create mutated genome from parent in 'sourceDir' and return as string
def mutate( sourceDir ):
    sourceFile = open(sourceDir + '/code.py', 'r')
    recordingBool = FALSE
    for line in sourceFile:
        if line == '	# === end mutable code =============================\n':
            break	#stop reading file
        if recordingBool:
            if line != '\n':	#skip blank lines
                #if random.random() < CHANCE_OF_COPYERROR:	#chance of mutating line
                #    pass
                #    #TODO: break line into segments, change one of them
                if random.random() < CHANCE_OF_COPYERROR:	#copy line completely different
                    codeLines.append(generateMutation())
                elif random.random() < CHANCE_OF_DELETION:	#chance of losing line in copy process
                     continue
                else:
                     codeLines.append(line)	#copy line like normal
        if line == '	# === mutatable code ===============================\n':
            recordingBool = TRUE	#start recording
            codeLines = []
    if random.random() < CHANCE_OF_ADDITION:	#chance of adding line
        codeLines.append(generateMutation())
    if random.random() < CHANCE_OF_DELETION:	#chance of deleting line
        try:
            codeLines.pop(random.randrange(0,(len(codeLines)-1)))
        except:
            #no lines in codeLines
            pass
    s = ''
    for line in codeLines:
        s += line
    return str(s)

#create childDir from parentDir genome
def reproduce( parentDir, childDir ):
    childF = open(childDir + '/code.py', 'w')
    s = genHeader(childDir)
    s += mutate(parentDir)
    s += genFooter()
    childF.write(s)
    childF.close()
    return
    
#===ENDDEFs==================================================================================
print 'The Creator has started'
rounds2run = int(raw_input('\t enter number of rounds to run:'))
roundsLeft = rounds2run
if clearDataOnRun:
	dataLog = open('./Creator/dataLog.txt','w')	#create new file for data
	dataLog.write('score\n')
	shutil.rmtree(ENVIRONMENT_DIR)			#delete old programs
	os.makedirs(ENVIRONMENT_DIR)			#make new environment
else:
	dataLog = open('./Creator/dataLog.txt','a')	#open file for data logging
while(roundsLeft > 0):	#loop this entered number of times
	#check population of environment
	#get # of programs
	n_of_programs = 0
	#print 'programs detected:'
	for filename in os.listdir(ENVIRONMENT_DIR):
	    #print  filename
	    n_of_programs += 1

	if n_of_programs < MIN_POP :	#if too small, seed with random programs
		print 'population: ', n_of_programs, ' too small'
		print 'generating additional programs:'
		while n_of_programs < MIN_POP:
			#create program directory
			createProg()
			print n_of_programs
			n_of_programs += 1
	print '=== start of round', rounds2run-roundsLeft, ',\t POP: ', n_of_programs ,' - MUTATION_RATE: ', MUTATION_RATE
	#open & read in current stats from file
	performance = [999999.999] * n_of_programs
	try:
	    statFile = open('./Creator/stats.txt', 'r')
	    i = 0
	    for line in statFile:
		performance[i] = float(line)
		i += 1
	    statFile.close()
	except:		#create file
	    pass
		 
	#update effectiveness stats if needed
	for currentProgramName in os.listdir(ENVIRONMENT_DIR):
	    progDir = ENVIRONMENT_DIR + '/' + currentProgramName
	    try:	#open stat file if exists, create if not
		testOpen = open(progDir + '/output.txt', 'r')
		#print currentProgramName, ' detected performance rating: ', performance[int(currentProgramName)]
		testOpen.close()
	    except:
		os.system("python " + progDir + "/code.py")	#run program
		#compute Sum of squared error
		output = []
		outputF = open(progDir + '/output.txt', 'r')
		for line in outputF:
		    output.append(float(line))
		outputF.close()
		actual = []
		actualF = open('./Creator/realOut.txt', 'r')
		for line in actualF:
		    actual.append(float(line))
		actualF.close()
		SSE = 0	#sum of squared percent error
		i = 0
		for iOutput in output:
		    SSE += math.pow((iOutput - actual[i]),2)/actual[i]	#(x'-x)^2/x
		    i += 1
		performance[int(currentProgramName)] = SSE
		#print currentProgramName, 'tested; recording performance:', SSE
		#TODO: output this generation's list of scores to file for analysis
	bestScore = min(performance)
	bestN = performance.index(bestScore)
	#delete least effective programs until desired population size or threshold performance level met
	while n_of_programs > POPULATION_CAP/2 :
	    low = max(performance)	#higher stat = worse performance
	    lowN = performance.index(low)
	    performance.pop(lowN)
	    print lowN, ', worst score of:', low, ' killed'
	    performance.insert(lowN, -1)	#insert to maintain location in list
	    shutil.rmtree(ENVIRONMENT_DIR + '/' + str(lowN))
	    n_of_programs -= 1

	#remaining programs reproduce
	for currentProgramName in os.listdir(ENVIRONMENT_DIR):
	    progDir = ENVIRONMENT_DIR + '/' + currentProgramName
	    childProgDir = initNextProg()
	    reproduce(progDir, childProgDir)
	    print progDir + ' begat \t' + childProgDir

	#TODO: add seed(s)

	# write to statFile
	statFile = open('./Creator/stats.txt', 'w')
	for stat in performance:
	    statFile.write(str(stat) + '\n')
	statFile.close()
	print '=== end of round', rounds2run-roundsLeft, ',\t BEST: ', bestN ,' - SCORE: ', bestScore
        dataLog.write(str(bestScore)+'\n')
        roundsLeft -= 1
        if bestScore == 0:
            print '=== CYCLE STOPPED. Perfect solution found. ==='
            break
dataLog.close()
