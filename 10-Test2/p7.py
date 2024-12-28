import re

def f(usernames):
    """Returns the number of valid usernames in the given array."""
    valid_count = 0
    
    # Define a regular expression pattern for a valid username
    pattern = r'^[a-z0-9_]{4,12}$'
    
    for username in usernames:
        # Check if the username matches the pattern
        if re.match(pattern, username):
            valid_count += 1
            
    return valid_count

# Example usage:
result = f(["uek", "water_7_x", "anna.may", "a_b_c_d_e_f"])
print(result)  # This will print 2