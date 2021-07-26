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
        self.ucg.setValidator(QtGui.QDoubleValidator())
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
        self.fit_func = 0

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
        self.fit_func = 0
        self.F.axes.clear()
        self.F.axes.set_ylim(140, 250)
        self.F.axes.set_xlim(-20, 260)
        x = [-15, 0, 30, 60, 90, 120, 180, 240]
        y = self.getBG()
        self.F.axes.plot(x, y, 'ks-')
        self.gridlayout.addWidget(self.F, 0, 1)
        self.F.draw()

    def on_button_fit(self, evt):
        self.F.axes.clear()
        self.F.axes.set_xlim(-20, 260)
        self.F.axes.set_ylim(140, 250)
        x = [-15, 0, 30, 60, 90, 120, 180, 240]
        y = self.getBG()
        self.fit_func = poly1d(polyfit(x, y, int(self.fitLevel.text())))
        self.F.axes.plot(x, y, 'ks-')
        cx = range(-15, 240)
        self.F.axes.plot(cx, self.fit_func(cx))
        self.gridlayout.addWidget(self.F, 0, 1)
        self.F.draw()

    def getIntegrateVal(self, rtg):
        gfr = float(self.gfr.text())
        sx = symbols('x')
        if type(self.fit_func) == int:
            x = [-15, 0, 30, 60, 90, 120, 180, 240]
            y = self.getBG()
            tmp = 0
            for i in range(0, 7):
                tmp += (y[i] + y[i + 1] - 2 * rtg) * (x[i + 1] - x[i]) / 2
            return tmp
        else:
            func = self.fit_func(sx) - rtg
            return gfr * integrate(func, (sx, -15, 240))

    def integrate(self, evt):
        if not is_number(self.gfr.text()):
            self.RTG_label.setText("GRF 不是合法的值")
            return
        if not is_number(self.ucg.text()):
            self.RTG_label.setText("UCG 不是合法的值")
            return
        ucg = float(self.ucg.text())
        maxRTG, minRTG = max(self.getBG()), 0
        rtg, tmp = 0, 0
        print("BG info : ", str(self.getBG()))
        print("GFR : ", float(self.gfr.text()))
        print("UCG : ", ucg)
        print("迭代计算开始：")

        for i in range(0, 50):
            rtg = (maxRTG + minRTG) / 2
            tmp = self.getIntegrateVal(rtg)
            print("第%d次迭代结果：rtg=" % (i + 1) + "%.3f 误差=" % rtg + "%.5f" % (tmp - ucg))
            if abs(tmp - ucg) < 0.0001:
                self.RTG_label.setText("TRG = " + '%.3f' % rtg + "(mg/dl)" + "\n误差为 %.5f" % (tmp - ucg))
                return
            if tmp > ucg:
                minRTG = rtg
            else:
                maxRTG = rtg
        self.RTG_label.setText("计算未达到精度要求\n结果为：%.3f " % rtg + "误差大小为 %.5f" % (tmp - ucg))


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
