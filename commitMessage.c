#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* concat(const char *s1, const char *s2)
{
    char *result = malloc(strlen(s1) + strlen(s2) + 1); // +1 for the null-terminator
    // in real code you would check for errors in malloc here
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

int main(){
	char commitMessage[72];
	scanf("%s", &commitMessage);
	FILE* dir = fopen(".git", "r");
	char initInstruction[]= "git init";
	char addInstruction[] = "git add .";
	char pullInstruction[] = "git pull origin master";
	char pushInstruction[] = "git push origin master";

	// char commitInstruction[] = "git commit -m testexx";
	char commitInstruction[] = "git commit -m ";

	strcat(commitInstruction, commitMessage);

	
	if(!dir)
		system(initInstruction);
	system(addInstruction);
	system(commitInstruction);

	printf("Commit efetuado com sucesso");
	perror("Programa C: mensagem na saida de erro");

	return 0;
}


