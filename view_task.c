#include "main.h"

void view_task(struct task list[], int count) {

	int i = 0;

	if(count == 0) {
		printf("The task list in empty.\n");
	} else {
		printf("Task list:\n");
		for(i = 0; i < count; i++) {
			printf("%d. %s\n", i + 1, list[i].description);
			if (list[i].complete) {
				printf("(Complete)");
			}
		}
	}


}
