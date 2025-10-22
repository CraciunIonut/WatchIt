import json
import sys

#TODO: resource_changes is a list of changes -> parse all of them and check the resource_changes.change.action for "no-op" 
# if any action is different from "no-op" then it means that it has changes, return true else return false

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: Invalid number of arguments")
        sys.exit(1)

    file_path = sys.argv[1]

    flag = False

    with open(file=file_path, mode='r', encoding='utf-8') as f:
        plan_json = json.load(f)

        for resource_change in plan_json["resource_changes"]:
            for action in resource_change["change"]["actions"]:
                if action != 'no-op':
                    flag = True
    
    print(flag)

    f.close()
                    
    sys.exit(0)

if __name__ == "__main__":
    main()