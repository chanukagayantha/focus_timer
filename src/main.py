import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QComboBox, QPushButton, QGridLayout
)
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont

class ProductivityTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.running = False
        self.paused = False
        self.work_phase = True
        self.remaining = 0
        
        # Timer presets
        self.presets = {
            "52/17": (52, 17),
            "Pomodoro (25/5)": (25, 5),
            "Ultradian (90/20)": (90, 20)
        }
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle('Productivity Timer')
        self.setFixedSize(400, 300)
        
        # Create widgets
        self.method_selector = QComboBox()
        self.method_selector.addItems(self.presets.keys())
        self.method_selector.setCurrentIndex(0)
        
        self.time_display = QLabel('00:00')
        self.time_display.setFont(QFont('Helvetica', 40))
        self.time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.phase_label = QLabel('Work Phase')
        self.phase_label.setStyleSheet('color: green; font-size: 14px;')
        self.phase_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.start_btn = QPushButton('Start')
        self.pause_btn = QPushButton('Pause')
        self.stop_btn = QPushButton('Stop')
        
        # Set initial button states
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        
        # Connect signals
        self.start_btn.clicked.connect(self.start_timer)
        self.pause_btn.clicked.connect(self.toggle_pause)
        self.stop_btn.clicked.connect(self.stop_timer)
        
        # Setup layout
        layout = QGridLayout()
        layout.addWidget(self.method_selector, 0, 0, 1, 2)
        layout.addWidget(self.time_display, 1, 0, 1, 2)
        layout.addWidget(self.phase_label, 2, 0, 1, 2)
        layout.addWidget(self.start_btn, 3, 0)
        layout.addWidget(self.pause_btn, 3, 1)
        layout.addWidget(self.stop_btn, 4, 0, 1, 2)
        
        self.setLayout(layout)
        
        # Setup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        
    def start_timer(self):
        if not self.running:
            self.running = True
            self.work_phase = True
            self.start_btn.setEnabled(False)
            self.pause_btn.setEnabled(True)
            self.stop_btn.setEnabled(True)
            
            preset = self.presets[self.method_selector.currentText()]
            self.work_duration = preset[0] * 60
            self.break_duration = preset[1] * 60
            self.remaining = self.work_duration
            
            self.update_display()
            self.timer.start(1000)
            
    def update_timer(self):
        if self.paused:
            return
            
        if self.remaining > 0:
            self.remaining -= 1
            self.update_display()
        else:
            self.play_notification()
            self.work_phase = not self.work_phase
            self.remaining = self.work_duration if self.work_phase else self.break_duration
            self.update_phase_label()
            self.update_timer()
            
    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_btn.setText('Resume' if self.paused else 'Pause')
        
    def stop_timer(self):
        self.running = False
        self.paused = False
        self.timer.stop()
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)
        self.pause_btn.setText('Pause')
        self.time_display.setText('00:00')
        self.phase_label.setText('Work Phase')
        self.phase_label.setStyleSheet('color: green; font-size: 14px;')
        
    def update_display(self):
        minutes = self.remaining // 60
        seconds = self.remaining % 60
        self.time_display.setText(f"{minutes:02d}:{seconds:02d}")
        
    def update_phase_label(self):
        text = "Work Phase" if self.work_phase else "Break Phase!"
        color = "green" if self.work_phase else "red"
        self.phase_label.setText(text)
        self.phase_label.setStyleSheet(f'color: {color}; font-size: 14px;')
        
    def play_notification(self):
        # macOS notification with sound
        message = "Time to start " + ("working!" if self.work_phase else "your break!")
        os.system(f"""
            osascript -e 'display notification "{message}" with title "Timer Alert" sound name "Ping"'
        """)
        os.system('afplay /System/Library/Sounds/Ping.aiff')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProductivityTimer()
    window.show()
    sys.exit(app.exec())