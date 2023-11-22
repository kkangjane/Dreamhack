// gcc -o fsb1 fsb1.c -m32 -mpreferred-stack-boundary=2

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char flag_buf[50];
void initialize() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
}

int main()
{
	FILE *fp;
	char buf[256];
	initialize();
	memset(buf, 0, sizeof(buf));
	fp = fopen('./flag', "r");
	fread(flag_buf, 1, sizeof(flag_buf), fp); //flag 파일의 내용을 읽어 flag_buf 변수에 저장하고 있다.
	printf("Input: ");
	read(0, buf, sizeof(buf)-1);
	printf(buf); // buf 변수를 그대로 출력하므로 fsb 취약점이 존재한다.
	return 0;
}