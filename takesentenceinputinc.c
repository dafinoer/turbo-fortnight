"""
hacker rank

https://www.hackerrank.com/challenges/playing-with-characters/problem
"""

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{ char ch,s[50],sen[500];
 scanf("%c",&ch);
 scanf("%s",s);
 scanf(" %[^\n]s",sen);
 
 printf("%c\n%s\n",ch,s);
 printf("%s",sen);   
    return 0;
}
