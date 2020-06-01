// Return the second largest value of three numbers
#include <stdio.h>

int secondLargest(int a, int b, int c);

int main(void){
    int m = secondLargest(9,10,1);
    printf("second largest number = %d", m);
    return 0;
}

int secondLargest(int a, int b, int c){
    int middleNum = (a > c) & (a < b) || (a < c) & (a > b) ? a: 
                    (b > a) & (b < c) ||(b < a) & (b > c) ? b : c;
    return middleNum;
}
