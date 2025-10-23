import json
import sys


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Error: Invalid number of arguments {0}\n".format(len(sys.argv)))
        sys.stderr.write("Arguments: {0}".format(sys.argv))
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