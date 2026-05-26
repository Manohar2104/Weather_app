import matplotlib.pyplot as plt


def compare_param(list1, list2,param):
    plt.barh(list1, list2,height=0.7)
    plt.xlabel(param)
    plt.show()

#compare_param(['Mumbai', 'delhi'], [6.28,6.58],"Temperature")
