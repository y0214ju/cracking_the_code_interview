def check_permutation(a: str, b: str): 
    if len(a) != len(b):
        return False
    str1 = "".join(sorted(a))
    str2 = "".join(sorted(b))
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

if __name__ == "__main__":
    if check_permutation("Test", "test"):
        print("True")
    else:
        print("False")

    

    

        
