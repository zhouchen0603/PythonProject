points=[(1,0),(2,3),(1,1),(0,1),(1,2)]

def get_latest_points(points, k):
    sorted_points = sorted(points,key=lambda point:abs(point[0])+abs(point[1]))
    return sorted_points[:k]

print(get_latest_points(points,2))