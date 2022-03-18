s = input()
upper = [i for i in s if str(i).isupper()]
lower = [i for i in s if str(i).islower()]

x = compile('print(f"There are {len(upper)} number of upper case and {len(lower)} number of lower case letters")', 'tst', 'exec')
exec(x)