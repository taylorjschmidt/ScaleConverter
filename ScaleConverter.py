from fractions import Fraction

def ScaleFactorArch(scale):
	scaleFactor = 1 / scale * 12
	return scaleFactor
	
def ScaleFactorEng(scale):
	scaleFactor = scale * 12
	return scaleFactor
	
def multiplier(current,desired):
	multiply = current / desired * 100
	print "\nYou should scale your file by %.2f percent\n" % multiply

def start():
	print """
I can easily help you convert your drawing or model from one scale to another.
Please enter the type of scale you are using.
Enter 'A' for Architectural Scale
Enter 'E' for Engineering Scale
"""
	choice()
	
def choice():
	valid = ['A', 'a', 'E', 'e']
	scaleType = raw_input("\nMake your selection here: ")
	if scaleType in valid:
		inputCheck(scaleType)
		
	else:
		print "Sorry, I don't understand that input. Let's try again."
		choice()
		
def inputCheck(entry):

	if entry == 'A' or entry == 'a':
		currentScale = float(Fraction(raw_input("Enter current scale: 1'-0\" = ")))
		desiredScale = float(Fraction(raw_input("Enter desired scale: 1'-0\" = ")))
	
		currentFactor = ScaleFactorArch(currentScale)
		desiredFactor = ScaleFactorArch(desiredScale)
		multiplier(currentFactor, desiredFactor)
	
	elif entry == 'E' or entry == 'e':
		currentScale = float(raw_input("Enter current scale: 1:"))
		desiredScale = float(raw_input("Enter desired scale: 1:"))
	
		currentFactor = ScaleFactorEng(currentScale)
		desiredFactor = ScaleFactorEng(desiredScale)
		multiplier(currentFactor, desiredFactor)
	
start()
