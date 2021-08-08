from hash_map import HashMap


class TestHashMap:
    def test_access(self):
        hash_map = HashMap()
        hash_map['turkey'] = 20
        assert hash_map['turkey'] == 20
