#include <stdio.h>

//add up the natural numbers below 1000 that are multiples of 3 or 5

//function to know if input number is a factor of 3 or 5
int isFactor(int currentNumber);

//

main(){
    int sum = 0;
    int i = 0;
    for(i; i < 1000; i++)
    {
        if(isFactor)
        {
            sum = sum + i;
        }
    }
    printf("%i\n", sum);
}

int isFactor(int currentNumber){
    if(currentNumber % 5 == 0 || currentNumber % 3 == 0)
    {
        return currentNumber;
    }
    else
    {
        return 0;
    }
}
