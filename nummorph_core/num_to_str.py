from .dicts import str_nums


def num_to_str(num: int):
    num = str(num)
    str_num = []
    segments = [num[-i-3:-i] if i != 0 else num[-i-3:] for i in range(0, len(num), 3)]
    segments.reverse()
    # proccess each segment
    for seg in segments:
        i = 0
        temp = []
        has_value = False
        while i < len(seg):
            if int(seg[i:len(seg)]) not in str_nums and int(seg[i:len(seg)]) != 0: # avoid ignoring 'teen' numbers
                has_value = True
                # third digit
                if i < len(seg)-2:
                    temp.append(str_nums[int(seg[i])])
                    if int(seg[i]) != 0:
                        tens = 10
                        tens **= len(seg[i:-1])
                        temp.append(str_nums[tens])
                    i += 1
                # second digit
                elif i == len(seg)-2:
                    d = int(seg[i])*10
                    temp.append(str_nums[d])
                    i += 1
                # first digit
                elif i == len(seg)-1:
                    temp.append(str_nums[int(seg[i])])
                    i += 1
            # 'teen' numbers
            elif int(seg[i]) != 0:
                has_value = True
                temp.append(str_nums[int(seg[i:len(seg)])])
                i += 1   
                break
            else:
                i += 1

        temp = ' '.join(temp)

        pow = (len(segments) - segments.index(seg)) - 1  # Determine the scale (thousand, million, etc)
        if pow == 0 and has_value:
            str_num.append(temp)
        elif has_value:
            str_num.extend([temp, str_nums[1000**pow], 'and'])

    # delete extra 'and'
    if str_num[-1] == 'and':
        str_num.pop(-1)

    return ' '.join(str_num)


if __name__ == "__main__":
    num = input().lower()
    print(num_to_str(num))