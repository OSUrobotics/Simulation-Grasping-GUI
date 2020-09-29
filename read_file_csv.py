import numpy as np

def read_file(path):

    list = np.loadtxt(open(path, "rb"), delimiter=",", skiprows=0)
    rows, cols = np.shape(list)
    angle = []
    sensor = np.zeros((rows, cols-2))
    time = []
    j = 0
    for date in list:
        sensor_cols = []
        angle.append(date[0])
        time.append(date[-1])
        for i in range(len(date)-2):
            sensor_cols.append(date[i+1])
        sensor[j, :] = sensor_cols
        j = j + 1
    return angle, sensor, time



if __name__ == '__main__':
    path = '/Door/1.csv'
    angle, sensor, time = read_file(path)
    print(angle)
    print(np.shape(sensor))
    print(time)