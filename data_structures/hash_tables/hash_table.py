from .linked_list import LinkedList


class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = [None] * self.table_size

    def __repr__(self):
        return f'Hashtable : {self.hashtable}'

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """

        hash_key = self._hash_key(key)
        key_value = [key, value]

        if self.hashtable[hash_key] is None:
            self.hashtable[hash_key] = list([key_value])
            return True
        else:
            for pair in self.hashtable[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hashtable[hash_key].append(key_value)
            return True

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hash_key = self._hash_key(key)
        if self.hashtable[hash_key] is not None:
            for pair in self.hashtable[hash_key]:
                if pair[0] == key:
                    return pair[1]
        return None

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        hash_key = self._hash_key(key)

        if self.hashtable[hash_key] is None:
            return False
        for i in range(0, len(self.hashtable[hash_key])):
            if self.hashtable[hash_key][i][0] == key:
                self.hashtable[hash_key].pop(i)
                return True
        return False



