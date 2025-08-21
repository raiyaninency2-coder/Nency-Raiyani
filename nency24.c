#include<stdio.h>
#include<conio.h>
void main()
{
    float gross_sales,net_sales;
    printf("enter gross sales:");
    scanf("%f",&gross_sales);
    net_sales=gross_sales-(0.1*gross_sales);
    printf("net_sales=%f",net_sales);
}
