def checking_password(password):
    return len(password) > 8 and password.lower() != password

print(checking_password(password = input()))