import subprocess
def errorMessage(operation):
	print(f"Something went wrong in {operation}")

def generateMessage(operation):
	return [f"Trying to {operation} files", f"{operation} done"]

def createSubProcess(args):
	args = args
	p = subprocess.Popen(args,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True)
	return p.communicate()

def doVerifyRemote():
	output, error = createSubProcess(['git', 'remote'])
	if output == '':
		raise Exception("Please, first connect to remote (or you can start the project with clone)")

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

def doPullSync():
	try: 
		doVerifyRemote();
		message = generateMessage("Pull")
		print(message[0])
		createSubProcess(['git', 'pull', 'origin', 'master'])
		print(message[1])
	except:
		errorMessage("Pull")

def doPushSync():
	try: 
		doVerifyRemote();
		message = generateMessage("Push")
		print(message[0])
		createSubProcess(['git', 'push', 'origin', 'master'])
		print(message[1])
	except:
		errorMessage("Push")

def doGitFlow():
	try: 
		doPullSync()
		doStagingArea()
		doCommit()
		doPushSync()
	except:
		errorMessage("Push")


doGitFlow()

# print("\n-----------------------\nSaida: \n" + saida[0] + "\n------------------------\n");
# print("\n-----------------------\nErros: \n" + saida[1] + "\n------------------------\n");

print("\n\nPython program finished")