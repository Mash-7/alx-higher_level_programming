#include "lists.h"
#include <stddef.h>

/**
 * insert_node  Inserts a number into a sorted singly linked list.
 * @head: Pointer to the head of the linked list.
 * @number: The number to be inserted.
 *
 * Return: Address of the new node.
 * On failure, NULL.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *num, *node = *head;

	num = malloc(sizeof(listint_t));
	if (num == NULL)
		return (NULL);
	num->n = number;
	num->next = node->next;
	node->next = num;

	if (node == NULL || node->n >= number)
	{
		num->next = node;
		*head = num;
		return (num);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	return(num);
}
