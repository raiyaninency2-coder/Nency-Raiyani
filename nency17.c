#include<stdio.h>
#include<conio.h>
void main()
{
    float i,p,r,n;
    printf("Enter p,r,n:");
    scanf("%f%f%f",&p,&r,&n);
    i=p*r*n/100;
    printf("\n i=%f",i);
    getch();
}
