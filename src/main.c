#include <stdio.h>
#include <stdlib.h>
#include "spiralgen.h"

// Include Windows headers if compiling on Windows, otherwise include POSIX headers
#ifdef _WIN32
#include <windows.h>
#else
#include <sys/ioctl.h>
#include <unistd.h>
#endif

TerminalSize get_terminal_size()
{
  TerminalSize ts = {80, 24}; // Default fallback

#ifdef _WIN32
  // Windows API way to get terminal size
  CONSOLE_SCREEN_BUFFER_INFO csbi;
  if (GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbi))
  {
    ts.width = csbi.srWindow.Right - csbi.srWindow.Left + 1;
    ts.height = csbi.srWindow.Bottom - csbi.srWindow.Top + 1;
  }
#else
  // Linux/macOS way to get terminal size
  struct winsize w;
  if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) != -1)
  {
    ts.width = w.ws_col;
    ts.height = w.ws_row;
  }
#endif

  return ts;
}

int main(int argc, char *argv[])
{
  // We can parse argc/argv here later for custom colors or speeds
  (void)argc;
  (void)argv;

  TerminalSize term_size = get_terminal_size();

  // Clear the screen using ANSI escape codes
  printf("\033[2J\033[H");

  printf("Terminal size detected: %d columns x %d rows\n", term_size.width, term_size.height);

  // Call the rendering logic (make sure render.c is set up!)
  render_spiral(term_size);

  return 0;
}