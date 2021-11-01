import pandas as pd


class Muscle:
    def __init__(self, muscle_name, muscle_point_list, color):
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
        return str(self.muscle_name) + " (" + str(self.color[0]) + "," + str(self.color[1]) + "," + str(self.color[2]) + "): " + points_str


muscle_list = [
    Muscle("musculo 1", [1, 2, 3, 4, 5, 6, 7, 8, 9], (255, 0, 0)),
    Muscle("musculo 2", [10, 11, 12, 13, 14, 15], (0, 0, 255)),
    Muscle("musculo 3", [25, 90], (69, 0, 255)),
    Muscle("GHJK 4", [60, 42], (11, 99, 11)),
    Muscle("musc 5", [70, 142, 420], (0, 99, 110)),
    Muscle("musc 9", [99, 31], (100, 99, 110))
]


def get_muscles_from_csv():
    df = pd.read_csv("./muscles.csv")
    ms_list = []
    for i in range(0, len(df)):
        pts = df["points"][i].split(",")
        pts_int = []
        for j in range(len(pts)):
            if(pts[j] != ''):
                pts_int.append(int(pts[j]))

        col = df["color"][i].split(',')
        ms_list.append(
            Muscle(
                df["name"][i],
                pts_int,
                (int(col[0].split("(")[1]), int(
                    col[1]), int(col[2].split(")")[0]))
            )
        )
    return ms_list


def save_csv():
    names = []
    points = []
    colors = []
    for muscle in muscle_list:
        names.append(muscle.muscle_name)
        pts = ""
        for pt in muscle.muscle_points:
            pts = pts + str(pt) + ","
        points.append(pts)
        colors.append(muscle.color)
    df = pd.DataFrame()
    df["name"] = names
    df["points"] = points
    df["color"] = colors

    df.to_csv("muscles.csv")


if __name__ == "__main__":
    save_csv()
