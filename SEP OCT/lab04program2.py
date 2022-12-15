#centriod , orthocenter , incenter , circumcenter 
print("Enter coordinates of three points")
ax=int(input("X coordinates of point 1:"))
ay=int(input("Y coordinates of point 1:"))
bx=int(input("X coordinates of point 2:"))
by=int(input("Y coordinates of point 2:"))
cx=int(input("X coordinates of point 3:"))
cy=int(input("Y coordinates of point 3:"))
s=ax*(by-cy)+bx*(cy-ay)+cx*(ay-by)
if s==0:
    print("The given points are colliner")
    centroidx=(ax+bx+cx)/3
    centroidy=(ay+by+cy)/3
    print("Centroid of the triangles are ",centroidx,centroidy,sep='')
else:
    print("The given points are not colliner")
    centroidx=(ax+bx+cx)/3
    centroidy=(ay+by+cy)/3
    print("Centroid of the triangles are ",centroidx,centroidy,sep='')

