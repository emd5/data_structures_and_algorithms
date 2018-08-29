from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def load_dog():
    dog_queue = AnimalShelter()
    dog_queue.enqueue('dog')
    return dog_queue.front


@pytest.fixture()
def load_cats():
    cat_queue = AnimalShelter()
    cat_queue.enqueue('cat')
    return cat_queue.front


def test_animal_shelter_class_exist():
    """Test animal shelter class exist. """
    assert AnimalShelter





