"""
2, 3, 5, 7
11, 13, 17, 19
23, 29
31, 37
41, 43, 47
53, 59
61, 67
71, 73 79
83, 89
97
"""
# 2 থেকে নিয়ে ওই সংখ্যার আগ পর্যন্ত সংখ্যাগুলো দিয়ে ভাগ দিতে থাকব। যদি কোনো সংখ্যা দিয়ে ভাগ যায় তাহলে is_prime = False হবে। অর্থাৎ, সংখ্যাটি যৌগিক হবে. অন্যথায় মৌলিক হবে।

is_prime = True
n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print("Prime")
else:
    print("Not prime")