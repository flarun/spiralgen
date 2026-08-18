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
  (void)argc;
  (void)argv;

  int frame = 0;

  // Endless loop for our terminal screensaver
  while (1)
  {
    TerminalSize term_size = get_terminal_size();

    // Clear the screen and reset cursor to top-left
    printf("\033[2J\033[H");

    // Render the spiral frame using the frame counter to animate it
    render_spiral(term_size, frame);

    // Wait 50 milliseconds (~20 frames per second) so it doesn't flicker wildly
    sleep_ms(50);

    frame++;
  }

  return 0;
}