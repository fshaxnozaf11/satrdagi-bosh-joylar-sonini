def bo'sh_joylar_soni(satr):
    return len(satr) - len(satr.replace(" ", ""))

print(bo'sh_joylar_soni("Hello World"))  # 1
print(bo'sh_joylar_soni("   "))  # 3
print(bo'sh_joylar_soni("Python"))  # 0
