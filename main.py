# Homework 11

# 1. Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу
# всі слова, що складаються не менше ніж з семи літер.
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.
# 3. Створіть програму, яка перевіряє текст на неприпустимі слова.
# Якщо неприпустиме слово знайдено, його слід замінити на набір символів *.
# За підсумками роботи програми необхідно показати статистику дій.


################## 1

# with open("Test_1.txt", "w") as test_file:
#     test_file.write("Даний текстовий файл. Необхідно створити новий файл, який потрібно переписати з першого файлу\n"
#                     "всі слова, що складаються не менше ніж з семи літер 1234567")
#
# input_file_name = "Test_1.txt"
# output_file_name = "Test_2.txt"
#
# with open(input_file_name, "r") as input_file:
#     content = input_file.read()
#
# with open(output_file_name, "w") as output_file:
#     words = content.split()
#
#     selected_words = [word for word in words if len(word) >= 7]
#
#     output_file.write(" ".join(selected_words))
#
# with open(input_file_name, "r") as input_file:
#     input_content = input_file.read()
#     print(f"Вміст першого файлу: {input_content}")
# with open(output_file_name, "r") as output_file:
#     output_content = output_file.read()
#     print(f"Вміст другого файлу: {output_content}")
#
#
# ################## 2
# with open(input_file_name, "r") as input_file:
#     content = input_file.read()
#     word_count = len(content.split())
#     print(f"Кількість слів у тексті першого файлу: {word_count}")
#
# with open(output_file_name, "r") as output_file:
#     content = output_file.read()
#     word_count = len(content.split())
#     print(f"Кількість слів у тексті другого файлу: {word_count}")
#
#

# ################## 3

# def replace_forbidden_words(text, forbidden_words):
#     replaced_text = text
#
#     for word in forbidden_words:
#         replaced_text = replaced_text.replace(word, "*" * len(word))
#
#     return replaced_text
#
#
# def main():
#     with open("text.txt", "w") as input_file:
#         input_file.write("""To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles,
# And by opposing end them? To die: to sleep; No more; and by a sleep to say we end
# The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation
# Devoutly to be wish'd. To die, to sleep""")
#
#     with open("text.txt", "r") as input_file:
#         text = input_file.read()
#
#     forbidden_words = ["die"]
#     modified_text = replace_forbidden_words(text, forbidden_words)
#
#     with open("correct_text.txt", "w") as output_file:
#         output_file.write(modified_text)
#
#     forbidden_words_count = text.count("die")
#     print(f"Статистика: {forbidden_words_count} заміни {"слова" if forbidden_words_count == 1 else "слів"} {', '.join(forbidden_words)}.")
#
#
# if __name__ == "__main__":
#     main()
