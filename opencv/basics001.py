import cv2

img=cv2.imread(r"C:\Users\Arman\Pictures\Screenshots\Screenshot 2025-10-16 083355.png")

if img is None:
    print("image not loading")

else:
    cv2.imshow("image is being shown",img)          # opens the window
    cv2.waitKey(0)                                  # waits for a key 
    cv2.destroyallwindows()                         # closes the windows



