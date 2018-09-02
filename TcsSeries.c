#include<stdio.h>
#include<stdlib.h>
int main(int argc , char * argv[])
{
    int a , b , i ;
    a=atoi(argv[1]);
    if(a%2==0)
    {
        b=(a/2)-1;
        i=pow(3,b);
        printf("%d",i);
    }
    else
    {
        b=(a/2);
        i=pow(2,b);
        printf("%d",i);
    }

    return 0;
}
