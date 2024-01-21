import sys


def generate_framed_text(lines):
    framed_lines = []
    for line in lines:
        framed_line = "|" + line + "|"
        framed_lines.append(framed_line)
    framed_text = "\n".join(framed_lines)
    return framed_text

def main():
    lines = input("Enter the lines of text: ").splitlines()
    framed_text = generate_framed_text(lines)
    print(framed_text)

if __name__ == "__main__":
    main()
