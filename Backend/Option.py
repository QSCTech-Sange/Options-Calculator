import scipy.stats as sps
import numpy as np


class Option:

    # european 为 欧式期权 (False 为欧式期权)
    # kind 看涨或看跌（Put 为 -1 , Call 为 1）
    # s0 标的资产现价
    # k 期权执行价
    # t 期权到期时间 - 现在时间
    # r 适用的无风险利率
    # sigma 适用的波动率
    # dv 股利信息（本例中使用连续股利率dv）
    # d1 和 d2 是 BSM 定价过程中需要用到的参数
    def __init__(self, european, kind, s0, k, t, r, sigma, dv):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t
        self.sigma = sigma
        self.r = np.log(1 + r)
        self.dv = np.log(1 + dv)
        # 计算二叉树需要的
        self.tree = None
        self.delta = None
        self.u = None
        self.d = None
        self.p = None

    # B-S-M 计算价格方法
    def bsprice(self):
        if self.european or self.kind == 1:
            d_1 = (np.log(self.s0 / self.k) + (
                    self.r - self.dv + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                self.t)
            d_2 = d_1 - self.sigma * np.sqrt(self.t)
            return self.kind * self.s0 * np.exp(-self.dv * self.t) * sps.norm.cdf(
                self.kind * d_1) - self.kind * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d_2)
        else:
            return "美式看跌期权不适合这种计算方法"

    # 蒙特卡罗定价
    def mcprice(self, iteration):
        if self.european or self.kind == 1:
            zt = np.random.normal(0, 1, iteration)
            st = self.s0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.t + self.sigma * self.t ** .5 * zt)
            p = []
            for St in st:
                p.append(max(self.kind * (St - self.k), 0))
            return np.average(p) * np.exp(-self.r * self.t)
        else:
            return "美式看跌期权不适合这种计算方法"

    # 二叉树定价
    def bt(self, iteration):
        if iteration % 2 != 0:
            iteration += 1
        self.delta = self.t / iteration
        self.u = np.exp(self.sigma * np.sqrt(self.delta))
        self.d = 1 / self.u
        self.p = (np.exp((self.r - self.dv) * self.delta) - self.d) / (self.u - self.d)
        self.tree = []
        for j in range(int(iteration / 2) + 1):
            i = j * 2
            temp = self.s0 * np.power(self.u, iteration - i)
            temp = np.max([(temp - self.k) * self.kind, 0])
            self.tree.append(temp)
        for j in range(1, int(iteration / 2) + 1):
            i = j * 2
            temp = self.s0 * np.power(self.d, i)
            temp = np.max([(temp - self.k) * self.kind, 0])
            self.tree.append(temp)
        for j in range(0, iteration):
            # 每一层的最高幂次
            k = iteration - j - 1
            newtree = []
            for i in (range(len(self.tree) - 1)):
                temp = self.tree[i] * self.p + (1 - self.p) * self.tree[i + 1]
                temp = temp * np.exp(-self.r * self.delta)
                if not self.european:
                    if i < (k + 1) / 2:
                        power = k - i * 2
                        compare = self.s0 * np.power(self.u, power)
                    else:
                        power = i * 2 - k
                        compare = self.s0 * np.power(self.d, power)
                    temp = np.max([temp, (compare - self.k) * self.kind])
                newtree.append(temp)
            self.tree = newtree
        return self.tree[0]
