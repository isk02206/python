n = int(input())
skip = n//2
hitchhikers = []
for i in range(n):
    score = float(input())
    hitchhikers.append(score)
rank_group = hitchhikers[:skip]
compare_group = hitchhikers[skip:]
max_rank = max(rank_group)
for x in compare_group:
    if float(x) > max_rank:
        print(float(x))
        break
else:
    print(float(compare_group[-1]))