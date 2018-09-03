from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    """Instantiate an empty queue class. """
    return Queue()


@pytest.fixture()
def small_queue():
    """Instantiate a queue and add some values. """
    queue = Queue([1, 2, 3, 4, 5])
    return queue


def test_queue_exists():
    """Test if queue exist. """
    assert Queue


def test_create_instance_of_queue():
    """Test and instance of a queue"""
    queue = Queue()
    assert isinstance(queue, Queue)


def test_default_property_front(empty_queue):
    """Test empty queue front is none. """
    assert empty_queue.front is None


def test_default_property_queue_length(empty_queue):
    """Tests the empty queue is equal to 0. """
    assert empty_queue._length == 0


def test_empty_enqueue_successful(empty_queue):
    """Test enqueue on an empty queue where value is found. """
    assert len(empty_queue) == 0
    empty_queue.enqueue(25)
    assert len(empty_queue) == 1


def test_empty_queue_with_dequeue_successful(empty_queue):
    """Test dequeue when queue is empty. """
    empty_queue.dequeue()
    assert len(empty_queue) == 0


def test_enqueue_with_small_queue(small_queue):
    """Test queue by adding one, length increment by 1. """
    assert len(small_queue) == 5
    small_queue.enqueue(90)
    assert len(small_queue) == 6


def test_peek_with_empty_queue(empty_queue):
    """Test peek method when queue is empty. """
    assert empty_queue.peek() is None


def test_peek_with_small_queue(small_queue):
    """Test peek method when there are nodes in the queue. """
    assert small_queue.peek() == small_queue.front



