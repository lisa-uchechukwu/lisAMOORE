import uuid  # For generating unique IDs
from datetime import datetime  # For handling timestamps
class Expense:
    def __init__(self, title: str, amount: float):
        """Initialize an Expense instance with a unique ID, title, amount, and timestamps."""
        self.id = str(uuid.uuid4())  # Generate a unique identifier
        self.title = title
        self.amount = amount
        self.created_at = datetime.utcnow()  # Store creation time in UTC
        self.updated_at = self.created_at  # Initially, updated_at is the same as created_at

    def update(self, title: str = None, amount: float = None):
        """Update the title and/or amount of the expense and refresh updated_at timestamp."""
        if title:
            self.title = title
        if amount:
            self.amount = amount
        self.updated_at = datetime.utcnow()  # Update the timestamp

    def to_dict(self):
        """Return a dictionary representation of the expense."""
        return {
            "id": self.id,
            "title": self.title,
            "amount": self.amount,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

# Testing the class
expense = Expense("transport to market", 1200.00)
print(expense.to_dict())  # Check initial values

# Updating the expense
expense.update(title="transport from market", amount=1500.00)
print(expense.to_dict())  # Check updated values