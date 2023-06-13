from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data == []

    def __str__(self):
        str_items = ""
        for i in range(len(self._data)):
            value = self._data[i]
            str_items += str(value)
            if i + 1 < len(self._data):
                str_items += ", "

        return "Queue(" + str_items + ")"

    def enqueue(self, value):
        return self._data.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Fila vazia, não é possível remover elementos")
        return self._data.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]


if __name__ == "__main__":
    queue = Queue()
    elements = [1, 2, 3, 4, 5]

    for elem in elements:
        queue.enqueue(elem)

    print(queue)
    # queue.dequeue()
    print(queue.search(50))
