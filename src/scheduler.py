import schedule
import time

class Scheduler:
    def __init__(self, agent):
        self.agent = agent
        schedule.every(6).hours.do(self.agent.learn)
    
    def start(self):
        print("🕒 Scheduler active (learning every 6 hours).")
        while True:
            schedule.run_pending()
            time.sleep(60)
