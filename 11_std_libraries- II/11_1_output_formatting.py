from reprlib import recursive_repr
import pprint
import textwrap


# class MyList(list):
#     @recursive_repr()
#     def __repr__(self):
#         return '<' + '|'.join(map(repr, self)) + '>'
#
#
# m = MyList('abc')
# m.append(m)
# m.append('x')
# print(m)




# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
#     'yellow'], 'blue']]]
#
# pprint.pprint(t, width=30)



# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
# wrapped_text = textwrap.wrap(text, width=130)
# for line in wrapped_text:
#     print(line)