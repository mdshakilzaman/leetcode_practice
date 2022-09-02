
from cv2 import solve


def validSquare( p1, p2, p3, p4):
    """
    :type p1: List[int]
    :type p2: List[int]
    :type p3: List[int]
    :type p4: List[int]
    :rtype: bool
    """
    import math
    def distance (p1, p2):
        
        dist = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
        dist = dist ** 0.5
        
        return dist
        
        #find poui
        
    points_list = [p1,p2,p3,p4]
    x_parallel = -1
    y_parallel = -1

    for i in range (1, 4):

        if points_list[0][0] == points_list[i][0]:
            #this is y_parallel point
            if y_parallel != -1:
                #we cannot two y_parallel points to a given point
                return False
            else:
                y_parallel = i

        elif points_list[0][1] == points_list[i][1]:
            if x_parallel != -1:
                return False
            else:
                x_parallel = i

    dist_p1_p2 = distance (p1, p2)
    dist_p1_p3 = distance (p1, p3)
    dist_p1_p4 = distance (p1, p4)

    if dist_p1_p2 == 0 or dist_p1_p3 == 0 or dist_p1_p4 == 0:
        return False

    if dist_p1_p2 == dist_p1_p3:
        
        dist_p4_p3 = distance (p4, p3)
        dist_p4_p2 = distance (p4, p2)
        
        if abs(dist_p1_p4 - 1.4142135623730951*dist_p1_p2) < 1e-9:
            if dist_p1_p2 == dist_p4_p3 == dist_p4_p2: 
                return True

    if dist_p1_p2 == dist_p1_p4:
        
        dist_p3_p2 = distance (p3, p2)
        dist_p3_p4 = distance (p3, p4)
        
        if abs(dist_p1_p3 - 1.4142135623730951*dist_p1_p2) < 1e-9:
            if dist_p1_p2 == dist_p3_p2 == dist_p3_p4:
                return True

    if dist_p1_p3 == dist_p1_p4:
        
        dist_p2_p3 = distance (p2, p3)
        dist_p2_p4 = distance (p2, p4)
        
        if abs(dist_p1_p2 - 1.4142135623730951*dist_p1_p3) < 1e-9:
            if dist_p1_p3 == dist_p2_p3 == dist_p2_p4:
                return True


    return False


if __name__ == "__main__":
    
    print (validSquare([0,1],[1,2],[0,2],[0,0]))