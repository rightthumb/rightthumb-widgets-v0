Perfect — here’s a set of **ULQL-style query dicts** (simple → advanced) you can use directly with your `PandasQueryBackend` + `MatplotlibVisualization`. Each example assumes you have:

```python
qb = PandasQueryBackend()
viz = MatplotlibVisualization()
datasets = {"events": events_df, "threats": threats_df}
```

---

# 🟢 Simple Queries

### 1. Count all events in last 15 minutes

```python
ulql = {
    "from": "events",
    "time": {"field": "ts", "from": "-15m", "to": "now"},
    "select": [{"metric": "count", "as": "events"}]
}
```

### 2. Traffic per source\_type in last 1 hour

```python
ulql = {
    "from": "events",
    "time": {"field":"ts","from":"-1h","to":"now"},
    "select": [{"metric":"count","as":"hits"}],
    "group_by": ["time:5min","source_type"]
}
```

### 3. All PHP errors (count)

```python
ulql = {
    "from": "threats",
    "where": [{"op":"eq","path":"category","value":"php-error"}],
    "select": [{"metric":"count","as":"errors"}]
}
```

---

# 🟡 Intermediate Queries

### 4. SSH failed logins per IP in last 24h

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-24h","to":"now"},
    "where": [{"op":"eq","path":"category","value":"ssh-fail"}],
    "select": [{"metric":"count","as":"failures"}],
    "group_by": ["ip"]
}
```

### 5. 404 errors per minute (traffic pattern)

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-2h","to":"now"},
    "where": [{"op":"eq","path":"category","value":"http-404"}],
    "select": [{"metric":"count","as":"404s"}],
    "group_by": ["time:1min"]
}
```

### 6. Distinct IPs hitting wp-\* paths

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-1d","to":"now"},
    "where": [{"op":"eq","path":"category","value":"wp-404"}],
    "select": [{"metric":"count_distinct:ip","as":"unique_ips"}]
}
```

---

# 🔴 Advanced Queries

### 7. Multi-series: PHP errors vs 404s per 10 minutes

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-6h","to":"now"},
    "where": [
        {"op":"in","path":"category","value":["php-error","http-404"]}
    ],
    "select": [{"metric":"count","as":"hits"}],
    "group_by": ["time:10min","category"]
}
```

### 8. Top 5 IPs by threat count (any category)

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-24h","to":"now"},
    "select": [{"metric":"count","as":"threats"}],
    "group_by": ["ip"]
}
# Then sort in Pandas:
df = qb.execute(ulql, datasets).sort_values("threats", ascending=False).head(5)
```

### 9. Correlate PHP errors and SSH failures by time window

```python
ulql = {
    "from": "threats",
    "time": {"field":"ts","from":"-12h","to":"now"},
    "where": [
        {"op":"in","path":"category","value":["php-error","ssh-fail"]}
    ],
    "select": [{"metric":"count","as":"hits"}],
    "group_by": ["time:30min","category"]
}
```

### 10. Average requests per IP (excluding 200 OK) in last hour

```python
ulql = {
    "from": "events",
    "time": {"field":"ts","from":"-1h","to":"now"},
    "where": [{"op":"ne","path":"meta.status","value":200}],
    "select": [{"metric":"avg:meta.status","as":"avg_status"}],
    "group_by": ["ip"]
}
```

---

⚡ These give you a spectrum:

* **Simple counts** (what happened?)
* **Intermediate breakdowns** (per IP, per category, per time bucket)
* **Advanced correlations** (multiple categories, top-N IPs, averages).

You can now swap the `"from"` dataset (`events` vs `threats`), adjust `"time"`, and build reports or visualizations with **one ULQL dict**.

---

👉 Do you want me to also prepare **paired VizSpec dicts** for these queries (so you can paste and immediately get charts without writing them yourself)?
