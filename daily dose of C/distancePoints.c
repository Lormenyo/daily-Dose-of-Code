/**

    Title: Find the distance between two points of a straight line

    >> Write down a program that will take two points of a straight line as input

    >> and will calculate the distance between them

    ## Test ##

    input: x1=1 y1=2 x2=3 y2=3  output: 2.236

    input: x1=2 y1=2 x2=5 y2=5  output: 4.243  [distance = sqrt of (x2-x1)^2 + (y2-y1)^2]

**/

#include <stdio.h>
#include <math.h>

void distance(int x1, int y1, int x2, int y2);

int main(){

    distance(1 ,2, 3, 3 );

    return 0;
}

void distance(int x1, int y1, int x2, int y2){
    float d = sqrt( pow((x2-x1),2) + pow((y2-y1),2));
    printf("The distance between (%d, %d) and (%d, %d) is %f \n",  x1,y1,x2,y2,d);
}