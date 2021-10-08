class LLNode:
    prev: "LLNode" = None
    value: any = None


class LinkedList:
    def __init__(self):
        self._tail = None

    def add(self, value: any) -> None:
        nnode = LLNode()
        nnode.value = value
        if self._tail is None:
            self._tail = nnode
        else:
            nnode.prev = self._tail
            self._tail = nnode

    def peek(self) -> any:
        if self._tail is None:
            return None
        else:
            return self._tail.value

    def remove(self, value: any) -> None:
        raise NotImplementedError("You need to write this code.")
