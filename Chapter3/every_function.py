# Exercise 3-10. From the book Python Crash Course 2nd Edition by Eric Matthews
# Every Function: Think of something you could store in a list. 
# For example, you could make a list of mountains, rivers, countries, cities, languages, 
# or any-thing else you’d like. Write a program that creates a list containing these 
# items and then uses each function introduced in this chapter at least once.

lang_lst = '''english french kazakh russian german'''.split()

print(f"Original list:{lang_lst}")
print(f"\n Using title() method: {lang_lst[0].title()} ")

lang_lst[1] = 'polish'
print(f"\n Changing language from french to polish: {lang_lst}")

lang_lst.append('french')
print(f"\n Adding more elements with append(): {lang_lst}")

lang_lst.insert(1,'gaelic')
print(f"\n Inserting more elements with insert(): {lang_lst}")

del lang_lst[1]
print(f"\n Deleting elements with del: {lang_lst}")

lang_lst.pop(0)
print(f"\n Deleting elements with pop(): {lang_lst}")

lang_lst.remove('kazakh')
print(f"\n Deleting elements by value with remove(): {lang_lst}")

lang_lst.sort()
print(f"\n Sorting elements using sort(): {lang_lst}")

lang_lst.sort(reverse=True)
print(f"\n Reversing elements using sort(reverse=True): {lang_lst}")

print(f"\n Sorting elements using sorted(list): {sorted(lang_lst)}")

lang_lst.reverse()
print(f"\n Reversing elements using reverse(): {lang_lst}")
