import os, json, regex, sys

def check_variable(coco: str, toggle: str, absMonth: str):
    """Find and evaluate condition blocks containing a toggle.

    A condition block is considered complete when it contains both:
    - the requested toggle
    - a condition matching the target absolute month

    Args:
        toggle: Toggle name to search for.
        abs_month: Target absolute month, such as ``"142"``.
        variable_path: Path to the variable definition JSON file.

    Returns:
        A list of ``(score, path)`` matches, where:
        - ``score == 1`` means the block is complete.
        - ``score == 0`` means the toggle exists but the month is missing
          or does not match.
        - ``path`` is the one-based location of the block in the tree.
    """

    content = open("./variables/01.020", "r").read()
    data: dict = json.loads(content)

    condition_blocks = data["condition"]["conditions"]

    def walk_conditions(blocks, path=()):
        
        for index, block in enumerate(blocks):

            current_path: tuple = path + (index + 1,)

            if toggle in block["condition"]:

                if "AbsMonth(Today()) >= " + absMonth in block["condition"]:                                    
                    yield 1, current_path
                else:
                    yield 0, current_path

            children: list = block.get("childs", [])
            if children:
                yield from walk_conditions(children, current_path)
            
        
    matches = list(walk_conditions(condition_blocks))

    if matches:
        print(f"Found {len(matches)} matches:")
        for match in matches:
            print(f"Path: {match}")
    











if __name__ == "__main__":
    coco, toggle, absMonth = sys.argv[1], sys.argv[2], sys.argv[3]
    check_variable(coco, toggle, absMonth)