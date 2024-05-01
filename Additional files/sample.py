# for i in range(0,6):
#     val = 1
#     for j in range(i+1):
#         print(val, end=" ")
#         val = val * (i-j) // (j+1)
#     print()

# para = 'Python is a computer programming language often used to build websites and software, automate tasks, and analyze data. Python is a general-purpose language, not specialized for any specific problems, and used to create various programmes. This versatility and its beginner-friendliness have made it one of the most used programming languages today. In 2020, more than one-third of Indian IT professionals said Python was their preferred programming language. It continues to top lists of the most desired programming languages in the country'
# data = para.split()
# new_dict = {}
# for i in data:
#     if i in new_dict:
#         new_dict[i] += 1
#     else:
#         new_dict[i] = 1
# print("Word count: ", len(data))
# print("Repeated word count:")
# print(new_dict)

# strg = 'The quick Brow Fox'
# up = 0
# low = 0
# for i in strg:
#     if i.isupper():
#         up += 1
#     elif i.islower():
#         low += 1
# print("Uppercase count:", up)
# print("Lowercase count:", low)


# s5 = st.number_input('NA Sales', min_value=0.0, max_value=6.431174, value=3.215587)
# s6 = st.number_input('EU Sales', min_value=0.0, max_value=5.381450, value=2.690725)
# s7 = st.number_input('JP Sales', min_value=0.0, max_value=3.196873, value=1.5984365)
# s8 = st.number_input('Other Sales', min_value=0.0, max_value=3.251154, value=1.625577)
# s9 = st.number_input('Critic Score', min_value=0.0, max_value=9.899495, value=4.9497475)
# s10 = st.number_input('Critic Count', min_value=0.0, max_value=10.630146, value=5.315073)
# s11 = st.number_input('User Score', min_value=0.0, max_value=95.0, value=47.5)
# s12 = st.number_input('User Count', min_value=0.0, max_value=103.271487, value=51.6357435)