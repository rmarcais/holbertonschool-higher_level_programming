#include "lists.h"
/**
 * checkpin - checks if a singly linked list is a palindrome
 * @left: double pointer
 * @right: pointer to head of list
 * Return: 1 or 0
 */
int checkpin(listint_t **left, listint_t *right)
{
	int a;
	if (right == NULL)
		return (1);
	a = checkpin(left, right->next);
	if (a == 0)
		return (0);
	if ((*left)->n != right->n)
		a = 0;
	*left = (*left)->next;
	return (a);
}
/**
 * is_palindrome - returns 1 if it's a palindrome or 0 if not
 * @head: pointer to head of list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	return checkpin(head, *head);
}
