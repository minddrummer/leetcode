# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
# Assume that the total area is never beyond the maximum possible value of int.




class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    # def rect_Area(self, A,B,C,D):
    #     return abs(A-C) * abs(B-D)

    # def overlap(self, A, B, C, D, E, F, G, H):
    #     directx1 = sorted([A,C])
    #     directy1 = sorted([B,D])
    #     directx2 = sorted([E,G])
    #     directy2 = sorted([F,H])
    #     overlap = True
    #     if directx1[1] <= directx2[0] or directx2[1] <= directx1[0]:
    #         overlap = False   
    #     if directy1[1] <= directy2[0] or directy2[1] <= directy1[0]:
    #         overlap = False  
    #     return overlap

    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = abs(A-C) * abs(B-D) #self.rect_Area(A,B,C,D)
        area2 = abs(E-G) * abs(F-H) #self.rect_Area(E,F,G,H)
        directx1 = sorted([A,C])
        directy1 = sorted([B,D])
        directx2 = sorted([E,G])
        directy2 = sorted([F,H])
        overlap = True
        if directx1[1] <= directx2[0] or directx2[1] <= directx1[0]:
            overlap = False   
        if directy1[1] <= directy2[0] or directy2[1] <= directy1[0]:
            overlap = False
        if overlap:
            '''donot have to know the exact relation, but the length for the overlapping, right?'''
            x_cor = sorted(directx1 + directx2)
            x_len = x_cor[2] - x_cor[1]
            y_cor = sorted(directy1 + directy2)
            y_len = y_cor[2] - y_cor[1]
            return area1 + area2 - x_len*y_len
        else:
            return area1+area2



if __name__ == '__main__':
    test = Solution()
    print test.computeArea()        