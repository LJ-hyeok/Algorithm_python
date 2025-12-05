import sys

# 빠르게 입력을 받기 위한 설정
input = sys.stdin.readline

def check(battery_capacity, n, dists):
    move_right = min(dists[0], battery_capacity)
    for i in range(1, n - 1):
        prev_dist = dists[i-1] # 왼쪽 구간 거리a
        curr_dist = dists[i]   # 오른쪽 구간 거리
        move_left = prev_dist - move_right

        if move_left > battery_capacity:
            return False

        rem_battery = battery_capacity - move_left
        move_right = min(curr_dist, rem_battery)

    last_gap = dists[n-2] - move_right
    if last_gap > battery_capacity:
        return False

    return True

def solve():
    # 입력 처리
    try:
        # L: 도로 길이, N: 로봇 개수
        line1 = input().split()
        if not line1: return
        l, n = map(int, line1)
        
        # 로봇 위치 배열
        line2 = input().split()
        if not line2: arr = []
        else: arr = list(map(int, line2))
    except ValueError:
        return

    # 예외 처리: 로봇이 1개 이하라면 움직일 필요 없음
    if n <= 1:
        print(0)
        return

    # 인접한 로봇 사이의 거리(구간) 계산
    # dists[i]는 i번째 로봇과 i+1번째 로봇 사이의 거리
    dists = []
    for i in range(n - 1):
        dists.append(arr[i+1] - arr[i])

    # 이분 탐색 (Binary Search)
    # 최소 배터리 0부터 최대 배터리 L까지 탐색
    low = 0
    high = l
    ans = l

    while low <= high:
        mid = (low + high) // 2
        
        if check(mid, n, dists):
            # mid 용량으로 가능하다면, 더 작은 용량도 가능한지 확인 (왼쪽 탐색)
            ans = mid
            high = mid - 1
        else:
            # mid 용량으로 부족하다면, 용량을 늘려야 함 (오른쪽 탐색)
            low = mid + 1

    print(ans)

if __name__ == '__main__':
    solve()