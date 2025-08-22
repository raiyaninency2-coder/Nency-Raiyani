#include<stdio.h>
#include<conio.h>
void main()
{
    float net_salary,gross_salary,allowances,deductions;
    printf("enter gross_salary:");
    scanf("%f",&gross_salary);
    if(gross_salary>10000)
    {
        allowances=0.1*gross_salary;
        deductions=0.03*gross_salary;
    }
    else
    if(gross_salary>5000)
    {
        allowances=0.07*gross_salary;
        deductions=0.02*gross_salary;
    }
    else
    {
        allowances=0.05*gross_salary;
        deductions=0.01*gross_salary;
    }
    net_salary=gross_salary+allowances-deductions;
    printf("allowances=%f",allowances);
    printf("deductions=%f",deductions);
    printf("net_salary=%f",net_salary);
}
