#include<stdio.h>
#include<conio.h>
void main()
{
    float m1,m2,m3,total,average;
    printf("enter marks:");
    scanf("%f%f%f",&m1,&m2,&m3);
    if(m1<35||m2<35||m3<35)
    {
        printf("\n student has failed");
    }
    total=m1+m2+m3;
    average=total/3;
    printf("\n total=%f",total);
    printf("\n average=%f",average);
    if(average>=70)
    {
        printf("\n grade=distinction");
    }
    else
    if(average>=60)
    {
        printf("\n grade=first class");
    }
    else
    if(average>=50)
    {
        printf("\n grade=second class");
    }
    else
    if(average>=35)
    {
        printf("\n grade=third class");
    }
    else
    {
        printf("\n result=fail");
    }
}
