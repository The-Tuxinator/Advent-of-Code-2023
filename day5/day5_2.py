def source_to_destination(source, dest_map):
    print(f"destmap: {dest_map}")
    for row in dest_map:
        if row[0] <= source <= row[1]:
            return source + row[2]
    return source

def dest_map_breakdown(i, dest_map):
    print(dest_map[0])
    dest_map = dest_map[1:]
    print(dest_map)
    lookup_table = []
    for row in dest_map:
        if row == "":
            continue
        # print(row)
        row = [int(x) for x in row.split()]
        low = row[1]
        high = row[1]+row[2]
        offset = row[0] - row[1]
        lookup_table.append([low, high, offset])
    return lookup_table


def seed_to_location(seed, dest_maps):
    for row in dest_maps:
        seed = source_to_destination(seed, row)
        print(seed)
    return seed

with open("input5", "r") as input_file:
    almanac = input_file.read()

almanac = almanac.split("\n\n")
almanac = [x.split("\n") for x in almanac]

# Extract the numbers from the seed line and remove it from the almanac
seeds = str(almanac.pop(0))

# convert seeds to separate ints
seeds = [int(x) for x in seeds[:-2].split(":")[1].split()]
seed_starts = seeds[0::2]
seed_ends = seeds[1::2]



almanac = [dest_map_breakdown(i, x) for i, x in enumerate(almanac)]


for i, seed_range in enumerate(seed_starts):
    print([range(seed_range, seed_ends[i])])
    for seed in [*range(seed_range, seed_ends[i])]:
        print(seed)
        print(seed_to_location(seed, almanac))







# print(almanac)
# locations = []
# for seed< in seeds:

# print(locations)
# print(min(locations))
# print(seeds)
# seed_locations = []
# for i, source in enumerate(seeds):
#     for dest_map in almanac:
#         source = dest_map_breakdown(source, dest_map)
#     seed_locations.append(source)
#     print(f"Seed {i}: {source}")
# print(min(seed_locations))
