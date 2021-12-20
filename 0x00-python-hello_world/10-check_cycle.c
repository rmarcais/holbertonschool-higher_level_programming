#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list, *tmp2;
	int i, j = 1;


	while (tmp != NULL)
	{
		tmp = tmp->next;
		tmp2 = list;
		for (i = 1; i <= j; i++, tmp2 = tmp2->next)
			if (tmp == tmp2)
				return (1);
		j++;
	}
	return (0);
}
