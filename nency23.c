#include<stdio.h>
#include<conio.h>
void main()
{
    float net_salary,gross_salary,allowance,deduction;
    printf("Enter gross salary:");
    scanf("%f",&gross_salary);
    allowance=0.1*gross_salary;
    deduction=0.03*gross_salary;
    net_salary=gross_salary+allowance-deduction;
    printf("allowance=%f",allowance);
    printf("deduction=%f",deduction);
    printf("net_salary=%f",net_salary);
    getch();
}
