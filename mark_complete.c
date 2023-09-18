#include "main.h"

void mark_completed(struct task list[], int count, int task_index) {


	if (task_index >= 1 && task_index <= count) {
		list[task_index - 1].complete = 1;
		printf("Task marked as complete!\n");
	} else {
		printf("Invalid task index. Please entre a valid task number.\n");
	}
}
