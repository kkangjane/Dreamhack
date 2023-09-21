#include <stdio.h>
#include <unistd.h>

void get_shell()
{
	char *cmd = "/bin/sh";
	char *args[] = {cmd, NULL};
	execve(cmd, args, NULL);
}
int main()
{
	char buf[0x28];
	printf("Input: ");
	scanf("%s", &buf);
	return 0;
}
