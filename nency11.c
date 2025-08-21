#include<stdio.h>
#include<conio.h>
void main()
{
    float dollors,pounds,rupees;
    printf("Enter dollors:");
    scanf("%f",&dollors);
    rupees=dollors*48;
    printf("rupees=%f",rupees);
    pounds=rupees/70;
    printf("pounds=%f",pounds);
    getch();
}
