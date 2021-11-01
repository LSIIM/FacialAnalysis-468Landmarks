from FaceMeshModule import FaceMeshDetector
import cv2
import muscles_identification as muscId
def detect_face_on_image(path):
    detector = FaceMeshDetector(maxNumFaces=1,minDetectionConfidence=0.9)
    name = path.split('/')
    name = name[len(name)-1].split('.')
    name = name[0]
    img = cv2.imread(path)
    img2,faces = detector.findFaceMesh(img,True)
    print(name)
    for face in faces:
        for i,lms in enumerate(face):
            achou = False
            for muscle in muscId.muscle_list:
                if(i in muscle.muscle_points):
                    achou = True
                    cv2.putText(img2,str(i),lms,cv2.FONT_HERSHEY_PLAIN,1.4,muscle.color,1)                        
                    break
            if(not achou):
                cv2.putText(img2,str(i),lms,cv2.FONT_HERSHEY_PLAIN,1.1,(0,255,0),1)


    cv2.putText(img2,"Legenda de cores",(100,300),cv2.FONT_HERSHEY_PLAIN,10,(0,0,0),3)           
    for i,muscle in enumerate(muscId.muscle_list):
        print(i)
        print(muscle)
        cv2.putText(img2,muscle.muscle_name,(100,500 + 200*i),cv2.FONT_HERSHEY_PLAIN,10,muscle.color,3) 
    cv2.imwrite(name+"-landmarks-colored.jpg",img2)
     
if __name__ == "__main__":
    detect_face_on_image("./human-muscles.jpg")