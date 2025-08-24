#Task 2: Implement a Basic LRU Cache

class LRUCache:
    def __init__(self, capacity):
        """
        Initialize the cache with a fixed capacity.
        """
        self.capacity = capacity
        self.cache = {}          # Store key-value pairs
        self.usage_order = []    # Store keys in usage order (least recent → most recent)

    def get(self, key):
        """
        Return the value of the key if present in cache, else return -1.
        Move the key to the end to show that it was recently used.
        """
        if key not in self.cache:
            return -1
        
        # Move key to the end (most recently used)
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache[key]

    def put(self, key, value):
        """
        Insert or update the value of the key.
        If the key exists, update it and move to the end.
        If the key doesn't exist and cache is at capacity,
        remove the least recently used item (from the start).
        """
        if key in self.cache:
            # Update value and usage
            self.cache[key] = value
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            if len(self.cache) >= self.capacity:
                # Evict least recently used key
                lru_key = self.usage_order.pop(0)
                del self.cache[lru_key]
            
            # Insert new key
            self.cache[key] = value
            self.usage_order.append(key)
