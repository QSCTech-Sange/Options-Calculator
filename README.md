# Options Calculator

这是一个全能的期权计算器，涵盖 BS法，蒙特卡洛法，二叉数法，能够对看涨期权，看跌期权，欧式期权，美式期权，有股利期权，无股利期权进行定价，并附带GUI客户端。

本计算器的**特色**在于

1. 支持非常全面的期权类型
2. 美观优雅简洁大方的界面
3. 可以直接提取使用其中的 `Option` 类来应用于你所需要的计算期权价格的地方。
4. 可以指定具体日期而不用再手动算时间间隔
5. 可以直接输入一年计无风险利率而不用用户计算连续复利

> 以上两点直接将 Options Calculator 从普通的学术研究计算器拉到了普世的，实用的价值层面。广度层面的延伸。

5. 可以比较观察不同方法的计算结果差异
6. 可以手动指定二叉树方法和蒙特卡罗方法的迭代次数，更好地理解期权定价。

> 以上两点深化了 Options Calculator 的学术研究价值意义。深度层面的加强。



## 功能介绍

![welcome](img/welcome.png)

主界面采用流行的左右布局，左侧是 LOGO 和 六个 Tab 标签功能页，右侧为每一个标签页对应的主界面。默认在第一个 Tab 下，即欢迎光临。因为还没有输入参数，因此无法查看价格，第三个标签是禁止的。

![input](img/input.png)

在输入参数界面，涵盖了有关期权的一些参数录入。首先是当前日期，默认会设置今天的日期，可以指定往期日期。这里点击后会调用一个日历格式。到期日期默认为当前日期的后十天。然后有美式欧式和看涨看跌的选项，只提供两种选择。最后是标的资产现价，期权执行价，波动率，一年单利计无风险利率，一年单利计股息利率的输入。这里会默认提供一些，以便用户想直接看结果。波动率，无风险利率，股息利率都是结尾是%的，即如果用户要输入 5%，只要输入5即可。在其他期权计算器中往往都是让用户直接输入无风险利率，而我们这里要求用户需要输入的是一年单利计利率，将转换交给了计算器本身。最后可以指定蒙特卡罗迭代次数和二叉树次数，也可以使用默认的设定。

![result](img/result.png)

当点击确定输入后，会弹出提示框让用户等待，并在完成后自动跳转到查看价格的 Tab。可以观察三种方法的计算结果。

![1559705817688](img/list.png)

算法一览直(tou)接(lan)进入MBA的网页界面。

![img](img/about.png)

关于我们。

![quit](img/quit.png)

再见页面。



## 编译方法

项目依赖于 `Python3`以及下列Python包：`numpy`,`pyqt5`,`qtawesome` 和 `scipy`。

安装完 python 后可进入项目目录通过以下指令安装缺少的包。

```shell
pip install requirements.txt
```



