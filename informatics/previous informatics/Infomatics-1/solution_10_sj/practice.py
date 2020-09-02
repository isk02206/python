dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
print(dict[2])
pop( a) = list에 있는 a를 뽑아내는것
만약에 ( ) 빈괄호일 경우 마지막껄 뽑는다
inser(position, a) a가 포지션안에 들어가게 하는것
Mutability(변할수있느냐 없는냐)
class종류들:
1string
word = 'ghent'
 word = word[pos1:] + word[:pos1]
word = word[pos2:] +word[:pos2]
print(word) - 두번쨰word만 print
2.integer
3.float
4.list- mutable
list1 = ['a','b','c']
list1.pop(0) - 0번쨰 자리를ㄹ 없앰
list1.pop(0)
list1 = ['c']
5.set
6.dictionary

list.append 안에는 argument가 하나만 들어가야 한다.


셋은 딕셔너리로 변환 가능
딕셔너리는 셋으로 변환 불가능

setdefault = set의 기본값을 정함
key 와 value를 정함

for x in seq:
x = 0
 while x < len(seq):
x += 1
