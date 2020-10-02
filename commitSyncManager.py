import subprocess

args = ['a.exe']
p = subprocess.Popen(args,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True)

saida = p.communicate("MensagemCommit") #tentar receber por args via terminal

print("\n-----------------------\nSaida: \n" + saida[0] + "\n------------------------\n");
print("\n-----------------------\nErros: \n" + saida[1] + "\n------------------------\n");

print("Programa python finalizado")