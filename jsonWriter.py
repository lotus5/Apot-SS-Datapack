

def json_writer(weight: int, quality: float, item: str, type: str, dimension: str, min_rarity: str, max_rarity: str) -> int:
    f = open("demofile.json", "w")
    f.write("{\n  \"conditions\": [{\n")
    f.write("    \"type\": \"forge:mod_loaded\",\n")
    f.write("    \"modid\": \"simplyswords\"\n")
    f.write("  }],\n")

    f.write("  \"weight\": " + str(weight) + ",\n  \"quality\": " + str(quality))
    f.write(",\n  \"stack\": {\n")
    f.write("    \"item\": " + item + ",\n")
    f.write("    \"count\": 1,\n")
    f.write("    \"nbt\": \"{Damage:0}\"\n")
    f.write("  },\n")

    f.write("  \"type\": " + type + ",\n")
    f.write("  \"dimensions\": [\n    " + dimension + "\n  ],\n")

    if min_rarity != None:
        f.write("  " + min_rarity + ",\n")
    f.write("  " + max_rarity + "\n}")

    f.close()
    return 1

json_writer(85, 4.0, "\"simplyswords:iron_scythe\"", "\"HEAVY_WEAPON\"", "\"minecraft:overworld\"", "\"max_rarity\": \"uncommon\"", "\"max_rarity\": \"rare\"")