#include <stdio.h>
#include <unistd.h>


int infinite_while(void);

/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0
 */
int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (!pid)
			return (0);
		printf("Zombie process created, PID: %d\n", pid);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - Infinite while loop
 *
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
