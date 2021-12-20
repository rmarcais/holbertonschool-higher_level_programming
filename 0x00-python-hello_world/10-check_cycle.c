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
	listint_t *tmp;

	if (list == NULL || list->next==NULL)
		return (0);
	tmp = list;
	while (tmp)
	{
		tmp = tmp->next->next;
		if (tmp == list)
			return (1);
		list = list->next;
	}
	return (0);
}