1. 在 [本页面](<https://github.com/QSCTech-Sange/Options-Calculator>) 下载此仓库，并解压
2. 在终端中输入

```shell
cd 到刚刚解压的目录
cd Frontend
chmod a+x main.py
python main.py
```

即可。



## 项目结构

本项目总共621行，结构如下：

```shell
.
├── Backend
│   ├── __init__.py
│   ├── Option.py
├── Frontend
│   ├── about.py
│   ├── img
│   │   ├── background_2.png
│   │   ├── background_3.png
│   │   ├── background.png
│   │   ├── hint.png
│   │   └── logo2.png
│   ├── input.py
│   ├── list.py
│   ├── main.py
│   ├── page.py
│   ├── quit.py
│   ├── result.py
│   ├── style.qss
│   └── welcome.py
├── img
│   ├── about.png
│   ├── input.png
│   ├── list.png
│   ├── quit.png
│   ├── result.png
│   └── welcome.png
├── README.md
└── requirements.txt

```

项目分为前端和后端，前端在` Frontend` 文件夹里，后端在 `Backend` 文件夹里。`README.md` 即本文件。根目录下 `img` 里的文件只是为了本文档的渲染而已，忽略即可。 `requirements.txt` 记录了项目的依赖。

### 后端

后端里有`__init__.py` 和 `option.py`。 前者仅仅只是为了前端导入所必要的文件，其内容为空。

而 `Option.py` 是核心，有一个 `option` 类，内含期权的数据和计算价格的方法。可以打开阅读，有详尽的注释。我们需要 `numpy` 来计算`ndarray`列表和生成随机数，需要`scipy` 来计算正态分布分布函数。内置了 B-S 算法，蒙特卡罗算法和二叉树算法。

### 前端

前端基于`Qt`的主框架，主界面在 `main.py` 里，需要 `qtawesome`来绘制图标。`page.py`是一个单独页面的基础。

`welcome.py` `input.py` `result.py` `list.py` `about.py` `quit.py`  分别对应欢迎页面，输入页面，结果页面，算法一览页面和退出页面。`style.qss` 是样式，定义了一些诸如哪些按钮应该长什么样等等。此目录里的 img  里的文件是绘制界面需要用的一些图片。



## 算法详解

### Option 类

`european` 为是否是欧式期权 (False 为欧式期权)
`kind` 看涨或看跌（`Put` 为 -1 ,` Call` 为 1）
`s0` 标的资产现价
`k` 期权执行价
`t` 期权到期时间 - 现在时间
`r` 适用的无风险利率
`sigma` 适用的波动率
`dv` 股利利率

```python
class Option:
  
    def __init__(self, european, kind, s0, k, t, r, sigma, dv):
        self.european = european
        self.kind = kind
        self.s0 = s0
        self.k = k
        self.t = t
        self.sigma = sigma
        self.r = np.log(1 + r)
        self.dv = np.log(1 + dv)
```

这里认为传递给期权的构造函数的无风险利率和股利利率都是一年计利率，我们在构造时将其计算为连续复利。

### B-S-M 计算方法

因为涉及到了股利利率，所以严格来说不是BS算法而是BSM算法。

```python
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
```

BSM 算法本身只能用于**欧式期权**，由于美式看涨期权和欧式看涨期权价格相等，因此我们将扩展到仅仅是**不能计算美式看跌期权**。

其中我们算了d1 和 d2 它们是用于最终计算的中间变量。涉及到有股利情况下，它们是
$$
d_1 = \frac{ln\frac{S0}{k} + (r+ 0.5 \cdot \sigma^2 - dv)t}{\sigma \cdot \sqrt{t}}
$$

$$
d_2 = d_1 - \sigma \sqrt{t}
$$

而看涨期权（涉及股利）的价格为
$$
P = S_0 \cdot e^{-dv \cdot t} \cdot N(d_1) - k \cdot e^{-rt}N(d_2)
$$
看跌期权的价格就是
$$
P = ke^{-rt}[1-N(d_2)] - S_0[1-N(d_1)]
$$
这里运用了一些小技巧，将kind表示成一个flag标记，使得同一个式子能应用于看涨看跌两种情况。注意
$$
N(d) = 1 - N(-d)
$$
这是我们的公式能正确运行的原因。



### 蒙特卡罗模拟计算方法

蒙特卡罗算法本身只能用于**欧式期权**，由于美式看涨期权和欧式看涨期权价格相等，因此我们将扩展到仅仅是**不能计算美式看跌期权**。

蒙特卡洛模拟计算方法需要指定迭代次数iteration。

注意我们生成的 `zt` 是一个列表，不是一个单一的值，它的所有值的分布符合一个标准正态分布，总共有iteration个值，它代表波动的上涨或下跌。

接下来我们根据这个公式
$$
st = s0 * e^{(r-dv-0.5*\sigma^2)*t + \sigma *t ^{0.05}*zt}
$$
来计算最终价值，这里根据迭代次数生成了迭代次数个最终价值。这些最终价值要根据看涨或看跌进行 k- x 或者 x-k 的处理，并取处理后和0相比的较大值。

我们计算这些最终价值的平均值，再贴现到当前日期。贴现是指原价值乘以e^(-r*t)

```python
# 蒙特卡罗定价
def mcprice(self, iteration):
    if self.european or self.kind == 1:
        zt = np.random.normal(0, 1, iteration)
        st = self.s0 * np.exp((self.r - self.dv - .5 * self.sigma ** 2) * self.t + self.sigma * self.t ** .5 * zt)
        st = np.maximum(self.kind * (st - self.k), 0)
        return np.average(st) * np.exp(-self.r * self.t)
    else:
        return "美式看跌期权不适合这种计算方法"
```



### 二叉树计算方法

此方法最难，但是适用于所有期权，因此也最为必要。我们首先要计算u,d,p。u代表上涨，d代表下跌，p是一个风险中性概率。每一期可能上涨，也可能下跌，u,d即衡量上涨会涨的倍数和下跌会下跌的倍数。p即上涨的概率，1-p 是下跌的概率。从最开始的单一起点（标的资产价值）慢慢往未来推，可能上涨可能下降，下降后又可能上涨可能下降，这样子慢慢形成一棵二叉树。这时候二叉树的价格不是期权价值，是站在未来时间的估计现价。 而我们需要的是期权价格。

我们需要从树的叶子节点从后往前推导期权价值。举例来说，最后一步最上面节点的期权价值等于（n = 迭代次数），每一个节点类似，只是下面的节点需要将u替换成d，n以每个节点减少2的等差往下降。
$$
max(0,k-s_0u^n)
$$
这是看跌期权，看涨期权则为
$$
max(0,s_0u^n-k)
$$
这样我们得到了二叉树最后一层叶子节点的所有期权价值。

每次往前推的过程是这样，

n-1节点的期权价值等于n步对应的两个节点的风险中性概率加权再无风险利率贴现的值，（美式同时和提前行权的价值取较大值）。

举例来说，s0 u^500 和 s0 u^498的父节点是s0 u^499，它的期权价值等于

p *(500的节点的期权价值) * (1-p) *(499的节点的期权价值)  × 无风险利率贴现

无风险利率贴现就是 e^(-rt)

注意，如果是美式期权的话，这个价值还要和 k - s0 u^499 相比，（看涨是 s0 u^499 - k）取较大值。

这样一层层往前推，就推导到了我们的根节点，就是站在此时此刻的期权价值。

```python
# 二叉树定价
def bt(self, iteration):
    if iteration % 2 != 0:
        iteration += 1
    delta = self.t / iteration
    u = np.exp(self.sigma * np.sqrt(delta))
    d = 1 / u
    p = (np.exp((self.r - self.dv) * delta) - d) / (u - d)
    tree = []
    # 计算树的叶子结点
    for j in range(int(iteration / 2) + 1):
        i = j * 2
        temp = self.s0 * np.power(u, iteration - i)
        temp = np.max([(temp - self.k) * self.kind, 0])
        tree.append(temp)
    for j in range(1, int(iteration / 2) + 1):
        i = j * 2
        temp = self.s0 * np.power(d, i)
        temp = np.max([(temp - self.k) * self.kind, 0])
        tree.append(temp)
    # 每一次循环往前推一层，直到最上层
    for j in range(0, iteration):
        newtree = []
        for i in (range(len(tree) - 1)):
            temp = tree[i] * p + (1 - p) * tree[i + 1]
            temp = temp * np.exp(-self.r * delta)
            if not self.european:
                # k 是每一层的最高幂次
                k = iteration - j - 1
                if i < (k + 1) / 2:
                    power = k - i * 2
                    compare = self.s0 * np.power(u, power)
                else:
                    power = i * 2 - k
                    compare = self.s0 * np.power(d, power)
                temp = np.max([temp, (compare - self.k) * self.kind])
            newtree.append(temp)
        tree = newtree
    return tree[0]
```

