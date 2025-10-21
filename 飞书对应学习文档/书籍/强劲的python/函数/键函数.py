def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest

# 老方法 max_by_int_value(nums)
# 新方法 max_by_key(nums,int)

# 老方法 max_by_abs(interges)
# 新方法 max_by_key(intergers,abs)
