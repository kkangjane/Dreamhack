char correct[] = "DREAMHACK!";

int main()
{
    char s;

    memset(&s, 0, 0x10);
    read(0, &s, 0x400);
    validate(&s, 128);
}

int validate(char a1[], unsigned int a2)
{
    unsigned int i;
    int j;

    for (i = 0; i <= 9; i++)
    {
        if (a1[i] != correct[i])
            exit(0);
    }
    for (j = 11; a2 > j; j++)
    {
        if (a1[j] != a1[j + 1] + 1)
            exit(0);
    }
    return 0;
}