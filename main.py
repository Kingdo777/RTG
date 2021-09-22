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
        # self.fitLevel.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]")))
        self.t_15.setValidator(QtGui.QIntValidator())
        self.t0.setValidator(QtGui.QIntValidator())
        self.t30.setValidator(QtGui.QIntValidator())
        self.t60.setValidator(QtGui.QIntValidator())
        self.t90.setValidator(QtGui.QIntValidator())
        self.t120.setValidator(QtGui.QIntValidator())
        self.t180.setValidator(QtGui.QIntValidator())
        self.t240.setValidator(QtGui.QIntValidator())
        self.bg_15.setValidator(QtGui.QDoubleValidator())
        self.bg0.setValidator(QtGui.QDoubleValidator())
        self.bg30.setValidator(QtGui.QDoubleValidator())
        self.bg60.setValidator(QtGui.QDoubleValidator())
        self.bg90.setValidator(QtGui.QDoubleValidator())
        self.bg120.setValidator(QtGui.QDoubleValidator())
        self.bg180.setValidator(QtGui.QDoubleValidator())
        self.bg240.setValidator(QtGui.QDoubleValidator())
        self.gfr.setValidator(QtGui.QDoubleValidator())
        self.uge.setValidator(QtGui.QDoubleValidator())
        # 绑定事件
        self.Clean_PushButton.clicked.connect(self.on_button_clean)
        self.Reset_PushButton.clicked.connect(self.on_button_reset)
        self.RTG_PushButton.clicked.connect(self.on_button_RTG)
        # 第五步：定义MyFigure类的一个实例
        self.F = MyFigure(width=3, height=2, dpi=100)
        # 第六步：在GUI的groupBox中创建一个布局，用于添加MyFigure类的实例（即图形）后其他部件。
        self.gridlayout = QGridLayout(self.groupBox)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)
        # 拟合函数
        self.fit_func = []
        self.t = []
        self.bg = []

    def getData(self):
        t_label = [
            self.t_15.text(),
            self.t0.text(),
            self.t30.text(),
            self.t60.text(),
            self.t90.text(),
            self.t120.text(),
            self.t180.text(),
            self.t240.text()
        ]
        bg_label = [
            self.bg_15.text(),
            self.bg0.text(),
            self.bg30.text(),
            self.bg60.text(),
            self.bg90.text(),
            self.bg120.text(),
            self.bg180.text(),
            self.bg240.text()
        ]
        self.t = []
        self.bg = []
        data = []
        for i in range(8):
            if is_number(t_label[i]) and \
                    is_number(bg_label[i]) and \
                    24 * 60 >= int(t_label[i]) >= -24 * 60 and \
                    0 <= float(bg_label[i]) <= 1000.0:
                data.append((int(t_label[i]), float(bg_label[i])))
        data.sort(key=lambda x: x[0])
        print(t_label)
        print(bg_label)
        print(data)
        for d in data:
            self.t.append(d[0])
            self.bg.append(d[1])

    def plot(self):
        self.fit_func = []
        self.F.axes.clear()
        self.F.axes.set_ylim(min(self.bg)-10, max(self.bg)+10)
        self.F.axes.set_xlim(min(self.t)-5, max(self.t)+5)
        x = self.t
        y = self.bg
        for i in range(len(x) - 1):
            self.fit_func.append(poly1d(polyfit(x[i:i + 2], y[i:i + 2], 1)))
        self.F.axes.plot(x, y, 'ks-')
        self.gridlayout.addWidget(self.F, 0, 1)
        self.F.draw()

    def on_button_reset(self, evt):
        self.t_15.setText("-15")
        self.t0.setText("0")
        self.t30.setText("30")
        self.t60.setText("60")
        self.t90.setText("90")
        self.t120.setText("120")
        self.t180.setText("180")
        self.t240.setText("240")
        self.bg_15.setText("158")
        self.bg0.setText("156")
        self.bg30.setText("195")
        self.bg60.setText("225")
        self.bg90.setText("235")
        self.bg120.setText("225")
        self.bg180.setText("200")
        self.bg240.setText("160")

    def on_button_clean(self, evt):
        self.bg_15.clear()
        self.bg0.clear()
        self.bg30.clear()
        self.bg60.clear()
        self.bg90.clear()
        self.bg120.clear()
        self.bg180.clear()
        self.bg240.clear()
        self.F.axes.clear()
        self.F.draw()
        self.RTG_label.setText("我被清空了呢")

    def getIntegrateVal(self, rtg):
        gfr = float(self.gfr.text())
        x = self.t
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

    def on_button_RTG(self, evt):
        if not is_number(self.gfr.text()):
            self.RTG_label.setText("GRF 不是合法的值")
            return
        if not is_number(self.uge.text()):
            self.RTG_label.setText("UGE 不是合法的值")
            return
        self.getData()
        if len(self.t) < 2:
            self.RTG_label.setText("数据太少")
            return
        self.plot()
        uge = float(self.uge.text())
        maxRTG, minRTG = max(self.bg), 0
        rtg, tmp = 0, 0
        print("BG info : ", str(self.bg))
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
