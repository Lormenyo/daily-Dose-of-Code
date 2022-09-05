#include <stdio.h>

int main(void) {
   int n1, n2;
   printf("Enter interger one: ");
   scanf("%d", &n1);
   printf("Enter interger two: ");
   scanf("%d", &n2);

   int add = n1 + n2;
   int sub = n1 - n2;
   int mul = n1 * n2;
   int div = n1 / n2;
   int mod = n1 % n2;

   printf("add:%d, sub:%d, div:%d, mul:%d, mod:%d", add, sub, div, mul, mod);

   return 0;
}