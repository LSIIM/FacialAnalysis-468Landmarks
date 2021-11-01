class Muscle:
    def __init__(self,muscle_name,muscle_point_list,color):
        self.muscle_name = muscle_name
        self.muscle_points = muscle_point_list
        self.color = color
    def __str__(self):
        points_str = "["
        for point in self.muscle_points:
            points_str = points_str + str(point)
            if(point != self.muscle_points[len(self.muscle_points) - 1]):
                points_str = points_str + ","
            else:
                points_str = points_str + "]"
        return str(self.muscle_name) + " ("+ str(self.color[0]) + ","+ str(self.color[1]) + ","+ str(self.color[2])+ "): " + points_str
muscle_list = [
    Muscle("musculo 1",[1,2,3,4,5,6,7,8,9],(255,0,0)),
     Muscle("musculo 2",[10,11,12,13,14,15],(0,0,255))
]