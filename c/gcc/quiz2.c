#include <stdio.h>
#include "libcheckeod.h"

void main(){
    int x;
    printf("Input Number:");
    scanf("%d",&x);

    while (x!=0)
    {
        checkeod(x);
        break;
    }
    printf("Program Exit\n");

}