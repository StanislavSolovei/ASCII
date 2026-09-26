def decode_ascii_art(code):
    char1 = code[0]
    char2 = code[1]
    seq = code[2:]                    

    chars = [char1, char2]
    current_char_index = 0
    lines = []
    current_line_parts = []

    i = 0
    while i < len(seq):
        if i + 1 < len(seq) and seq[i] == '0' and seq[i + 1] == '0':
            lines.append(''.join(current_line_parts))
            current_line_parts = []
            current_char_index = 0
            i += 2
            continue

        count = int(seq[i])
        char = chars[current_char_index % 2]
        if count > 0:
            current_line_parts.append(char * count)
        current_char_index += 1
        i += 1

    if current_line_parts:
        lines.append(''.join(current_line_parts))

    return lines

code = " #90190200739023005290820032339332002141317131410011531173115100017393710001903290610001903190710001903290610011529043410021529013510032490352005290820073902300901902";

obrazek = decode_ascii_art(code)
for linia in obrazek:
    print(linia)
