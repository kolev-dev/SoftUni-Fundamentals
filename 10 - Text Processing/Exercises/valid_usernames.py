def validate_length(username: str) -> bool:
    if 3 <= len(username) <= 16:
        return True
    return False

def validate_characters(username: str) -> bool:
    for character in username:
        if character.isalnum() or character == "-" or character == "_":
            pass
        else:
            return False
    return True

def no_redundant_symbols(username) -> bool:
    if " " in username:
        return False
    return True

usernames = input().split(", ")
validated = [username for username in usernames\
             if validate_length(username)\
             and validate_characters(username)\
             and no_redundant_symbols(username)]

for validated_username in validated:
    print(validated_username)