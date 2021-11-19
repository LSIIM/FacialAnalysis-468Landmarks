
from triangles import TRIANGLES


image = adjuster.getImg()
for lm in nlms:
    cv2.putText(image, str("."), lm, cv2.FONT_HERSHEY_PLAIN,
                0.8, (0, 255, 0), 1)

for tria in TRIANGLES:
    image = cv2.line(image, nlms[tria[0]],
                     nlms[tria[1]], (0, 0, 255), 1)
    image = cv2.line(image, nlms[tria[0]],
                     nlms[tria[2]], (0, 0, 255), 1)
    image = cv2.line(image, nlms[tria[1]],
                     nlms[tria[2]], (0, 0, 255), 1)

cv2.imshow("img", image)
cv2.waitKey(0)
