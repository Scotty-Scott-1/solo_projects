#include "main.h"

void add_task(struct task list[], int *count,const char *description) {

	if(*count < 100) {

		strcpy(list[*count].description, description);
		list[*count].complete = 0;
		(*count)++;
		printf("Task added successfully!\n");
	} else {

		printf("The task list is full. You can't add more tasks.\n");

	}
}
