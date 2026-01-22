class KeyValueStore:
    def __init__(self):
        # Main committed data
        self.store = {}
        
        # Stack of transactions
        # Each transaction is a dict of changes: {key: value}
        # Use special marker for deletes: {key: DELETED}
        self.transactions = []
        
        # Sentinel value for deleted keys
        self.DELETED = object()
    
    def set(self, key: str, value: int) -> None:
        """Set key to value"""
        if self.transactions:
            # We're in a transaction, record change in current transaction
            self.transactions[-1][key] = value
        else:
            # No transaction, update main store
            self.store[key] = value
    
    def get(self, key: str) -> int:
        """
        Get value for key
        Check transactions from most recent to oldest, then main store
        """
        # Check transactions stack (newest first)
        for transaction in reversed(self.transactions):
            if key in transaction:
                value = transaction[key]
                if value is self.DELETED:
                    return None  # Key was deleted in this transaction
                return value
        
        # Not in any transaction, check main store
        return self.store.get(key)
    
    def delete(self, key: str) -> None:
        """Delete key"""
        if self.transactions:
            # Mark as deleted in current transaction
            self.transactions[-1][key] = self.DELETED
        else:
            # No transaction, delete from main store
            if key in self.store:
                del self.store[key]
    
    def begin(self) -> None:
        """Start a new transaction"""
        # Push new empty transaction onto stack
        self.transactions.append({})
    
    def commit(self) -> None:
        """
        Commit current transaction
        Merge changes into parent transaction (or main store if top-level)
        """
        if not self.transactions:
            raise Exception("No transaction to commit")
        
        # Pop current transaction
        current_transaction = self.transactions.pop()
        
        if self.transactions:
            # There's a parent transaction, merge into it
            for key, value in current_transaction.items():
                self.transactions[-1][key] = value
        else:
            # No parent transaction, merge into main store
            for key, value in current_transaction.items():
                if value is self.DELETED:
                    if key in self.store:
                        del self.store[key]
                else:
                    self.store[key] = value
    
    def rollback(self) -> None:
        """
        Rollback current transaction
        Discard all changes in this transaction
        """
        if not self.transactions:
            raise Exception("No transaction to rollback")
        
        # Simply pop and discard the current transaction
        self.transactions.pop()


# ============================================
# TESTS
# ============================================

def test_basic_operations():
    store = KeyValueStore()
    
    store.set('a', 1)
    assert store.get('a') == 1
    
    store.set('a', 2)
    assert store.get('a') == 2
    
    store.delete('a')
    assert store.get('a') is None
    
    print("✅ Basic operations passed")


def test_single_transaction():
    store = KeyValueStore()
    
    store.set('a', 1)
    
    store.begin()
    store.set('a', 2)
    assert store.get('a') == 2  # See uncommitted change
    store.commit()
    
    assert store.get('a') == 2  # Change is now permanent
    
    print("✅ Single transaction passed")


def test_rollback():
    store = KeyValueStore()
    
    store.set('a', 1)
    
    store.begin()
    store.set('a', 2)
    store.rollback()
    
    assert store.get('a') == 1  # Back to original value
    
    print("✅ Rollback passed")


def test_nested_transactions():
    store = KeyValueStore()
    
    store.set('a', 1)
    
    store.begin()  # Transaction 1
    store.set('a', 2)
    assert store.get('a') == 2
    
    store.begin()  # Transaction 2 (nested)
    store.set('a', 3)
    assert store.get('a') == 3
    
    store.rollback()  # Rollback transaction 2
    assert store.get('a') == 2  # Back to transaction 1
    
    store.commit()  # Commit transaction 1
    assert store.get('a') == 2  # Now permanent
    
    print("✅ Nested transactions passed")


def test_delete_in_transaction():
    store = KeyValueStore()
    
    store.set('a', 1)
    
    store.begin()
    store.delete('a')
    assert store.get('a') is None  # Deleted in transaction
    store.rollback()
    
    assert store.get('a') == 1  # Restored after rollback
    
    print("✅ Delete in transaction passed")


def test_complex_scenario():
    """The example from problem statement"""
    store = KeyValueStore()
    
    store.set('a', 1)
    assert store.get('a') == 1
    
    store.begin()
    store.set('a', 2)
    assert store.get('a') == 2
    
    store.begin()
    store.set('a', 3)
    assert store.get('a') == 3
    
    store.rollback()
    assert store.get('a') == 2
    
    store.commit()
    assert store.get('a') == 2
    
    store.begin()
    store.set('b', 10)
    store.rollback()
    assert store.get('b') is None
    
    print("✅ Complex scenario passed")


def test_multiple_keys():
    store = KeyValueStore()
    
    store.set('a', 1)
    store.set('b', 2)
    
    store.begin()
    store.set('a', 10)
    store.set('c', 30)
    
    assert store.get('a') == 10
    assert store.get('b') == 2  # Unchanged
    assert store.get('c') == 30
    
    store.commit()
    
    assert store.get('a') == 10
    assert store.get('b') == 2
    assert store.get('c') == 30
    
    print("✅ Multiple keys passed")


# Run all tests
if __name__ == "__main__":
    test_basic_operations()
    test_single_transaction()
    test_rollback()
    test_nested_transactions()
    test_delete_in_transaction()
    test_complex_scenario()
    test_multiple_keys()
    print("\n🎉 All tests passed!")