#include<stdio.h>
#include<conio.h>
void main()
{
    float bytes,KB,MB,GB;
    printf("Enter bytes:");
    scanf("%f",&bytes);
    KB=bytes/1024;
    MB=bytes/1048576;
    GB=bytes/1073741824;
    printf("\nKB=%f",KB);
    printf("\nMB=%f",MB);
    printf("\nGB=%f",GB);
    getch();
}
