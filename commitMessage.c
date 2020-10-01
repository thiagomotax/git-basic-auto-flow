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
	FILE* dir = fopen(".git", "r");
	char initInstruction[]= "git init";
	char addInstruction[] = "git add .";

	printf("Type the commit message to sync data with repository");
	fgets(commitMessage, sizeof(commitMessage), stdin);
	char *commitInstruction = "git commit -m 'teste";
	//concat("git commit -m", commitMessage);
	
	if(!dir)
		system(initInstruction);
	system(addInstruction);
	system(&commitInstruction);

	printf("Commit efetuado com sucesso");
	perror("Programa C: mensagem na saida de erro");

	sleep(10);
	return 0;
}


