import requests
from bs4 import BeautifulSoup


class Scraper:
    def __inti__(self):
        pass

    def fetch_tactic(self, url):
        """
        Fetch each tacitcs from https://attack.mitre.org/tactics/enterprise/
        to prepare Tactic ID for fetching techniques.

        Parameters
        ----------
        url : string
            url of target site.

        Returns
        -------
        None
            nothing

        Raises
        ------
        RequestTimeoutError
            when a page can not accessible
        RateLimitError
            when you kidding the admin site
        """
        r = requests.get(url)
        if r.ok:
            soup = BeautifulSoup(r.content, 'html.parser')
            tds = soup.findAll('tr')
            for td in tds:
                print(td)
                # TODO: saving in list ttps

    def fetch_techinique(self):
        pass

    def save_ttp(self):
        pass

    def visualize(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    cls = Scraper()
    cls.fetch_tactic("https://attack.mitre.org/tactics/enterprise/")