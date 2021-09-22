# -*-coding:utf-8-*-
import sys

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QGridLayout
from numpy import polyfit, poly1d
from sympy import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import RTG
import matplotlib

matplotlib.use("Qt5Agg")  # 声明使用QT5


# 创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        # 第一步：创建一个创建Figure
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        # 第二步：在父类中激活Figure窗口
        super(MyFigure, self).__init__(self.fig)  # 此句必不可少，否则不能显示图形
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，如matlab的subplot(1,1,1)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_ylim(140, 250)
        self.axes.set_xlim(-20, 260)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


class ExampleApp(QtWidgets.QMainWindow, RTG.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)
        # 设置输入文本框的格式
        self.fitLevel.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[1-9]")))
        self.t_15.setValidator(QtGui.QDoubleValidator())
        self.t0.setValidator(QtGui.QDoubleValidator())
        self.t30.setValidator(QtGui.QDoubleValidator())
        self.t60.setValidator(QtGui.QDoubleValidator())
        self.t90.setValidator(QtGui.QDoubleValidator())
        self.t120.setValidator(QtGui.QDoubleValidator())
        self.t180.setValidator(QtGui.QDoubleValidator())
        self.t240.setValidator(QtGui.QDoubleValidator())
        self.gfr.setValidator(QtGui.QDoubleValidator())
        self.uge.setValidator(QtGui.QDoubleValidator())
        # 绑定事件
        self.plotPushButton.clicked.connect(self.on_button_plot)
        self.fitPushButton.clicked.connect(self.on_button_fit)
        self.RTG_PushButton.clicked.connect(self.integrate)
        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        # 拟合函数
        self.fit_func = []

    def getBG(self):
        return [
            float(self.t_15.text()),
            float(self.t0.text()),
            float(self.t30.text()),
            float(self.t60.text()),
            float(self.t90.text()),
            float(self.t120.text()),
            float(self.t180.text()),
            float(self.t240.text())
        ]

    def on_button_plot(self, evt):
        self.fit_func = []
        self.F.axes.clear()
        self.F.axes.set_ylim(140, 250)
        self.F.axes.set_xlim(-20, 260)
        x = [-15, 0, 30, 60, 90, 120, 180, 240]
        y = self.getBG()
        for i in range(len(x) - 1):
            self.fit_func.append(poly1d(polyfit(x[i:i + 2], y[i:i + 2], 1)))
        self.F.axes.plot(x, y, 'ks-')
        self.gridlayout.addWidget(self.F, 0, 1)
        self.F.draw()

    def on_button_fit(self, evt):
        self.F.axes.clear()
        self.F.axes.set_xlim(-20, 260)
        self.F.axes.set_ylim(140, 250)
        x = [-15, 0, 30, 60, 90, 120, 180, 240]
        y = self.getBG()

    def getIntegrateVal(self, rtg):
        gfr = float(self.gfr.text())
        x = [-15, 0, 30, 60, 90, 120, 180, 240]
        tmp = 0.0
        sx = symbols('x')
        for i in range(len(x) - 1):
            up_side = self.fit_func[i](x[i]) - rtg  # 上底
            down_side = self.fit_func[i](x[i + 1]) - rtg  # 下底
            high = x[i + 1] - x[i]
            if (up_side * down_side) > 0:
                if up_side > 0:
                    tmp += ((up_side + down_side) * high / 2)
            else:
                result = solve(self.fit_func[i](sx) - rtg, sx)[0]
                if up_side > 0:
                    high = result - x[i]
                    tmp += ((up_side + 0) * high / 2)
                else:
                    high = x[i + 1] - result
                    tmp += ((0 + down_side) * high / 2)
        return tmp * gfr

    def integrate(self, evt):
        if not is_number(self.gfr.text()):
            self.RTG_label.setText("GRF 不是合法的值")
            return
        if not is_number(self.uge.text()):
            self.RTG_label.setText("UGE 不是合法的值")
            return
        uge = float(self.uge.text())
        maxRTG, minRTG = max(self.getBG()), 0
        rtg, tmp = 0, 0
        print("BG info : ", str(self.getBG()))
        print("GFR : ", float(self.gfr.text()))
        print("UGE : ", uge)
        print("迭代计算开始：")

        for i in range(0, 50):
            rtg = (maxRTG + minRTG) / 2
            tmp = self.getIntegrateVal(rtg)
            print("第{}次迭代结果：rtg={} fake_uge={} 误差={}".format(i + 1, rtg, tmp, tmp - uge))
            if abs(tmp - uge) < 0.0001:
                self.RTG_label.setText("RTG = " + '%.3f' % rtg + "(mg/dl)" + "\n误差为 %.5f" % (tmp - uge))
                return
            if tmp > uge:
                minRTG = rtg
            else:
                maxRTG = rtg
        self.RTG_label.setText("计算未达到精度要求\n结果为：%.3f " % rtg + "误差大小为 %.5f" % (tmp - uge))


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
