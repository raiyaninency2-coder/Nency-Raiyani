#include<stdio.h>
#include<conio.h>
int main()
{
    int hours,minutes;
    printf("Enter hours:");
    scanf("%d",&hours);
    minutes=60*hours;
    printf("minutes=%d",minutes);
    getch();
}
