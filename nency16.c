#include<stdio.h>
#include<conio.h>
void main()
{
    float fahrenheit,celcius;
    printf("Enter fahrenheit:");
    scanf("%f",&fahrenheit);
    celcius=(5/9)*(fahrenheit-32);
    printf("celcius=%f",celcius);
    getch();
}
