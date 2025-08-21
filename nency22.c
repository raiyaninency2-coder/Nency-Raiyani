#include<stdio.h.>
#include<conio.h.>
void main()
{
    int a,b,temp;
    printf("Enter a and b:");
    scanf("%d%d",&a,&b);
    printf("before swapping: a=%d,b=%d",a,b);
    temp=a;
    a=b;
    b=temp;
    printf("after swapping:a=%d,b=%d",a,b);
    getch();
}
