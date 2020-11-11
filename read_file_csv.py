import numpy as np


def read_file(path, type):
    """read the csv file and return the value of angle, sensor and time"""
    global n, sensor
    lst = np.loadtxt(path, delimiter=",", skiprows=0)
    rows, cols = np.shape(lst)
    angle = []
    if type == 'door':
        sensor = np.zeros((rows, cols-2))
        n = 2
    elif type == 'drawer':
        sensor = np.zeros((rows, cols-4))
        n = 4
    time = []
    j = 0
    for date in lst:
        sensor_cols = []
        angle.append(date[0])
        time.append(date[-1])
        for i in range(len(date)-n):
            sensor_cols.append(date[i+1])
        sensor[j, :] = sensor_cols
        j = j + 1
    return angle, sensor, time


if __name__ == '__main__':
    path = 'C:/Users/Haonan Yuan/Documents/Oregon state University/Python_workspace/Interface_door_PyQT/drawer_tests/trial_one_tests/trial_1/1.csv'
    angle, sensor, time = read_file(path, 'door')
    print(angle)
    print(np.shape(sensor))
    print(time)
