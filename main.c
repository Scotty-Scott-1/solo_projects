#include "main.h"

#define read_spec "%[^\n]"

int main(void) {

struct task task_list[1024];

int task_count;
int choice;
char description[1024];
int task_index;

while(1) {

	printf("\nTo-Do List Menu\n");
	printf("1. Add Task\n");
	printf("2. View Tasks\n");
	printf("3. Mark tasks as Complete\n");
	printf("4. Exit\n");
	printf("5. Enter your choice: ");
	scanf("%d", &choice);

	getchar();

	switch (choice) {
	case 1:
		printf("Enter task desciption: ");
		scanf(read_spec, description);
		add_task(task_list, &task_count, description);
		break;
	case 2:
		view_task(task_list, task_count);
		break;
	case 3:
		view_task(task_list, task_count);
		printf("Enter the tasl number to mark as complete: ");
		scanf("%d", &task_index);
		mark_completed(task_list, task_count, task_index );
		break;
	case 4:
		printf("Exiting the program\n");
		exit (0);

	default:
		printf("Invalid choice. Please try again\n");
		break;

	}

}
	return (0);
}
