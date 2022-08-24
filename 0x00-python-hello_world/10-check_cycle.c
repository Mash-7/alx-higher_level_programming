#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Te list to check
 *
 * Return: if there is a cycle, 1.
 * Else, 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	i = list;
	j = list;

	if (list == NULL || list->next == NULL)
		return (0);

	i = list->next;
	j = list->next->next;

	while (i && j && j->next)
	{
		if (i == j)
			return (1);
		i = i->next;
		j = j->next->next;
	}
	return (0);
}
