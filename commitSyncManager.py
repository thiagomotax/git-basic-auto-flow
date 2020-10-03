import subprocess
def errorMessage(operation):
	print(f"Something went wrong in {operation}")

def generateMessage(operation):
	return [f"Trying to {operation} files", f"{operation} done"]

def doStagingArea():
	try: 
		message = generateMessage("Add")
		print(message[0])
		createSubProcess(['git', 'add', '.'])
		print(message[1])
	except: 	
		errorMessage("Add")


def doCommit():
	try: 
		message = generateMessage("Commit")
		commitMessage = input("Please type the description for commit: ")
		print(message[0])
		createSubProcess(['git', 'commit', '-m', commitMessage])
		print(message[1])
	except: 	
		errorMessage("Commit")


def createSubProcess(args):
	args = args
	p = subprocess.Popen(args,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True)
	p.communicate()

doStagingArea()
doCommit()

# print("\n-----------------------\nSaida: \n" + saida[0] + "\n------------------------\n");
# print("\n-----------------------\nErros: \n" + saida[1] + "\n------------------------\n");

print("\n\nPrograma python finalizado")