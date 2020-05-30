// Write a program that will swap the value of two variable

#include <stdio.h>

void swapVariable(int n1, int n2);

int main(){
    swapVariable(9,3);
}


void swapVariable(int n1, int n2){
    int *a, *b;

    a = &n1; // pointer a points to variable n1(memory address)
    b = &n2; // pointer b points to variable n2(meemory address)

    int temp = *a;  // the value that pointer a points to is assigned to a temporary variable 
    n1 = n2;  // the value of n2 is assigned to n1, at this point they all have the same values
    n2 = temp;  // the value of temp variable is assigned to n2

    printf("n1:%d, n2:%d", n1, n2);
}