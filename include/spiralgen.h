#ifndef SPIRALGEN_H
#define SPIRALGEN_H

// A struct to hold our terminal window dimensions
typedef struct
{
  int width;
  int height;
} TerminalSize;

// Function prototypes
TerminalSize get_terminal_size();
void render_spiral(TerminalSize term_size);

#endif // SPIRALGEN_H