#include <stdio.h>

#ifndef DEBUG_H
#define DEBUG_H

/* debug strings, numbers, string and number, 
 * and two strings. not sure if I'll use all of these?
 */
#define DEBUGS(s) fprintf(stderr, "DEBUG: %s\n", s)
#define DEBUGN(s) fprintf(stderr, "DEBUG: %d\n", s)
#define DEBUGSN(d, s) fprintf(stderr, "DEBUG: %s: %d\n", d, s)
#define DEBUGSS(d, s) fprintf(stderr, "DEBUG: %s: %s\n", d, s)

#endif
