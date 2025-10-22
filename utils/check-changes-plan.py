import json
import sys

def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Example usage: python3 ./check-changes-plan.py <file-path>")
        sys.exit(1)
    file_path = sys.argv[1]
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        plan_json = json.load(f)
        print(json.dumps(plan_json['resource_changes']))
        


if __name__ == "__main__":
    main()