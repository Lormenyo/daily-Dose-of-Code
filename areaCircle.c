#include <stdio.h>


float areaCirc(int radius); //without this declation, you will get a warning(implicit declaration of function)

int main(){
   float circarea = areaCirc(3);
   printf("Area of the circle: %f", circarea);
}

float areaCirc(int radius){
    float area = 3.142 * radius * radius;
    return area;
}