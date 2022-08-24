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
	listint_t *num, *node, *hd;

	hd = *head;
	num = malloc(sizeof(listint_t));
	if (num == NULL)
		return (NULL);
	num->n = number;

	while (hd != NULL)
	{
		if (hd->n > number)
			break;
		node = hd;
		hd = hd->next;
	}
	if (*head == NULL)
	{
		num->next = NULL;
		*head = num;
	}
	else
	{
		num->next = hd;
		if (hd == *head)
			*head = num;
		else
			node->next = num;
	}
	
	return(num);
}
