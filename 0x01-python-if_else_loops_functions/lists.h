#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
* struct listint_s - function that list singly linked list
* @n: integer
* @next: points to the next node
*
* Description: node structure of singly linked list
*
*/
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
listint_t *insert_node(listint_t **head, int number);

#endif
