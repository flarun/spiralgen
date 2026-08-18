#include <stdio.h>
#include <math.h>
#include "spiralgen.h"

void render_spiral(TerminalSize term_size)
{
  // Use the terminal height to define our maximum radius so it fits the screen
  int radius = term_size.height / 2;

  // Prevent rendering if the terminal is impossibly small
  if (radius <= 0)
    return;

  // Loop from the top of the circle down to the bottom
  for (int y = radius; y >= -radius; y--)
  {

    // This is the core math from your original python/c scripts:
    // width = sqrt(radius^2 - distance^2)
    double width_calc = sqrt(pow(radius, 2) - pow(y, 2));
    int solid_section = (int)width_calc;

    // Terminal characters are usually twice as tall as they are wide.
    // We multiply the width by 2 to make it a true circle instead of a squished oval.
    solid_section *= 2;

    // Calculate empty space to center the shape
    int empty_section = term_size.width - solid_section;
    int half_empty = empty_section / 2;

    // 1. Print the left padding (empty space)
    for (int i = 0; i < half_empty; i++)
    {
      printf(" ");
    }

    // 2. Print the solid section with an ANSI color code (Cyan: \033[36m)
    printf("\033[36m");
    for (int i = 0; i < solid_section; i++)
    {
      printf("0"); // Using the "0" from your original project
    }

    // 3. Reset the color (\033[0m) and move to the next line
    printf("\033[0m\n");
  }
}