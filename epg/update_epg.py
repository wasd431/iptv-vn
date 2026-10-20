from datetime import datetime, timedelta, timezone

now = datetime.now(timezone.utc)
start_time = now.strftime("%Y%m%d%H%M%S +0000")

stop_time = (now + timedelta(days=7)).strftime("%Y%m%d%H%M%S +0000")
refresh_date = now.strftime("%Y-%m-%d %H:%M:%S UTC")

with open("epg.xml", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("START_TIME", start_time)
content = content.replace("STOP_TIME", stop_time)
content = content.replace("REFRESH_DATE", refresh_date)

with open("epg.xml", "w", encoding="utf-8") as f:
    f.write(content)

print("EPG updated successfully for:", refresh_date)
