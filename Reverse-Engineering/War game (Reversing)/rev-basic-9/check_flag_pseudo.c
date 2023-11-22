int check_flag(char *input)
{
	int len = strlen(input);
	if ((len + 1) % 8 == 1)
		return -1;
	for (int i = 0; i < len + 1; i += 8)
		func(&input[i]);
	return (memcmp(input, &something, 0x19ui64) == 0)
}

void func(char *str)
{
	char key[16] = "I_am_KEY";
	
	char *result;
	result = *input_str;
	v2 = *input_str;
	for (int i = 0; i < 16; i++)
	{
		for (int j = 0; j < 8; j++)
		{
			v2 = ROR(input_str[(j+1)&7] + a[key[j]^v2]), 5)
			input_str[(j+1)&7] = v2;
		}
		result = i + 1;
	}
	return result;
}