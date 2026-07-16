

#! Any Func
# numbers = [3, 19, 90, 45, 32]

# result = any(number > 80 for number in numbers)

# print(result)

# programming_language = ['python', 'java', 'go']

# print(
#     any(pl == 'python' for pl in programming_language)
# )

# print(
#     any(pl == 'C#' for pl in programming_language)
# )

# passwords = ['123', '98a', '12q', '987']

# print(
#     any(ch.isalpha() for pwd in passwords for ch in pwd)
# )

#! Password is valid
#? en az 16 karakterli olsun
#* en az bir büyük harf bir küçük harf olsun
#todo en az bir noktalama işareti olsun
#? en az bir tane rakam
#todo: HINT: string kütüphanesinde noktalama işaretleri hazır olarak var.
#todo: Sample PWD: beast?Beast1beast

from string import punctuation

pwd = input('Password: ')

if len(pwd) < 16:
    print('Invalid Password..!')
if not any(ch.isupper() for ch in pwd):
    print('Invalid Password..!')
if not any(ch.islower() for ch in pwd):
    print('Invalid Password..!')
if not any(ch.isdigit() for ch in pwd):
    print('Invalid Password..!')
if not any(ch in punctuation for ch in pwd):
    print('Invalid Password..!')
print('Valid Password')

