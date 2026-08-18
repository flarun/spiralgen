#ifndef SPIRALGEN_H
#define SPIRALGEN_H

typedef struct
{
  int width;
  int height;
} TerminalSize;

// Function prototypes
TerminalSize get_terminal_size();
void render_spiral(TerminalSize term_size, int frame);
void sleep_ms(int milliseconds);

#endif // SPIRALGEN_H