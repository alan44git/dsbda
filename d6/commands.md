# HBase & Hive Flight Data Management

## 📋 TASK A — Create Flight Info HBase Table

### Overview
Create a table named `flight_info` with three column families:
- **info** — flight airline, source, and destination
- **schedule** — departure and arrival times
- **delay** — delay information

### Create Table

```hbase
create 'flight_info', 'info', 'schedule', 'delay'
```

### Verify

```hbase
list
```

Expected output: `flight_info`

---

## 📝 Insert Data into HBase Table

### Syntax

```hbase
put 'table', 'rowkey', 'columnfamily:column', 'value'
```

### Sample Flight Data

#### Flight 1 (F101 — Air India)

```hbase
put 'flight_info', 'F101', 'info:airline', 'AirIndia'
put 'flight_info', 'F101', 'info:source', 'Delhi'
put 'flight_info', 'F101', 'info:destination', 'Mumbai'

put 'flight_info', 'F101', 'schedule:departure', '10:00'
put 'flight_info', 'F101', 'schedule:arrival', '12:00'

put 'flight_info', 'F101', 'delay:departure_delay', '15'
```

#### Flight 2 (F102 — Indigo)

```hbase
put 'flight_info', 'F102', 'info:airline', 'Indigo'
put 'flight_info', 'F102', 'info:source', 'Pune'
put 'flight_info', 'F102', 'info:destination', 'Bangalore'

put 'flight_info', 'F102', 'schedule:departure', '09:00'
put 'flight_info', 'F102', 'schedule:arrival', '11:00'

put 'flight_info', 'F102', 'delay:departure_delay', '30'
```

### View Data

```hbase
scan 'flight_info'
```

---

## 🔧 TASK B — Create, Drop, Alter Tables

### 1. Create Table

```hbase
create 'flight_info', 'info', 'schedule', 'delay'
```

### 2. Alter Table

Add new column family:

```hbase
alter 'flight_info', 'status'
```

Verify changes:

```hbase
describe 'flight_info'
```

### 3. Drop Table

First disable the table:

```hbase
disable 'flight_info'
```

Then drop it:

```hbase
drop 'flight_info'
```

### Recreate Table

⚠️ **Important for next tasks:**

```hbase
create 'flight_info', 'info', 'schedule', 'delay'
```

> Reinsert data again if the table was dropped.

---

## 🔗 TASK C — Create External Hive Table Connected to HBase

### Exit HBase Shell

```bash
exit
```

### Open Hive Shell

```bash
hive
```

### Create Hive Database

```sql
CREATE DATABASE flightdb;
USE flightdb;
```

### Create External Hive Table

Map to HBase table:

```sql
CREATE EXTERNAL TABLE flight_hive(
    flight_id STRING,
    airline STRING,
    source STRING,
    destination STRING,
    departure STRING,
    arrival STRING,
    departure_delay INT
)
STORED BY 'org.apache.hadoop.hive.hbase.HBaseStorageHandler'
WITH SERDEPROPERTIES (
    "hbase.columns.mapping" = ":key,info:airline,info:source,info:destination,schedule:departure,schedule:arrival,delay:departure_delay"
)
TBLPROPERTIES ("hbase.table.name" = "flight_info");
```
### Verify Data in Hive

```sql
SELECT * FROM flight_hive;
```

Expected output:

| flight_id | airline  | source | destination | departure | arrival | departure_delay |
|-----------|----------|--------|-------------|-----------|---------|-----------------|
| F101      | AirIndia | Delhi  | Mumbai      | 10:00     | 12:00   | 15              |
| F102      | Indigo   | Pune   | Bangalore   | 09:00     | 11:00   | 30              |

---

## 📊 TASK D — Find Total Departure Delay

Use SQL aggregation to calculate the total delay:

```sql
SELECT SUM(departure_delay) AS total_delay
FROM flight_hive;
```

Result: **45**

---

## 📈 TASK E — Find Average Departure Delay

### Formula

$$\text{Average Delay} = \frac{\sum \text{Departure Delays}}{\text{Number of Flights}}$$

### Hive Query

```sql
SELECT AVG(departure_delay) AS avg_delay
FROM flight_hive;
```

Result: **22.5**

---

## 🔍 TASK F — Create Index on Flight Information Table

Hive supports indexing to optimize query performance.

### Create Index

```sql
CREATE INDEX flight_index
ON TABLE flight_hive (airline)
AS 'COMPACT'
WITH DEFERRED REBUILD;
```

### Build Index

```sql
ALTER INDEX flight_index
ON flight_hive
REBUILD;
```

### Show Indexes

```sql
SHOW INDEX ON flight_hive;
```