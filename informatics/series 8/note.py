# def solution(word, position=None):
#     dictionary = {}
#     if position == None:
#         position = '0123456789'
#     for i in word:
#         dictionary.update({i:position[word.index(i)]})
#     return dictionary
# print(solution('LOMXARYETS'))
# print(solution('AELMORSTXY', '4702159836'))
# print(solution('MERYXASTOL', '2765349810'))

high = int(input())
building_name = str(input())
pre_building_high = int(input())
print(building_name, 'is visible from the ground floor up to', pre_building_high, 'meters.')
counter = 1
while True:
    building_name = str(input())
    building_high = int(input())

    if pre_building_high < building_high:
        print(building_name, 'is visible from', pre_building_high, 'meters up to', building_high, 'meters.')
    else:
        continue
    pre_building_high = building_high
    counter += 1
    if counter == high:
        break


