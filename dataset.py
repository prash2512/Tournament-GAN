import numpy as np
import matplotlib.pyplot as plt


class data_generator():
    def __init__(self):

        n = 8
        radius = 2
        std = 0.02
        delta_theta = 2*np.pi / n

        centers_x = []
        centers_y = []
        for i in range(n):
            centers_x.append(radius*np.cos(i*delta_theta))
            centers_y.append(radius*np.sin(i*delta_theta))

        centers_x = np.expand_dims(np.array(centers_x), 1)
        centers_y = np.expand_dims(np.array(centers_y), 1)

        p = [1./n for _ in range(n)]

        self.p = p
        self.size = 2
        self.n = n
        self.std = std
        self.centers = np.concatenate([centers_x, centers_y], 1)

    def sample(self, N):
        n = self.n
        std = self.std
        centers = self.centers
        ith_center = np.random.choice(n, N,p=self.p)
        sample_centers = centers[ith_center, :]
        sample_points = np.random.normal(loc=sample_centers, scale=std)
        return sample_points.astype('float32')

    
    def plot(self,points):
        plt.scatter(points[:, 0], points[:, 1], s=10, c='b', alpha=0.5)
        plt.scatter(self.centers[:, 0], self.centers[:, 1], s=100, c='g', alpha=0.5)
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.show()
        plt.close()

