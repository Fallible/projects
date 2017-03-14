#include <stdio.h>
//largest palindrome made from the product of two 3-digit numbers

/*
 *I want to build this as multiple functions.  One should check if my current
 * number is a palindrome.  Another should run a nested for loop to generate
 * all products of 2 three digit numbers.
 *
 */

int checkPal(int number)
{
    int i;
    int thousands, hundreds, tens, ones;
    int segmentedNumber[4];
    for(i = 0; i < 4; i++){
        segmentedNumber = number %
    }
}


int runLoop()
{
    int i = 999;
    int j = 999;
    int currentHighest = 0;
    for(i; i > 99; i--)
    {
        for(j; j > 99; j--)
	{
            if(i * j > currentHighest) currentHighest = i * j;           
	}
    }
    return currentHighest;
}

int main()
{
    int 

}


