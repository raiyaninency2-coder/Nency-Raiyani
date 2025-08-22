#include<stdio.h>
#include<conio.h>
void main()
{
    float gross_sales,net_sales,discount;
    printf("enter gross_sales:");
    scanf("%f",&gross_sales);
    if(gross_sales>20000)
        discount=0.15*gross_sales;
    else
    if(gross_sales>10000)
        discount=0.1*gross_sales;
    else
        discount=0.05*gross_sales;
    net_sales=gross_sales-discount;
    printf("discount=%f",discount);
    printf("net_sales=%f",net_sales);
}
