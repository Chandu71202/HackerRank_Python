import re

if __name__ == '__main__':
    _input = input()
    pattern = r'(\w)\1'
    matcher = re.search(pattern, _input)
    if matcher:
        print(matcher.group(1))
    else:
        print(-1)
