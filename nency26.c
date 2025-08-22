#include<stdio.h>
#include<conio.h>
void main()
{
    float a,b;
    printf("Enter two values:");
    scanf("%f%f",&a,&b);
    if(a>b)
        printf("%f>%f",a,b);
    else
    if(a<b)
        printf("%f<%f",a,b);
    else
        printf("%f=%f",a,b);
}


