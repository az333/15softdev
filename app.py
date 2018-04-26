
def minReq(password):
    lower = [x for x in password if x.islower()]
    upper = [x for x in password if x.isupper()]
    num = [x for x in password if x.isdigit()]
    return len(lower) > 0 and len(upper)> 0 and len(num) > 0

print minReq("az")
print minReq("Az")
print minReq("AZ1")
print minReq("Az1")


def strength(password):
    if minReq(password):
        lower = {x for x in password if x.islower()}
        upper = {x for x in password if x.isupper()}
        num = {x for x in password if x.isdigit()}
        special = {x for x in password if not x.isalnum()}
        lists = [upper, lower, num, special]
        quality = 0.25 * len(password)
        for lis in lists:
            if len(lis) > 0:
                quality += len(lis)
            else:
                quality -= 2
        if quality > 10:
            quality = 10
    else:
        quality = "your password so is so bad that it doesn't even meet the minimum requirements"
    return quality



print strength("2aacbA!")
