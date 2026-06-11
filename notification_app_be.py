from datetime import datetime


class Notification:
    def __init__(self, id, title, category, date, urgency, read=False):
        self.id = id
        self.title = title
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M")
        self.urgency = urgency
        self.read = read
        self.priority_score = self.calculate_priority()

    def calculate_priority(self):
        now = datetime.now()

        age_hours = (now - self.date).total_seconds() / 3600

        category_weight = {
            "placement": 100,
            "result": 90,
            "event": 70,
            "general": 50
        }.get(self.category.lower(), 50)

        recency_weight = max(0, 50 - age_hours)

        return category_weight + (self.urgency * 10) + recency_weight


class NotificationSystem:
    def __init__(self):
        self.notifications = []

    def add_notification(self, notification):
        self.notifications.append(notification)

    def get_top_notifications(self, limit=10):
        unread = [n for n in self.notifications if not n.read]

        unread.sort(
            key=lambda x: x.priority_score,
            reverse=True
        )

        return unread[:limit]


system = NotificationSystem()

system.add_notification(
    Notification(
        1,
        "Google Placement Drive Tomorrow",
        "placement",
        "2026-06-11 08:00",
        10
    )
)

system.add_notification(
    Notification(
        2,
        "Semester Result Published",
        "result",
        "2026-06-11 09:00",
        9
    )
)

system.add_notification(
    Notification(
        3,
        "Hackathon Registration Open",
        "event",
        "2026-06-10 18:00",
        7
    )
)

system.add_notification(
    Notification(
        4,
        "Library Notice",
        "general",
        "2026-06-09 10:00",
        3
    )
)

system.add_notification(
    Notification(
        5,
        "Microsoft Placement Test Today",
        "placement",
        "2026-06-11 11:00",
        10
    )
)

print("\nTOP 10 PRIORITY NOTIFICATIONS\n")

top_notifications = system.get_top_notifications(10)

for i, n in enumerate(top_notifications, start=1):
    print(f"{i}. {n.title}")
    print(f"   Category : {n.category}")
    print(f"   Priority : {n.priority_score:.2f}")
    print("-" * 40)