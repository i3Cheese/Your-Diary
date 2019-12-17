import sqlite3
from datetime import datetime

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor
from ui_diagram import Ui_Diagramm


class DiagramWidget(QWidget, Ui_Diagramm):
    def __init__(self, parent):
        super().__init__()
        self.prnt = parent
        self.data_base = self.prnt.data_base
        self.category_id = self.prnt.category_id
        self.do_draw = False

        super().setupUi(self)
        self.setWindowTitle(f'{self.prnt.title} - Диаграмма')
        self.listWidget.editable = False
        self.reload()

        # Настраиваем отрисовку диаграммы
        def paintEvent(a0) -> None:
            nonlocal self
            qp = QPainter()
            qp.begin(self.frame)
            self.drawDiagram(qp)
            qp.end()

        self.frame.paintEvent = paintEvent

        # Диаграмма перерисовывается при каждом изменении даты
        self.dteStart.dateTimeChanged.connect(self.frame.update)
        self.dteEnd.dateTimeChanged.connect(self.frame.update)

    def reload(self):
        start, end = self.prnt.getTimeBorders()
        self.dteStart.setDateTime(start)
        self.dteEnd.setDateTime(end)
        self.listWidget.reload()

    def getStatistic(self, start: datetime, end: datetime):
        notes = self.prnt.loadNotes()
        flags_time = {el: 0 for el in self.loadFlagsId()}
        flags_time[-1] = 0
        cnt = 0
        for note in notes:
            # начало и конец записи
            s, f = datetime.fromisoformat(note[1]), datetime.fromisoformat(note[2])
            s, f = max(s, start), min(f, end)
            if s >= f:
                continue
            td = (f - s).total_seconds()
            cnt += td
            if note[4]:
                flags_time[note[4]] += td
            else:
                flags_time[-1] += td
        return cnt, flags_time

    def getColor(self, flag_id: int):
        if flag_id == -1:
            return QColor(50, 50, 50)
        else:
            con = sqlite3.connect(self.data_base)
            cur = con.cursor()
            r, g, b = cur.execute(
                f'SELECT red, green, blue FROM flags WHERE id = {flag_id}').fetchone()
            return QColor(r, g, b)

    def drawDiagram(self, qp: QPainter):
        """Предназначена для рисования на frame"""
        start = self.dteStart.dateTime().toPyDateTime()
        end = self.dteEnd.dateTime().toPyDateTime()
        all_time, flag_time = self.getStatistic(start, end)

        center = self.frame.width() // 2, self.frame.height() // 2
        r = min(self.frame.width() // 2, self.frame.height() // 2) - 1
        rect = QRect(center[0] - r, center[1] - r, 2 * r, 2 * r)
        if all_time == 0:
            qp.drawEllipse(rect)
        else:
            now_angle = 0
            for flag_id, time in flag_time.items():
                color = self.getColor(flag_id)
                d_angel = int(16 * 360 * time / all_time)
                qp.setBrush(color)
                qp.drawPie(rect, now_angle, d_angel)
                now_angle += d_angel

    def loadFlagsId(self):
        return self.prnt.loadFlagsId()
