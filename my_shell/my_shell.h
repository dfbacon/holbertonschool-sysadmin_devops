#ifndef MY_SHELL
#define MY_SHELL
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>

/* string functions */
int _putchar(char c);
int _printstring(char *string);
int _strlen(char *s);
int _cstrlen(char **s);
char *_strncpy(char *dest, char *src, int n);
char *_strcat(char *dest, char *src);
char *_strdup(char *str);
int _strcmp(char *s1, const char *s2);
char *readline(int fd);
int _atoi(char *s);
/* memory functions */
char *_memset(char *s, char b, unsigned int n);
void _free(char **c);
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size);
/* environment functions */
char *_getenv(const char *name);
void _fork(char **c, char **env);
int seg_num(char *line, char sep);
int seg_strlen(char *line, char sep);
char **_strtok(char *line, char sep);
/* builtin functions */
int _bstrcomp(char *s1, char *s2);
void _exit(char **command, char **env);

#endif /* #ifndef MY_SHELL */
