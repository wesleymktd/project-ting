from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    file_data1 = {"nome_do_arquivo": "aquivo1.txt", "qtd_linhas": 3}
    file_data2 = {"nome_do_arquivo": "aquivo2.txt", "qtd_linhas": 10}
    file_data3 = {"nome_do_arquivo": "aquivo3.txt", "qtd_linhas": 6}
    file_data4 = {"nome_do_arquivo": "aquivo4.txt", "qtd_linhas": 1}

    priority_queue.enqueue(file_data1)
    priority_queue.enqueue(file_data2)
    priority_queue.enqueue(file_data3)
    priority_queue.enqueue(file_data4)

    assert len(priority_queue) == 4
    assert priority_queue.search(1) == file_data4

    item_dequeue = priority_queue.dequeue()

    assert len(priority_queue) == 3
    assert item_dequeue == file_data1

    with pytest.raises(IndexError):
        priority_queue.search(20)
