from timeit import timeit

items = {
	'a': 1,
	'b': 2,
}
default = -1

def use_catch(key):
	try:
		return items[key]
	except KeyError:
		return default

def use_get(key):
	return items.get(key, default)


if __name__=='__main__':
	print('catch', timeit('use_catch("a")',
		  'from __main__ import use_catch'))
	print('catch', timeit('use_get("a")',
		  'from __main__ import use_get'))
	print('')
	print('catch', timeit('use_catch("x")',
		  'from __main__ import use_catch'))
	print('get', timeit('use_get("x")',
		  'from __main__ import use_get'))

