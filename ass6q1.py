class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        """Returns the current password (last item in the list)"""
        return self.old_passwords[-1] if self.old_passwords else None

    def set_password(self, new_password):
        """Sets the new password only if it hasn't been used before"""
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password updated successfully.")
        else:
            print("Error: Password has been used before. Choose a new password.")

    def is_correct(self, password):
        """Checks if the given password matches the current password"""
        return password == self.get_password()

# Example Usage
pm = Password_manager()
pm.set_password("password123")  # First password
pm.set_password("password456")  # New password
print(pm.get_password())         # Output: password456
print(pm.is_correct("password456"))  # Output: True
print(pm.is_correct("wrongpass"))    # Output: False
pm.set_password("password123")  # Error: Reused password
