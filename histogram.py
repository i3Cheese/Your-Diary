from PyQt5.QtWidgets import QWidget
from ui_Histogram import Ui_Histogram
from datetime import timedelta, datetime


class HistogramWidget(QWidget, Ui_Histogram):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.prnt = parent

        self.reload()
        self.setWindowTitle(f'{self.prnt.title} - Диаграмма')
        self.pbCreate.clicked.connect(self.doHistogram)

    def reload(self):
        start, end = self.prnt.getTimeBorders()
        self.deStart.setDate(start.date())
        self.deEnd.setDate(end.date())

    def doHistogram(self):
        start = self.deStart.dateTime().toPyDateTime()
        end = self.deEnd.dateTime().toPyDateTime() + timedelta(days=1)
        if start > end:
            return None
        x, y = self.getStatistic(start, end)
        plot = self.graphicsView.plotItem
        plot.clear()
        plot.hideAxis('bottom')
        plot.plot(x, y, fillLevel=0, brush=(0, 255, 255))

    def getStatistic(self, start: datetime, end: datetime):
        notes = self.prnt.loadNotes()

        # Сканлайн
        evs = []
        for note in notes:
            n_start, n_end = datetime.fromisoformat(note[1]), datetime.fromisoformat(note[2])
            n_start, n_end = max(n_start, start), min(n_end, end)
            if n_start >= n_end:
                continue
            evs.append((n_start, 1))
            evs.append((n_end, -1))
        now_date = start + timedelta(days=1)
        while now_date <= end:
            evs.append((now_date, 0))
            now_date += timedelta(days=1)
        evs.sort()
        x = [start.timestamp()]
        y = [0]
        last_time = start
        cnt_time = 0
        cnt_notes = 0
        for time, event_type in evs:
            if event_type == 0:
                if cnt_notes:
                    cnt_time += (time - last_time).total_seconds()

                x.append((time - timedelta(hours=23)).timestamp())
                x.append((time - timedelta(hours=23)).timestamp())
                x.append((time - timedelta(hours=1)).timestamp())
                x.append((time - timedelta(hours=1)).timestamp())
                y.append(0)
                y.append(cnt_time // 60)
                y.append(cnt_time // 60)
                y.append(0)

                cnt_time = 0
                last_time = time
            else:
                if cnt_notes:
                    cnt_time += (time - last_time).total_seconds()
                cnt_notes += event_type
                last_time = time
        return x, y
