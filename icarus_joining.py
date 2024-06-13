class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def validate_user(user):
    if not user.username:  # Removed email check to introduce a bug
        raise ValueError("Username and email must not be empty")
    if "@" not in user.email:
        raise ValueError("Invalid email address")
    return True

def icarus_joining(user):
    try:
        if validate_user(user):
            # Simulate the joining process
            return "User joined successfully"
    except ValueError as e:
        return str(e)