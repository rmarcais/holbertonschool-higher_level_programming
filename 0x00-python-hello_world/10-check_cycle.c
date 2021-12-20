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
	listint_t *tmp = list, *tmp2 = list;


	while (tmp != NULL && tmp2 != NULL)
	{
		tmp = tmp->next->next;
		tmp2 = tmp2->next;
		if (tmp == tmp2)
			return (1);
	}
	return (0);
}
