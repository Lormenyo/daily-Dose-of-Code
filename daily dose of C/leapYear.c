/**

    Title: Checking a given year is a leap year or not

    >> Write down a program that will take a year as input and will check the year

    >> is a leap year or not

    ## Test ##

    input: 2020  output: true

    input: 2021  output: false

**/
#include <stdio.h>
#include <stdbool.h>

void isLeapYear(int year);

int main(){
    isLeapYear(2020);
   isLeapYear(2019);
    return 0;
}

void isLeapYear(int year){
    // First: check if divisible by 4, if no, it is not a leap year, if yes do second check
    if (year % 4 == 0){
         // Second: check if divisible by 100, if yes, it is not a leap year. If no, it is a leap year
        if (year % 100 != 0){
            printf("%d is a Leap year\n", year);
        }
    }
    else{
        printf("%d is not a Leap year\n", year);
    }
   
}