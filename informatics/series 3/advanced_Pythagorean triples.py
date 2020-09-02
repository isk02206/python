'''
Created on 2018. 09. 11
@Subject : pythagorean_triples
@Author : Son Jee Hun
@Student Number : 01406444
'''
sum_length_of_right_angle_triangle = int(input()) #sum of length right angles triangle
# 0 < oppsite <= adjacent <= hypothenuse
#oppsite is the shortest side, adjacent is the next little side, hypothenuse is the longest side
for oppsite in range(1, sum_length_of_right_angle_triangle - 1):
    #print(oppsite)
    for adjacent in range(oppsite + 1, sum_length_of_right_angle_triangle):
        hypothenuse = (oppsite ** 2 + adjacent ** 2) ** (1/2) # arrangement of pythagorean formulas in hypothenuse
        #print(adjacent)
        if oppsite ** 2 + adjacent ** 2 == hypothenuse ** 2:
            # pythagorean formulas adjacent ** 2 + opposite ** 2 = hypothenuse ** 2
            if oppsite + adjacent + hypothenuse == sum_length_of_right_angle_triangle:
                print('(' + str(oppsite) + ',', str(adjacent) + ',', str(int(hypothenuse)) + ')')
