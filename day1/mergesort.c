#include <stdio.h>

int main(void)
{
	// Copied at first to a and b, then merging them
	int a[] = {1, 3, 5, 7};
	int b[] = {4, 4, 6, 8};
	int i=0, j=0;
	int c[8];
	// Length
	int a_i = 4;
	int b_j = 4;

	int k = 0;
	// Main stuff
	while (i < a_i && j < b_j)
	{
		if (a[i] < b[j])
			c[k++] = a[i++];
		else
			c[k++] = b[j++];
	
	}
	// Remaining stuff
	while (i < a_i)
		c[k++] = a[i++];
	while (j < b_j)
		c[k++] = b[j++];
	
	for (i = 0; i < k; i++)
		printf("%d\n", c[i]);
}
