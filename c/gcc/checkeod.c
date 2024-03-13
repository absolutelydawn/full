#include <stdio.h>


int checkeod(int x){
    if(x%2 == 0)
        printf("%d is even\n", x);
    else
        printf("%d is odd\n", x);
}