n = int(input())

layer = 1
end = 1
while end < n:
    end += 6*layer
    layer += 1
print(layer)