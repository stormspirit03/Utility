n=10    # number of buckets
value=15    # value to  hash

# implementation 

hash_table={i:[] for i in range (n)}

def hash_function(value,n):
    result=value%n
    return result

hash_value=hash_function(value,10)
hash_table[hash_value].append(value)

print(hash_table)