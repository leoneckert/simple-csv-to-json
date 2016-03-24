import sys
# call like this:
# python csv_to_json.py inputfile outputfile

printToConsole = False

first = True
element_keys = list()

numLines = 0  
for line in open(sys.argv[1]):
	numLines+=1


outPutFileName = sys.argv[2]
outPutFileName = outPutFileName
outputFile = open(outPutFileName, "w")

outputFile.write("[" + "\n") #write to output
if printToConsole: print "["

linecount = 0
for line in open(sys.argv[1]):
	line = line.strip()
	if first == True:
		elems = line.split(",")
		for elem in elems:
			element_keys.append(elem)
		first = False
	else:
		elems = line.split(",")
		if printToConsole: print "\t{"
		outputFile.write("\t{" + "\n") #write to output
		for i in range(len(elems)):
			if elems[i] == "\N":
				linetoPrint = "\t\t" + element_keys[i] + ": " + "null"
			else:
				linetoPrint = "\t\t" + element_keys[i] + ": " + elems[i]
			
			if(i != len(elems)-1):
				if printToConsole: print linetoPrint + ","
				outputFile.write(linetoPrint + "," + "\n") #write to output
			else:
				if printToConsole: print linetoPrint
				outputFile.write(linetoPrint + "\n") #write to output 
		if linecount != numLines-1:
			if printToConsole: print "\t},"
			outputFile.write("\t}," + "\n") #write to output 
		else:
			if printToConsole: print "\t}"
			outputFile.write("\t}" + "\n") #write to output 
	linecount += 1

outputFile.write("]") #write to output
if printToConsole: print "]"
outputFile.close() #write to output



