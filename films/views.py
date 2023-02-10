from json import load

with open("db.json", "r", encoding="utf-8") as f:
    data = load(f)
print(len(data))

# # print all movie name
# print([m.get("title") for m in data])


# print movie names with crime genre
# print([m.get("title") for m in data if m.get("genres") == ( "Comedy","Adventure")])


# movie released in 2002
# print([m.get("title") for m in data if m.get("year") == ("2002")])

# lenghty movie
# lenghty_movie = max(data, key=lambda m: int(m.get("runtime")))
# print(lenghty_movie)

# shortest runtime movie
# shortest_movie=min(data, key=lambda m:int(m.get("runtime")))
# print(shortest_movie)


# movie relased in year
# mc = {}
# for m in data:
#     year = m.get("year")
#     if year in mc:
#         mc[year] += 1
#     else:
#         mc[year] = 1
# print(mc)
#
# print(max(mc, key=lambda k: mc.get(k)))  # in 2013 more movies relaesed
# print(max(mc.items(), key=lambda t: t[1]))

