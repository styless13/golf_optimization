import pandas as pd
import matplotlib.pyplot as plt

# 1. Load CSV file & Clean Data
df = pd.read_csv('data.csv')
df['date'] = df['date'].ffill()
df['date_clean'] = pd.to_datetime(df['date'].astype(str) + ' 2026', errors='coerce').dt.strftime('%Y-%m-%d')

# 2. Datetime Conversion
df['arrival'] = pd.to_datetime(df['date_clean'] + ' ' + df['arrival_time'].astype(str), errors='coerce')
df['start'] = pd.to_datetime(df['date_clean'] + ' ' + df['start_time'].astype(str), errors='coerce')

# 3. Calculate Wait Time
df['wait_time_min'] = (df['start'] - df['arrival']).dt.total_seconds() / 60
df['arrival_hour'] = df['arrival'].dt.hour

# 4. Hourly Summary Dataframe
hourly = df.groupby('arrival_hour').agg(
visit_count=('wait_time_min', 'count'),
avg_wait=('wait_time_min', 'mean')
).reset_index()

# 5. Visualization (Matplotlib)
fig, ax1 = plt.subplots(figsize=(10, 5))

# 막대 그래프: 방문 고객 수 (파란색)
bars = ax1.bar(hourly['arrival_hour'], hourly['visit_count'], color='#4C72B0', alpha=0.6, label='Visits')
ax1.set_xlabel('Hour of Day')
ax1.set_ylabel('Visit Count', color='#4C72B0')
ax1.tick_params(axis='y', labelcolor='#4C72B0')

# 꺾은선 그래프: 평균 대기시간 (빨간색)
ax2 = ax1.twinx()
line = ax2.plot(hourly['arrival_hour'], hourly['avg_wait'], color='#C44E52', marker='o', linewidth=2, label='Avg Wait Time')
ax2.set_ylabel('Avg Wait Time (mins)', color='#C44E52')
ax2.tick_params(axis='y', labelcolor='#C44E52')

plt.title('Hourly Customer Visits & Average Wait Time')
plt.grid(True, linestyle='--', alpha=0.5)
fig.tight_layout()

# 그래프 창 출력
plt.show()
