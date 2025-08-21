#include<stdio.h>
#include<conio.h>
void main()
{
    float maths_mark,physics_mark,chemistry_mark,average,total;
    printf("enter marks:");
    scanf("%f%f%f",&maths_mark,&chemistry_mark,&physics_mark);
    total=maths_mark+chemistry_mark+physics_mark;
    average=total/3;
    printf("total=%f",total);
    printf("average=%f",average);
}
