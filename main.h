#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct task {
char title[1024];
char description[1024];
int complete;
};

void add_task(struct task list[], int *count, const char *description);
void view_task(struct task list[], int count);
void mark_completed(struct task list[], int task_count, int task_index);




#endif /* MAIN_H */
