"""Contains the UptimeKuma class"""

from prometheus_client.parser import text_string_to_metric_families as pc
import requests


class UptimeKumaMonitor:
    """An object containing a dictionary representation of data returned by
    UptimeKuma `/metrics` endpoint

    Attributes:
        uptime_kuma_url (str): Full https url to a uptime_kuma instance
        user (str): Username of the Uptime Kuma user with access to the /metrics endpoint
        password (str): Password for Uptime Kuma user
        verify_ssl (bool): Allow bypassing ssl verification, but verify by default
    """

    def __init__(self, uptime_kuma_url, user, password, verify_ssl=True):
        self.data = dict()
        self.metrics_url = (
            f"{uptime_kuma_url}/metrics"
        )
        self.user = user
        self.password = password
        self.verify_ssl = verify_ssl
        self.update()

    def update(self):
        try:
            response = requests.get(
                self.metrics_url, auth=(self.user, self.password), verify=self.verify_ssl
            )
            self.metrics = response.content
            for family in pc(str(self.metrics, "UTF-8")):
                for sample in family.samples:
                    if sample[0].startswith("monitor"): self.data [sample[1]["monitor_name"]] = {}
            for family in pc(str(self.metrics, "UTF-8")):
                for sample in family.samples:
                    if sample[0].startswith("monitor"): self.data [sample[1]["monitor_name"]][sample[0]] = sample[2]
        except Exception as error:
            raise UptimeKumaError(
                f"Could not fetch Uptime Kuma metrics: {error}"
            )


class UptimeKumaError(Exception):
    """Failed to fetch Uptime Kuma metrics."""

    pass