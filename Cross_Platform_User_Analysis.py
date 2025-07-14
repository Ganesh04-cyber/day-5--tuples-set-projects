platform_a = {"ganesh", "riya", "aman", "neha"}
platform_b = {"riya", "sneha", "ganesh", "vijay"}

unique_users=platform_a.union(platform_b)
print(unique_users)

only_a=platform_a.difference(platform_b)
print(only_a)

only_b=platform_b.difference(platform_a)
print(only_b)