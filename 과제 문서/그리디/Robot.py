def chk(capacity):
    move_right = min(dist[0], capacity) # 첫 번째 로봇
    
    for i in range(1, len(dist)): # 중간 로봇
        prev =  dist[i-1]
        cur = dist[i]
        move_left = prev - move_right
        
        # 왼쪽으로 마중조차 나갈 수 없는 경우
        if(move_left > capacity):
            return False

        move_right = min(capacity - move_left, cur)
        
    if(dist[n-2] - move_right > capacity): # 마지막 로봇
        return False
    return True

l, n = map(int, input().split())
arr = list(map(int, input().split()))
dist = []        
for i in range(n-1):
    dist.append((arr[i+1] - arr[i]))

left = 0
right = ans = l
while(left<=right):
    mid = (left + right)//2
    if(chk(mid)):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)