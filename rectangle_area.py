# Link: https://leetcode.com/problems/rectangle-area/


def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        
        def area (x1, y1, x2, y2):
        
            if y1 > y2 or x1 > x2:
                return 0
            
            return (x2-x1) * (y2-y1)
        
        r1_area = area (ax1, ay1, ax2, ay2)
        r2_area = area (bx1, by1, bx2, by2)
        
        
        left_overlap = max (ax1, bx1)
        up_overlap = min (ay2, by2)
        
        down_overlap = max (ay1, by1)
        right_overlap = min (ax2, bx2)
        
        overlap_area = area(left_overlap, down_overlap, right_overlap, up_overlap)
        
        return r1_area + r2_area - overlap_area