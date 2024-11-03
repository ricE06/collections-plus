# unit tests for the Linked List class

from src.collections_plus import LinkedList
import pytest

class TestLinkedList():

    @pytest.fixture
    def ll_gen(self):
        self.ll_empty = LinkedList()
        self.ll_singular = LinkedList(0)
        self.ll_data_1 = LinkedList(1, 2, 3)
        self.ll_data_2 = LinkedList(4, 5, 6, 7)

    @pytest.fixture
    def ll_big(self):
        self.ll_data_large = LinkedList(*(range(10_000_000)))

    def test_repr(self, ll_gen):
        assert str(self.ll_empty) == "LinkedList()"
        assert str(self.ll_singular) == "LinkedList(0)"
        assert str(self.ll_data_1) == "LinkedList(1, 2, 3)"
        assert str(self.ll_data_2) == "LinkedList(4, 5, 6, 7)"

    def test_get_simple(self, ll_gen):
        assert self.ll_singular[0] == 0
        assert self.ll_data_1[0] == 1
        assert self.ll_data_1[2] == 3
        assert self.ll_data_2[1] == 5

    def test_get_negative(self, ll_gen):
        assert self.ll_singular[-1] == 0
        assert self.ll_data_2[-3] == 5
        assert self.ll_data_2[-4] == 4

    def test_get_errors(self, ll_gen):
        with pytest.raises(IndexError):
            dummy = self.ll_data_1[10]
        with pytest.raises(IndexError):
            dummy = self.ll_data_1[-4]
        with pytest.raises(IndexError):
            dummy = self.ll_empty[0]
        with pytest.raises(TypeError):
            dummy = self.ll_data_2["not an integer"]

    def test_set_simple(self, ll_gen):
        self.ll_data_1[1] = 4
        assert str(self.ll_data_1) == "LinkedList(1, 4, 3)"
        self.ll_data_1[2] = 10
        assert str(self.ll_data_1) == "LinkedList(1, 4, 10)"
        self.ll_data_1[-3] = "first"
        assert str(self.ll_data_1) == "LinkedList(first, 4, 10)"

    def test_set_errors(self, ll_gen):
        with pytest.raises(IndexError):
            self.ll_data_1[10] = 10
        with pytest.raises(IndexError):
            self.ll_data_1[-10] = 10
        with pytest.raises(TypeError):
            self.ll_data_1["a"] = "not an integer"

    def test_del_simple(self, ll_gen):
        del self.ll_data_2[0]
        assert str(self.ll_data_2) == "LinkedList(5, 6, 7)"
        del self.ll_data_2[-2]
        assert str(self.ll_data_2) == "LinkedList(5, 7)"
        del self.ll_singular[0]
        assert str(self.ll_singular) == "LinkedList()"

    def test_del_errors(self, ll_gen):
        with pytest.raises(IndexError):
            del self.ll_data_1[10]
        with pytest.raises(IndexError):
            del self.ll_data_1[-10]
        with pytest.raises(TypeError):
            del self.ll_data_1[1.5]

    def test_len_simple(self, ll_gen):
        assert len(self.ll_empty) == 0
        assert len(self.ll_singular) == 1
        assert len(self.ll_data_1) == 3
        assert len(self.ll_data_2) == 4

    def test_iter(self, ll_gen):
        for val in self.ll_data_1:
            assert val == 1
            break
        values_1 = list(self.ll_data_1)
        values_2 = list(self.ll_data_2)
        values_empty = list(self.ll_empty)
        assert values_1 == [1, 2, 3]
        assert values_2 == [4, 5, 6, 7]
        assert values_empty == []

    def test_equality(self, ll_gen):
        another = LinkedList(1, 2, 3)
        assert (another == self.ll_data_1) == True
        assert (another != self.ll_data_1) == False
        assert (another == self.ll_data_2) == False
        other_empty = LinkedList()
        assert (other_empty == self.ll_empty) == True

    def test_comparison(self, ll_gen):
        another = LinkedList(1, 2, 4)
        assert (another > self.ll_data_1) == True
        assert (another < self.ll_data_1) == False
        shorter = LinkedList(1, 10)
        assert (shorter > self.ll_data_1) == True
        same = LinkedList(1, 2, 3)
        assert (same >= self.ll_data_1) == True
        assert (same <= self.ll_data_1) == True
        assert (same > self.ll_data_1) == False
        same_but_longer = LinkedList(1, 2, 3, -4)
        assert (same_but_longer > self.ll_data_1) == True

    def test_comparison_errors(self, ll_gen):
        with pytest.raises(TypeError):
            dummy = self.ll_data_2 == [4, 5, 6, 7]
        with pytest.raises(TypeError):
            dummy = self.ll_data_2 >= 4

    def test_copy(self, ll_gen):
        copied = self.ll_data_2.copy()
        assert copied == self.ll_data_2
        copied[0] = 400
        assert copied != self.ll_data_2

    def test_pop(self, ll_gen):
        popped = self.ll_data_1.pop()
        assert popped == 1
        assert str(self.ll_data_1) == "LinkedList(2, 3)"
        popped = self.ll_data_1.pop()
        assert popped == 2
        assert str(self.ll_data_1) == "LinkedList(3)"
        assert len(self.ll_data_1) == 1
        popped = self.ll_data_2.pop(2)
        assert popped == 6
        assert str(self.ll_data_2) == "LinkedList(4, 5, 7)"
        popped = self.ll_data_2.pop(-2)
        assert popped == 5
        assert str(self.ll_data_2) == "LinkedList(4, 7)"
        assert len(self.ll_data_2) == 2

    def test_append(self, ll_gen):
        self.ll_data_1.append(4)
        assert list(self.ll_data_1) == [1, 2, 3, 4]
        self.ll_data_1.append("10")
        assert list(self.ll_data_1) == [1, 2, 3, 4, "10"]
        assert len(self.ll_data_1) == 5
        self.ll_empty.append("foo")
        assert list(self.ll_empty) == ["foo"]
        assert len(self.ll_empty) == 1

    def test_extend(self, ll_gen):
        orig_2 = self.ll_data_2.copy()
        self.ll_data_1.extend(self.ll_data_2)
        assert orig_2 == self.ll_data_2
        assert list(self.ll_data_1) == [1, 2, 3, 4, 5, 6, 7]
        assert len(self.ll_data_1) == 7
        self.ll_data_1.extend(self.ll_empty)
        assert list(self.ll_data_1) == [1, 2, 3, 4, 5, 6, 7]
        assert len(self.ll_data_1) == 7
        self.ll_empty.extend(self.ll_data_1)
        assert list(self.ll_empty) == [1, 2, 3, 4, 5, 6, 7]
        assert len(self.ll_empty) == 7
        self.ll_singular.extend(self.ll_singular)
        assert list(self.ll_singular) == [0, 0]
        assert len(self.ll_singular) == 2

    def test_count(self):
        dupe = LinkedList(1, 1, 3, 1, 2, 2)
        assert dupe.count(1) == 3
        assert dupe.count(2) == 2
        assert dupe.count(3) == 1
        assert dupe.count(4) == 0

    def test_indexing(self, ll_gen):
        assert self.ll_data_1.index(2) == 1
        assert self.ll_data_1.index(3) == 2
        with pytest.raises(ValueError):
            dummy = self.ll_data_1.index(0)

    def test_insertion(self, ll_gen):
        self.ll_data_1.insert(0, 20)
        assert list(self.ll_data_1) == [20, 1, 2, 3]
        assert len(self.ll_data_1) == 4
        with pytest.raises(IndexError):
            dummy = self.ll_data_1.insert(5, 10)

    def test_removal(self, ll_gen):
        self.ll_data_2.remove(6)
        assert list(self.ll_data_2) == [4, 5, 7]
        assert len(self.ll_data_2) == 3
        with pytest.raises(ValueError):
            self.ll_data_2.remove(9)
        with pytest.raises(ValueError):
            self.ll_empty.remove(9)

    def test_concat(self, ll_gen):
        old_1 = self.ll_data_1.copy()
        old_2 = self.ll_data_2.copy()
        new = self.ll_data_1 + self.ll_data_2
        assert list(new) == [1, 2, 3, 4, 5, 6, 7]
        assert len(new) == 7
        new_2 = self.ll_data_2 + self.ll_data_1
        assert list(new_2) == [4, 5, 6, 7, 1, 2, 3]
        assert len(new_2) == 7
        assert old_1 == self.ll_data_1
        assert old_2 == self.ll_data_2
        new_3 = self.ll_data_1 + self.ll_data_2 + self.ll_data_1 + self.ll_singular
        assert list(new_3) == [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 0]

    def test_mult(self, ll_gen):
        old = self.ll_data_1.copy()
        new = self.ll_data_1 * 3
        empty = self.ll_data_1 * 0
        still_empty = self.ll_data_1 * (-3)
        assert list(new) == [1, 2, 3, 1, 2, 3, 1, 2, 3]
        assert list(empty) == []
        assert list(still_empty) == []
        assert len(new) == 9
        assert len(empty) == 0
        assert len(still_empty) == 0
        assert old == self.ll_data_1

    def test_operation_errors(self, ll_gen):
        with pytest.raises(TypeError):
            dummy = self.ll_data_1 + 2
        with pytest.raises(TypeError):
            dummy = self.ll_data_1 + [4, 5, 6, 7]
        with pytest.raises(TypeError):
            dummy = self.ll_data_1 * self.ll_data_2
        with pytest.raises(TypeError):
            dummy = self.ll_data_1 * 1.5
        



            

