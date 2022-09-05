/**

    Title: Factorial of a number

    >> Write down a program that will find factorial of a given number

    ## Test ##

    input: 4 output: 24

    input: 5 output: 120

**/
#include <stdio.h>

int recur_factorial(int n);
int loop_factorial(int n);

int main (){
    int f = loop_factorial(4);
    int r = recur_factorial(4);
    printf("Loop:%d, recursion:%d", f, r);
}

int recur_factorial(int n){
    if (n == 0 || n == 1){
        return 1;
    }
    else{
         return n*recur_factorial(n-1);
    }
}

int loop_factorial(int n){
    int fact = 1;
    int i;

    for (i=1; i<=n; i++ ){
            fact = fact*i;
        }
         return fact;
}
