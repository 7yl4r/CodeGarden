#/**************************************************
#          CodeGarden Creator
#          --------------------------------
#this program controlls the evolution of the programs in the codeGarden environment.
#***************************************************/

import os	#for directory operations
from time import gmtime, strftime	#for timestamps
import math	#for statistics computations
import shutil	#for directory deltions

POPULATION_CAP = 20
MIN_POP = 5
ENVIRONMENT_DIR = "./Environment"
FALSE = 0
TRUE = 1

print 'The Creator has started'

def initNextProg():	#initializes directory & returns name
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

def createProg():
	dirName = initNextProg()
	#create program code file
	f = open(dirName + '/code.py', 'w')
	code = generateCode(dirName)
	f.write(code)
	f.close()

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
	outVar = 0\n\
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

def generateCode( progDir ):
    s = genHeader( progDir )
    #TODO add: s += genSeedCode()
    s += genFooter()
    return s

def reproduce( parentDir, childDir ):
    childF = open(childDir + '/code.py', 'w')
    s = genHeader(childDir)
    #s += mutate(parentDir)
    s += genFooter()
    childF.write(s)
    childF.close()
    return
    

#check population of environment
#get # of programs
n_of_programs = 0
print 'programs detected:'
for filename in os.listdir(ENVIRONMENT_DIR):
    print  filename
    n_of_programs += 1

if n_of_programs < MIN_POP :	#if too small, seed with random programs
	print n_of_programs, ' too small'
	print 'generating additional programs:'
	while n_of_programs < MIN_POP:
		#create program directory
		createProg()
		print n_of_programs
		n_of_programs += 1
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
        print currentProgramName, ' detected performance rating: ', performance[int(currentProgramName)]
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
        SSE = 0	#sum of square error
	i = 0
        for iOutput in output:
            SSE += math.pow((iOutput - actual[i]),2)	#(x'-x)^2
            i += 1
        performance[int(currentProgramName)] = SSE
        print currentProgramName, 'tested; recording performance:', SSE

#delete least effective programs until desired population size or threshold performance level met
while n_of_programs > POPULATION_CAP :
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

# write to statFile
statFile = open('./Creator/stats.txt', 'w')
for stat in performance:
    statFile.write(str(stat) + '\n')
statFile.close()
