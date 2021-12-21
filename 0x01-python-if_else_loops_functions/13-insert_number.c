#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *tmp = *head;

	new_node = malloc(sizeof(listint_t *));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (tmp == NULL || number <= tmp->n)
	{
		*head = new_node;
		new_node->next = tmp;
		return (new_node);
	}
	while (tmp && tmp->next && number > tmp->next->n)
		tmp = tmp->next;
	new_node->next = tmp->next;
	tmp->next = new_node;
	return (new_node);
}
