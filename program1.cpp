#include<stdio.h>
int main()
{
    int a,b,c;
    printf("�nter 3 values:");
    scanf("%d%d%d",&a,&b,&c);
    if(a==b==c)
        printf("�ll values are equal.\n");
    else
    if(a>=b&&a>=c)
        printf("%d is largest.\n",a);
    else
    if(b>=a&&b>=c)
        printf("%d is largest.\n",b);
    else
        printf("%d is largest.\n",c);

    if(a<=b&&a<=c)
        printf("%d is smallest.\n",a);
    else
    if(b<=a&&b<=c)
        printf("%d is smallest.\n",b);
    else
        printf("%d is smallest.\n",c);


}
