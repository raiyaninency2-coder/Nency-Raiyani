#include<stdio.h>
#include<conio.h>
void main()
{
    float celcius,fahrenheit;
    printf("Enter celcius:");
    scanf("%f",&celcius);
    fahrenheit=((9/5)*celcius)+32;
    printf("fahrenheit=%f",fahrenheit);
    getch();
}
