#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>
#include "spiralgen.h"

void printFirstHalf()
{
  printf("printinf first half\n");
  int distance = diameter;
  printf("%d\n", distance);
}

void printSecondHalf()
{
  printf("printing second half\n");
}

void printSpiral()
{
  printFirstHalf();
  printSecondHalf();
}

int main(int argc, char *argv[])
{
  scanf("%d", &diameter);
  if (!(diameter % 2 == 0))
  {
    printf("You can only enter even values!\n");
    exit(0);
  }
  int radius = diameter / 2;
  printSpiral();
  return 0;
}

/*

  for (int distance; distance == 0; distance--) // loop over the distance
  {
    if (distance % 2 == 0) // working with only even distances
    {
      int fullSection = (int)sqrt(pow((double)radius, 2.0) - pow((double)distance, 2.0)); // width of actual circle in a line at a certain distance
      int emptySection = diameter - fullSection;
      int halfEmptySection = emptySection / 2;
      for (int i = 0; i < halfEmptySection; i++) // first half empty section
      {
        printf(" ");
      }
      for (int i = 0; i < fullSection; i++) // full section
      {
        printf("0");
      }
      for (int i = 0; i < halfEmptySection; i++) // second half empty section
      {
        printf(" ");
      }
      printf("\n");
    }
  }

  */