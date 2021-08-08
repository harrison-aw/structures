from pytest import fixture

from linked_list import LinkedList


class TestLinkedList:
    def test_repr(self, values):
        list_ = LinkedList(values)
        assert repr(eval(repr(list_))) == repr(list_)

    @fixture
    def values(self):
        return [1, 2, 3, 4]
