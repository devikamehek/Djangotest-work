from products.models import mobiles

# # print total number of mobiles
# print(len(mobiles))


# # print all mobile names
# for mob in mobiles:
#     print(mob.get("name"))
#     # print(mob["name"])


# # list comprehension
# print([mob.get("name") for mob in mobiles])

# print all samsung mobile names

# samsung_mob=[mob.get("name") for mob in mobiles if mob.get("brand")=="samsung"]
# print(samsung_mob)

# sort mobiles wrt price by desc
print(sorted(mobiles, key=lambda p: p.get("price"),reverse=True))

# print costly mobile
# print(max(mobiles,key=lambda m:m.get("price")))
# print(min(mobiles,key=lambda m:m.get("price")))
