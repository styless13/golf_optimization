# 1. Load dataset
try:
df = pd.read_csv('data.csv')

# 2. Convert date and time columns to datetime format
df['arrival_time'] = pd.to_datetime('2026-' + df['date'].astype(str) + ' ' + df['arrival_time'].astype(str))
df['start_time'] = pd.to_datetime('2026-' + df['date'].astype(str) + ' ' + df['start_time'].astype(str))
df['end_time'] = pd.to_datetime('2026-' + df['date'].astype(str) + ' ' + df['end_time'].astype(str))

# 3. Calculate Key Performance Indicators (KPIs)
df['wait_time_min'] = (df['start_time'] - df['arrival_time']).dt.total_seconds() / 60
df['play_duration_min'] = (df['end_time'] - df['start_time']).dt.total_seconds() / 60

# 4. Display Analysis Results
print("=" * 50)
print("📊 SCREEN GOLF VENUE OPERATIONAL ANALYSIS")
print("=" * 50)
print(f"Total Transactions Analyzed: {len(df)}")
print(f"Average Customer Wait Time: {df['wait_time_min'].mean():.1f} mins")
print(f"Maximum Wait Time Recorded: {df['wait_time_min'].max():.1f} mins")
print(f"Average Play Duration: {df['play_duration_min'].mean():.1f} mins")
print("-" * 50)
print("[Room Utilization - Usage Count]")
print(df['room_no'].value_counts().sort_index().to_string())
print("=" * 50)

except FileNotFoundError:
print("❌ Error: 'data.csv' not found. Please place it in the same directory.")
except Exception as e:
print(f"❌ Error occurred: {e}")
