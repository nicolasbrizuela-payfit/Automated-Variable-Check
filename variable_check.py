import os, json, regex, sys




def check_variable(coco: str, toggle: str, absMonth: str):
    file = open("./variables/01.020", "r")
    content = file.read()
    data = json.loads(content)

    condition_blocks = data["condition"]["conditions"]

    def walk_conditions(blocks, path=()):
        for index, block in enumerate(blocks):

            current_path = path + (index + 1,)

            if toggle in block["condition"] and "AbsMonth(Today()) >= " + absMonth in block["condition"]:
                # print(f"Found at path: {current_path}")
                yield current_path

            children = block.get("childs", [])
            
            if children:
                yield from walk_conditions(children, current_path)
            
        


    matches = list(walk_conditions(condition_blocks))

    if matches:
        print(f"Found {len(matches)} matches:")
        for match in matches:
            print(f"Path: {match}")
    


    # with open("output.txt", "w") as f:
    #     f.write()


if __name__ == "__main__":
    check_variable(sys.argv[1], sys.argv[2], sys.argv[3])