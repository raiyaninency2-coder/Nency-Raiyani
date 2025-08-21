#include<stdio.h>
#include<conio.h>
void main()
{
    float perimeter,area,l,b;
    printf("Enter l and b :");
    scanf("%f%f",&l,&b);
    perimeter=2*(l+b);
    printf("perimeter=%f",perimeter);
    area=l*b;
    printf("area=%f",area);
    getch();

}
