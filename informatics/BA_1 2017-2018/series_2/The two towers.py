out1 = str(input())
out2 = str(input())
sci = str(input())

if sci == 'first':
    if out1 == 'tail':
        sci1 = 'tail'
        if out2 == 'tail':
            sci2 = 'head'
        if out2 == 'head':
            sci2 = 'tail'
    if out1 == 'head':
        sci1 = 'head'
        if out2 == 'tail':
            sci2 = 'head'
        if out2 == 'head':
            sci2 = 'tail'
if sci == 'second':
    if out2 == 'tail':
        sci2 = 'tail'
        if out1 == 'tail':
            sci1 = 'head'
        if out1 == 'head':
            sci1 = 'tail'
    if out2 == 'head':
        sci2 = 'head'
        if out1 == 'tail':
            sci1 = 'head'
        if out1 == 'head':
            sci1 = 'tail'

print(sci1)
print(sci2)