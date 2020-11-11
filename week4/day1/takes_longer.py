qoute = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

mid_str = "always takes longer than"

temp = qoute.split()
mid_pos = len(temp) // 4

res = temp[:mid_pos] + [mid_str] + temp[mid_pos:]

res = ' '.join(res)

print("" + str(res))