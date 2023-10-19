# include <unistd.h>
int main()
{
    char    *buf;
    int fd = open("/home/shell_basic/flag_name_is_loooooong", RD_ONLY, 0);
    read(fd, buf, 0x30);
    write(1, buf, 0x30);
}