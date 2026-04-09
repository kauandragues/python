def exe02(strs):
    prefix = ""
    for index, letter in enumerate(strs[0]):
        is_common = True
        for word in strs:
            try:
                if word[index] != letter:
                    global is_commom
                    is_common = False
                    break
            except IndexError:
                return prefix

        if is_common:
            prefix += letter
        else:
            return prefix

    return prefix

print(exe02(["flower","flow","flight"]))