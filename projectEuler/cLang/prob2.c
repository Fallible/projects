#include <stdio.h>
//fibinochi with some other rules

int isOdd(int currentValue){
    return(currentValue % 2);
    //returns 0 if even.
}

int main()
{
    int i = 0;
    int fibPrev = 1;
    int fibNext = 2;
    int temp = 0;
    int sum = 0;
    for(i; fibNext <= 4000000; i++)
    {
        temp = fibPrev;
        fibPrev = fibNext;
        fibNext = fibNext + temp;
        if(!isOdd(fibNext))
        {
            sum = sum + fibNext;
        }
    }
    printf("%i", sum);

}
