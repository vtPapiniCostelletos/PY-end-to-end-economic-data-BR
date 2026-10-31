from ingestion.utils.http import get


class WorldBankClient:
    """
    Client for interacting with the World Bank API.
    Country code set to BRA by default, but can be changed by passing a different code to the constructor.
    The period of time for default is a int representing the year.
    """

    BASE_URL = "https://api.worldbank.org/v2"

    def __init__(self, country_code: str = "BRA"):
        self.country_code = country_code

    def get_indicator(
                    self
                    ,indicator_id: str
                    ,start_year: int
                    ,end_year: int
                ) -> dict:
            """Fetch an indicator's data for the specified year range."""
            url = (
                 f"{self.BASE_URL}/country/"
                 f"{self.country_code}/indicator/"
                 f"{indicator_id}"
            )

            params = {
                "format": "json",
                "per_page": 1000,
                "date": f"{start_year}:{end_year}"
            }
            
            return get(url, params=params)