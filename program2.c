#include<stdio.h>
int main()
{
    int a,b;
    printf("�nter  values:");
    scanf("%d%d",&a,&b);
    if(a==b)
        printf("�ll values are equal.\n");
    else
    if(a>=b)
        printf("%d is largest.\n",a);
    if(b>=a)
        printf("%d is largest.\n",b);

    if(a<=b)
        printf("%d is smallest.\n",a);
    else
        printf("%d is smallest.\n",b);


}
