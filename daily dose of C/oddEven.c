#include <stdio.h>


int main(void){
    int a;
    printf("Enter integer: ");
    scanf("%d", &a);
    if (a % 2 == 0){
        printf("Even");
    }
    else if (a % 3 == 0)
    {
        printf("Odd");
    }
    else
    {
        printf("Neither odd nor even");
    }
    return 0;
}