import scipy.stats as sps
import numpy as np


class Option:

    # european 为 欧式期权 (False 为欧式期权)
    # kind 看涨或看跌（Put 为 -1 , Call 为 1）
    # s0 标的资产现价
    # k 期权执行价
    # t 期权到期时间 - 现在时间,以天计
    # r 适用的无风险利率，连续复利
    # sigma 适用的波动率，
    # dv 股利信息，连续复利
    def __init__(self, european, kind, s0, k, t, r, sigma, dv):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t /365
        self.sigma = sigma
        self.r = r
        self.dv = dv
        self.bsprice = None
        self.mcprice = None
        self.btprice = None

    # B-S-M 计算价格方法
    def bs(self):
        if self.european or self.kind == 1:
            d_1 = (np.log(self.s0 / self.k) + (
                    self.r - self.dv + .5 * self.sigma ** 2) * self.t) / self.sigma / np.sqrt(
                self.t)
            d_2 = d_1 - self.sigma * np.sqrt(self.t)
            self.bsprice = self.kind * self.s0 * np.exp(-self.dv * self.t) * sps.norm.cdf(
                self.kind * d_1) - self.kind * self.k * np.exp(-self.r * self.t) * sps.norm.cdf(self.kind * d_2)
        else:
            self.bsprice = "美式看跌期权不适合这种计算方法"

    # 蒙特卡罗定价
    def mc(self, iteration):
        if self.european or self.kind == 1:
            zt = np.random.normal(0, 1, iteration)
            st = self.s0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.t + self.sigma * self.t ** .5 * zt)
            st = np.maximum(self.kind * (st - self.k), 0)
            self.mcprice = np.average(st) * np.exp(-self.r * self.t)
        else:
            self.mcprice = "美式看跌期权不适合这种计算方法"

    # 二叉树定价
    def bt(self, iteration):
        delta = self.t / iteration
        u = np.exp(self.sigma * np.sqrt(delta))
        d = 1 / u
        p = (np.exp((self.r - self.dv) * delta) - d) / (u - d)
        
        tree = np.arange(0,iteration * 2 + 2,2,dtype=np.float128)
        tree[iteration//2 + 1:] = tree[:(iteration+1)//2][::-1]
        np.multiply(tree,-1,out=tree)
        np.add(tree,iteration,out=tree)
        np.power(u,tree[:iteration//2],out=tree[:iteration//2])
        np.power(d,tree[iteration//2:],out=tree[iteration//2:])
        np.maximum((self.s0 * tree - self.k) * self.kind,0,out=tree)

        for j in range(iteration):
            newtree = tree[:-1] * p + tree[1:] * (1 - p)
            newtree = newtree * np.exp(-self.r * delta)
            if not self.european:
                compare = np.abs(iteration - j - 1 - np.arange(tree.size - 1) * 2).astype(np.float128)
                np.power(u,compare[:len(compare)//2],out=compare[:len(compare)//2])
                np.power(d,compare[len(compare)//2:],out=compare[len(compare)//2:])
                np.multiply(self.s0,compare,out=compare)
                np.subtract(compare,self.k,out=compare)
                np.multiply(compare,self.kind,out=compare)
                np.maximum(newtree, compare,out=newtree)
            tree = newtree
        self.btprice = tree[0]
