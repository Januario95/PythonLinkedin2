# from pytube import YouTube


# def download():
# 	os.chdir('C:/Users/a248433/Downloads')
#     youtubeObject = YouTube(link)
#     print(youtubeObject.title)
#     file_path = os.getcwd() + "\\" + youtubeObject.title + '.mp4'
#     print(file_path)
#     path = Path(file_path)
#     if path.exists():
#         pass
#     else:
#         try:
#             youtubeObject = youtubeObject.streams.get_highest_resolution()
#             youtubeObject.download()
#         except Exception as e:
#             raise e

points = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(points)

children = ['Sue', 'Jerry', 'Linda']
# print(sorted(children))
# print(sorted(['Sue', 'jerry', 'linda']))
# print('a' > 'A')

words = 'My favorite child is Linda'
# print(words.split())
# print(sorted(words.split()))
# print(sorted(words.split(),
# 	key=str.upper))
# print(sorted(words.split(),
# 	key=str.upper, reverse=True))

# leader = {321: 'CKL', 123: 'ABC',
# 		  432: 'JKC'}
# print(leader)
# print(sorted(leader, reverse=True))
# print(leader.get(432))

students = [
	('alice', 'B', 12),
	('eliza', 'A', 16),
	('tae', 'C', 15)
]
# print(sorted(students,
# 	key=lambda student: student[0]))




import math
import statistics

# print(math.radians(360))
# print(math.pi * 2)
# print(math.degrees(math.pi * 2))

ages = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(ages))
print(statistics.mode(ages))
print(statistics.median(ages))
print(sorted(ages))

print(statistics.variance(ages))
print(statistics.stdev(ages))
print(math.sqrt(statistics.variance(ages)))