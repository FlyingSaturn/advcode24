#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	FILE *file = fopen("../inputs/input_day1p1.txt", "r");
	if (file == NULL)
	{
		printf("Could not read file. Terminating the program...");
		return 1;
	}
	int arr[2];
	int *first = (int *) calloc(1, sizeof(int));
	if (first == NULL)
	{
		printf("Sorry");
		fclose(file);
		return 2;
	}
	int *second = (int *) calloc(1, sizeof(int));
	if (second == NULL)
	{
		printf("Sorry.");
		free(first);
		fclose(file);
		return 3;
	}
	int i = 0;
	while(fread(arr, sizeof(int), 2, file) == 2)
	{
		i++;
		first=realloc(first, i * sizeof(int));
		second=realloc(second, i * sizeof(int));
		if (first == NULL || second == NULL)
		{
			printf("Sorry.");
                	free(first);
                	free(second);
			fclose(file);
			return 4;
		}
		first[i-1] = arr[0];
		second[i-1]= arr[1];	
		printf("%d %d\n", first[i-1], second[i-1]);
	}
	fclose(file);
	free(first);
	free(second);
}
