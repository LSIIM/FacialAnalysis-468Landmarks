import cv2
import mediapipe as mp


class FaceMeshDetector():
    def __init__(self,
        staticImageMode=False,
        maxNumFaces=2,
        minDetectionConfidence=0.5,
        minTrackingConfidence=0.5):
        self.staticImageMode=bool(staticImageMode)
        self.maxNumFaces=int(maxNumFaces)
        self.minDetectionConfidence=float(minDetectionConfidence)
        self.minTrackingConfidence=float(minTrackingConfidence)

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh

        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces =self.maxNumFaces ,min_detection_confidence =self.minDetectionConfidence, static_image_mode = self.staticImageMode,min_tracking_confidence = self.minTrackingConfidence )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness = 1, circle_radius = 2)
    
    def findFaceMesh(self,img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.faceMesh.process(imgRGB)
        faces = []
        if results.multi_face_landmarks:
            for faceLms in results.multi_face_landmarks:
                face = []
                #print(faceLms)
                for i,lm in enumerate(faceLms.landmark):
                    ih,iw,ic = img.shape
                    x,y = int(lm.x*iw),int(lm.y*ih)
                    
                    #print(i,x,y)
                    face.append((x,y))
                faces.append(face)
        return img,faces