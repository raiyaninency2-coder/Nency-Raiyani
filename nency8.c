#include<stdio.h>
#include<conio.h>
void main()
{
    float hours, minutes;
    printf("Enter minutes:");
    scanf("%f",&minutes);
    hours=minutes/60;
    printf("hours=%f",hours);
    getch();
}
