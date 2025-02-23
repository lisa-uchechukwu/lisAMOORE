import uuid  # For generating unique IDs
from datetime import datetime  # For handling timestamps
# Define the Expense class first
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

# Now define ExpenseDatabase
class ExpenseDatabase:
    def __init__(self):
        """Initialize an empty list to store Expense instances."""
        self.expenses = []

    def add_expense(self, expense: Expense):  # Now Python knows what Expense is
        """Add an Expense object to the database."""
        self.expenses.append(expense)

    def remove_expense(self, expense_id: str):
        """Remove an expense from the database using its unique ID."""
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]

    def get_expense_by_id(self, expense_id: str):
        """Retrieve an expense by its unique ID."""
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None  # Return None if not found

    def get_expense_by_title(self, title: str):
        """Retrieve all expenses that match a given title."""
        return [expense for expense in self.expenses if expense.title.lower() == title.lower()]

    def to_dict(self):
        """Return a list of dictionaries representing all expenses in the database."""
        return [expense.to_dict() for expense in self.expenses]
# Run tests only if this script is executed directly
if __name__ == "__main__":
    # Create an instance of ExpenseDatabase
    db = ExpenseDatabase()

    # Create some expense objects
    expense1 = Expense("Groceries", 500000.00)
    expense2 = Expense("cosmetics", 260000.00)
    expense3 = Expense("toiletries", 20000.0)  

    # Add expenses to the database
    db.add_expense(expense1)
    db.add_expense(expense2)
    db.add_expense(expense3)

    # Print all expenses
    print("\nAll Expenses:")
    print(db.to_dict())

    # Retrieve an expense by ID
    found_expense = db.get_expense_by_id(expense1.id)
    print("\nFound Expense by ID:")
    print(found_expense.to_dict() if found_expense else "Not found")

    # Retrieve expenses by title
    grocery_expenses = db.get_expense_by_title("Groceries")
    print("\nExpenses with title 'Groceries':")
    print([expense.to_dict() for expense in grocery_expenses])

    # Remove an expense
    db.remove_expense(expense1.id)
    print("\nExpenses after removing one:")
    print(db.to_dict())