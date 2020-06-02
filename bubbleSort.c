// sort the values of three variables in Ascending order

// Bubble sort algorithm was used

#include <stdio.h>

void bubble(int arr[], int arr_size);

int main(){

    int arr[] = {9, 2, 3, 7, 4, 1};

   bubble(arr, 6);

    return 0;
}

void bubble(int arr[], int arr_size){

    int i,j;

    for (i=0; i<arr_size; i++){
        for (j=0; j< (arr_size-i-1); j++){

            // compare current element with all the elements
            if (arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }

   for (i=0; i<arr_size; i++){
       printf("%d, ", arr[i]);
   }

}