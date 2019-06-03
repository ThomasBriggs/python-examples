def isNum(s):
    if s == "e" or s == "E" or s == ".":
        return False
    else:
        try:
            float(s)
            return True
        except ValueError:
            if ". " in s or ".e" in s or ".E" in s or "e." in s or "e " in s or " e" in s or "+e" in s or "+E" in s
            or ".." in s:
            return False
        else:
            if "E" in s or "e" in s:
                if s[0] == "e" or s[0] == "E" or s[len(s)-1] == "e" or s[len(s)-1] == "E":
                    return False
                else:
                    sArray = list(s).pop(s.find("e"))
                    return isNum(''.join(sArray))
            return False
