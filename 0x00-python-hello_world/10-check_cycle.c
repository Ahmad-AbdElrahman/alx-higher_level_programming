#include <stdio.h>
#include "lists.h"
int check_cycle(listint_t *list)
{
	listint_t *sstep, *dstep;
	sstep = list;
	dstep = list;
	while (sstep && dstep && dstep->next)
	{
		sstep = sstep->next;
		dstep = dstep->next->next;
		if (sstep == dstep)
			return 1;
	}
	return 0;
		
}
