from .dicts import nums, tens

def str_to_num(text: str):
    words = text.split()
    total = 0
    temp = 0
    for word in words:
        if word in nums:
            temp += nums[word]
        elif word in tens:
            temp *= tens[word]
            if word != 'hundred':
                total += temp
                temp = 0
        elif word != 'and':
            return f"'{word}' is Invalid"

    total += temp
    return total


if __name__ == "__main__":
    text = input().lower().split()
    print(str_to_num(text))
