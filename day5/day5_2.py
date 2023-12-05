from functools import reduce


def source_to_destination(source, dest_map):
    # if source in range(dest_map[1], dest_map[1]+dest_map[2]):
    #     destination = (source - dest_map[1]) + dest_map[0]
    #     return destination
    return 0


def dest_map_breakdown(source, dest_map):
    # dest_map = dest_map[1:]
    # destination = 0
    # # print(dest_map)
    # for row in dest_map:
    #     destination = source_to_destination(source, [int(x) for x in row.split()])
    #     if destination:
    #         # print(destination)
    #         return destination
    # # print(source)
    return source



with open("input5", "r") as input_file:
    almanac = input_file.read()

maps = almanac.split("\n\n")
maps = [x.split("\n") for x in maps]

# Extract the numbers from the seed line and remove it from the maps
seeds = str(maps.pop(0))
# convert seeds to separate ints
seeds = [int(x) for x in seeds[:-2].split(":")[1].split()]
seed_starts = seeds[0::2]
seed_ends = seeds[1::2]
seeds = []
for i, seed_range in enumerate(seed_starts):
    seeds = seeds + [*range(seed_range, seed_range + seed_ends[i])]

print([seed_starts, seed_ends], seeds)
# print(seeds)
seed_locations = []
for i, source in enumerate(seeds):
    for dest_map in maps:
        source = dest_map_breakdown(source, dest_map)
    seed_locations.append(source)
    print(f"Seed {i}: {source}")
print(min(seed_locations))