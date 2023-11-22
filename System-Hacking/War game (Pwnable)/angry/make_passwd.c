#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define JOKER "\x5f\x75\x43\x30\x6e\x5f\x00"

int main(void)
{
    time_t time1;
    printf("%s_%d", JOKER, (int) time(&time1));
}