

if __name__ == "__main__":
    from nummorph_core.str_to_num import str_to_num
    from nummorph_core.num_to_str import num_to_str
    text = input("Enter: ").lower()
    if text.isdigit():
        print(num_to_str(text))
    else:
        print(str_to_num(text))

else:
    from .nummorph_core.str_to_num import str_to_num
    from .nummorph_core.num_to_str import num_to_str