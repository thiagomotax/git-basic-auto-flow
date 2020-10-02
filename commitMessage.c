#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char commitMessage[72];
	scanf("%s", &commitMessage); //pega a entrada do subprocess
	FILE* dir = fopen(".git", "r"); //tenta abrir a basta .git
	char initInstruction[]= "git init";
	char addInstruction[] = "git add .";
	char pullInstruction[] = "git pull origin master";
	char pushInstruction[] = "git push origin master";

	char commitInstruction[] = "git commit -m ";
	strcat(commitInstruction, commitMessage);

	if(dir != NULL){  //verifica se a pasta .git existe, e se nao existe, cria uma
		system(initInstruction);
		printf("\nRepositorio git criado");
	}
	else{
		printf("\nRepositprio git encontrado");
	}

	printf("\nArquivos adicionados a stanging area");
	system(addInstruction);

	printf("\nCommit efetuado com sucesso");
	system(commitInstruction);

	printf("\nSincronizando coms o repositório remoto");
	system(pullInstruction);

	printf("\nEnviando alterações para o repositório remoto");
	system(pullInstruction);

	return 0;
}


