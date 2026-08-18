#include <stdio.h>
#include <math.h>
#include "spiralgen.h"

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

void render_spiral(TerminalSize term_size, int frame)
{
  int width = term_size.width;
  int height = term_size.height;

  if (width <= 0 || height <= 0)
    return;

  // Center point of the terminal screen
  double center_x = width / 2.0;

  // Width / amplitude of the helix twist
  double amplitude = width / 6.0;
  if (amplitude < 5)
    amplitude = 5;

  // Loop through each row of the terminal
  for (int y = 0; y < height; y++)
  {
    // Calculate the sine offset for Strand 1 based on row and frame time
    // This creates a wave that moves vertically as 'frame' increases
    double freq = 0.15; // Controls how tightly wound the helix is
    double phase = frame * 0.2;

    double offset1 = sin(y * freq + phase) * amplitude;
    double offset2 = sin(y * freq + phase + M_PI) * amplitude; // Offset by 180 degrees (PI) for the second strand

    // Determine absolute column positions for both strands
    int pos1 = (int)(center_x + offset1);
    int pos2 = (int)(center_x + offset2);

    // Ensure positions stay within terminal bounds
    if (pos1 < 0)
      pos1 = 0;
    if (pos1 >= width)
      pos1 = width - 1;
    if (pos2 < 0)
      pos2 = 0;
    if (pos2 >= width)
      pos2 = width - 1;

    // To make it look clean, we can construct the line character by character or print efficiently.
    // Let's build a small line buffer or draw left-to-right.
    for (int x = 0; x < width; x++)
    {
      if (x == pos1)
      {
        // First strand (Cyan)
        printf("\033[36m0\033[0m");
      }
      else if (x == pos2)
      {
        // Second strand (Magenta/Pink to contrast like DNA base pairs)
        printf("\033[35mX\033[0m");
      }
      else
      {
        // Print connector or empty space between/around them
        // Optional: add a subtle backbone/ladder rung if they cross paths
        if ((pos1 < pos2 && x > pos1 && x < pos2) || (pos2 < pos1 && x > pos2 && x < pos1))
        {
          // Inside the helix core - maybe print a faint dot or leave blank
          if (x == (int)((pos1 + pos2) / 2.0) && y % 2 == 0)
          {
            printf("\033[90m-\033[0m"); // Faint gray connector rung
          }
          else
          {
            printf(" ");
          }
        }
        else
        {
          printf(" ");
        }
      }
    }
    printf("\n");
  }
}