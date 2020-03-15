def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    

    print("Splitting", total_candies, "candy" if total_candies < 2 else "candies")
    print('The remaining', 'candy after split:' if((total_candies % 3)<2) else 'candies after split:')
    return total_candies % 3

print(to_smash(91))
print(to_smash(1))
print(to_smash(8))
