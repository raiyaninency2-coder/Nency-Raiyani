#include<stdio.h>
#include<conio.h>
void main()
{
    float a,b,c;
    printf("enter 3 values:");
    scanf("%f%f%f",&a,&b,&c);
    if(a==b==c)
        printf("all values are equal.\n");
    else
    if(a<b&&a<c)
        printf("%f is smallest.\n",a);
    else
    if(b<a&&b<c)
        printf("%f is smallest value",b);
    else

        printf("%f is smallest value",c);

}
