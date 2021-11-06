# Uptime Kuma Monitor

Python wrapper around UptimeKuma `/metrics` endpoint

## Installation

```bash
pip install uptime_kuma_monitor
```

## QuickStart

```python
>>> from uptime_kuma_monitor import UptimeKumaMonitor
>>> utkm = UptimeKumaMonitor("https://your_uptime-kuma_url", "uptime-kuma_username", "uptime-kuma_password")
>>> utkm.data
{
    'UptimeKuma': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 141.0, 'monitor_status': 1.0},
    'AdGuard Home': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 22.0, 'monitor_status': 1.0},
    'Bitwarden': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 17.0, 'monitor_status': 1.0},
    'Home Assistant': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 114.0, 'monitor_status': 1.0},
    'Gitea': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 2331.0, 'monitor_status': 1.0},
    'NginxProxyManager': {'monitor_cert_days_remaining': 55.0, 'monitor_cert_is_valid': 1.0, 'monitor_response_time': 18.0, 'monitor_status': 1.0},
    ...
}
>>> utkm.data['UptimeKuma']['monitor_response_time']
13.0
>>> utkm.data['UptimeKuma']['monitor_status']
1.0
```

Notes:

- The user must have access to the Uptime Kuma `/metrics` endpoint

## Change Log

- v1.0.0 : Initial Release