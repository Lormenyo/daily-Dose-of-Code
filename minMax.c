#include <stdio.h>


void minMax2(int a, int b);
void minMax3(int a, int b, int c);

int main(void){
    minMax2(5,2);
    minMax3(10,4,2);
}
// Write a program that takes two numbers as input and outputs the min and max using ternary operators
void minMax2(int a, int b){
    int min;
    int max;
    min = a < b ? a : b;
    max = a > b ? a : b;
    printf("Min:%d , Max:%d", min, max);
}

// Write the program for three inputs as well
void minMax3(int a, int b, int c){
    int min;
    int max;
    min = (a < b) && (a < c) ? a : (b < a) && (b < c) ? b : c;
    max = (a > b) && (a > c) ? a : (b > a) && (b > c) ? b : c;
    printf("\nMin:%d , Max:%d", min, max);
}