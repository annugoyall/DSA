import hashlib

class ConsistentHashing:
    def __init__(self, nodes, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.nodes = nodes
        for node in self.nodes:
            self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            key = self._hash(node+str(i))
            self.ring[key] = node

    def remove_node(self, node):
        for i in range(self.replicas):
            key = self._hash(node+str(i))
            del self.ring[key]

    def get_node(self, key):
        if not self.ring:
            return None

        hash_val = self._hash(key)
        sorted_keys = sorted(self.ring.keys())
        for ring_key in sorted_keys:
            if hash_val <= ring_key:
                return self.ring[ring_key]
        return self.ring[sorted_keys[0]]

    def _hash(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

# Example usage
nodes = ['node1', 'node2', 'node3']
consistent_hashing = ConsistentHashing(nodes)

# Get node for a key
print(consistent_hashing.get_node('key1'))
print(consistent_hashing.get_node('key2'))

# Add a new node
consistent_hashing.add_node('node4')

# Get node for keys again
print(consistent_hashing.get_node('key1'))
print(consistent_hashing.get_node('key2'))

# Remove a node
consistent_hashing.remove_node('node1')

# Get node for keys again
print(consistent_hashing.get_node('key1'))
print(consistent_hashing.get_node('key2'))
