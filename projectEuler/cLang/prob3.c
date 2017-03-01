#include <stdio.h>
//Find Prime Factors




int main()
{
    long currentValue = 600851475143;
    int i;
    for(i = 3; i < currentValue / 2; i = i + 2)
    {
        if( currentValue % i == 0)
        {
            currentValue = currentValue / i;
        }
    }
    printf("%i", i); 
}	
