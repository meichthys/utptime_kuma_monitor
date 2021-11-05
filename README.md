# UptimeKuma

Python wrapper around UptimeKuma api

## Installation

```bash
pip install uptime_kuma
```

## QuickStart

```python
>>> from uptime_kuma import UptimeKuma
>>> utk = UptimeKuma("https://your_uptime-kuma_url", "uptime-kuma_username", "uptime-kuma_password")
>>> utk.data['UpdimeKuma']['monitor_response_time']
13.0
>>> utk.data['UpdimeKuma']['monitor_status']
1.0
```

Notes:

- The user must have access to the Uptime Kuma `/metrics` endpoint

## Change Log

- v1.0.0 : Initial Release