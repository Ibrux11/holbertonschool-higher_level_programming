# task_02_verboselist.py

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        length_before = len(self)
        super().extend(iterable)
        length_after = len(self)
        items_added = length_after - length_before
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)

# main_02_verboselist.py

#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)       # Outputs: Added [4] to the list.
vl.extend([5, 6])  # Outputs: Extended the list with [2] items.
vl.remove(2)       # Outputs: Removed [2] from the list.
vl.pop()           # Outputs: Popped [6] from the list.
vl.pop(0)          # Outputs: Popped [1] from the list.