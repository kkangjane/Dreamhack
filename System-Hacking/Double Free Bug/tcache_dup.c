// Name: tcache_dup.c
// Compile: gcc -o tcache_dup tcache_dup.c

#include <stdio.h>
#include <stdlib.h>

int main(){
	void *chunk = malloc(0x20);
	printf("Chunk to be double-freed: %p\n", chunk);

	free(chunk);

	*(char *)(chunk + 8) = 0xff; //mainpulate chunk->key
	free(chunk);

	printf("First allocation: %p\n", malloc(0x20));
	printf("Second allofcation: %p\n", malloc(0x20));

	return 0;
}
