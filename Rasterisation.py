import numpy as np 

print("Entrer les coordonnees du point A :")

xA = int(input("xA="))
yA = int(input("yA="))
zA = int(input("zA="))
wA = 1

aCoordonates = np.array([ [xA], [yA], [zA], [wA] ])

print("Les coordonnées du point A sont :", "\n", aCoordonates)

# Transformation Matrix

#Scale Matrix

xScaleCoef = int(input("xScaleCoef="))
yScaleCoef = int(input("yScaleCoef="))
zScaleCoef = int(input("zScaleCoef="))

scaleMatrix = np.array([ [xScaleCoef, 0, 0, 0], [0, yScaleCoef, 0, 0], [0, 0, zScaleCoef, 0], [0, 0, 0, 1] ])

print("La matrice de dilatation est :", "\n", scaleMatrix)
aNewCoordonates = np.dot(scaleMatrix, aCoordonates)
print("Les coordonnées du point A sont :", "\n", aNewCoordonates)

#Rotation Matrix

xRotationAngle = int(input("xRotationAngle="))
yRotationAngle = int(input("yRotationAngle="))
zRotationAngle = int(input("zRotationAngle="))

xRotationAngleRadians = np.radians(xRotationAngle)
yRotationAngleRadians = np.radians(yRotationAngle)
zRotationAngleRadians = np.radians(zRotationAngle)

# X Rotation Matrix

xRotationMatrix = np.array([ [1, 0, 0, 0], [0, np.cos(xRotationAngleRadians), np.sin(xRotationAngleRadians), 0], [0, -np.sin(xRotationAngleRadians), np.cos(xRotationAngleRadians), 0], [0, 0, 0, 1] ])

print("La matrice de rotation de X est :", "\n", np.around(xRotationMatrix))
aNewCoordonates = np.dot(xRotationMatrix, aNewCoordonates)
print("Les coordonnées du point A sont :", "\n", np.around(aNewCoordonates))

# Y Rotation Matrix

yRotationMatrix = np.array([ [np.cos(yRotationAngleRadians), 0, -np.sin(yRotationAngleRadians), 0], [0, 1, 0, 0], [np.sin(yRotationAngleRadians), 0, np.cos(yRotationAngleRadians), 0], [0, 0, 0, 1] ]) 

print("La matrice de rotation de Y est :", "\n", np.around(yRotationMatrix))
aNewCoordonates = np.dot(yRotationMatrix, aNewCoordonates)
print("Les coordonnées du point A sont :", "\n", np.around(aNewCoordonates))

# Z Rotation Matrix

zRotationMatrix = np.array([ [np.cos(zRotationAngleRadians), np.sin(zRotationAngleRadians), 0, 0], [-np.sin(zRotationAngleRadians), np.cos(zRotationAngleRadians), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ])

print("La matrice de rotation de Z est :", "\n", np.around(zRotationMatrix))
aNewCoordonates = np.dot(zRotationMatrix, aNewCoordonates)
print("Les coordonnées du point A sont :", "\n", np.around(aNewCoordonates))

#Translation Matrix

xTranslationCoef = int(input("xTranslationCoef="))
yTranslationCoef = int(input("yTranslationCoef="))
zTranslationCoef = int(input("zTranslationCoef="))

translationMatrix = np.array([ [1, 0, 0, xTranslationCoef], [0, 1, 0, yTranslationCoef], [0, 0, 1, zTranslationCoef], [0, 0, 0, 1] ])

print("La matrice de translation est :", "\n", translationMatrix)
aNewCoordonates = np.dot(translationMatrix, aNewCoordonates)
print("Les coordonnées du point A sont :", "\n", np.around(aNewCoordonates))