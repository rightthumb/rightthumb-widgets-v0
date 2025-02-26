import re

class HarTool:
    def __init__(self, data):
        """Initialize the HAR tool with either a file path or a pre-loaded dictionary."""
        if isinstance(data, dict):
            self.data = data  # If already a dictionary, use it directly
        elif isinstance(data, str):
            self.data = self.load(data)  # If a file path, load the JSON
        else:
            raise TypeError("Invalid input: expected a file path (str) or a dictionary (dict).")

        self.entries = self.data.get("log", {}).get("entries", [])

    def load(self, path):
        """Try loading a JSON file using various parsers, returning immediately on success."""
        parsers = []

        # Try importing each JSON module
        try:
            import orjson  # type: ignore
            parsers.append(("orjson", lambda f: orjson.loads(f.read()), "rb"))
        except ImportError:
            pass

        try:
            import ujson  # type: ignore
            parsers.append(("ujson", lambda f: ujson.load(f), "r"))
        except ImportError:
            pass

        try:
            import simplejson as json
            parsers.append(("simplejson", lambda f: json.load(f), "r"))
        except ImportError:
            import json
            parsers.append(("json", lambda f: json.load(f), "r"))

        # Try each parser and return immediately on success
        for name, parser, mode in parsers:
            try:
                with open(path, mode, encoding=None if mode == "rb" else "utf-8") as f:
                    data = parser(f)
                print(f"Loaded with {name}")
                return data  # Return immediately on success
            except Exception as e:
                print(f"Failed with {name}: {e}")

        raise RuntimeError("All JSON parsers failed.")

    def urls(self,dic=True):
        """Extracts all unique URLs from the HAR file."""
        urls = {entry["request"]["url"] for entry in self.entries if "request" in entry}
        Urls = sorted(urls)
        if not dic: return Urls
        urlDic = {}
        for url in Urls:
            ext = url.split('.')[-1]
            if False:
                pass
            elif '.php?' in url:
                ext = 'php'
            elif '/' in ext:
                if 'com/css?' in url: ext = 'css'
            elif '?' in ext:
                ext = '?'
            if not ext in urlDic:
                urlDic[ext] = []
            urlDic[ext].append(url)
        return urlDic

    def search(self, text, caseSensitive=False, regex=False, ext=".json"):
        """
        Searches request and response contents for a given text.

        Args:
            text (str): The text to search for.
            caseSensitive (bool): Whether the search should be case-sensitive.
            regex (bool): Whether to interpret the text as a regular expression.
            ext (str): File extension filter (currently unused, but included for future use).

        Returns:
            set: URLs containing the searched text.
        """
        matching_urls = set()
        flags = 0 if caseSensitive else re.IGNORECASE

        for entry in self.entries:
            request_content = entry.get("request", {}).get("postData", {}).get("text", "")
            response_content = entry.get("response", {}).get("content", {}).get("text", "")
            url = entry["request"]["url"]

            if regex:
                pattern = re.compile(text, flags)
                if pattern.search(request_content) or pattern.search(response_content):
                    matching_urls.add(url)
            else:
                search_text = text if caseSensitive else text.lower()
                if (search_text in request_content.lower()) or (search_text in response_content.lower()):
                    matching_urls.add(url)

        return sorted(matching_urls)  # Sorted for consistency

    def searchAdvanced(self, has=[], omit=[], OR=False, ext=None, caseSensitive=False, snip=0):
            """
            Advanced search for URLs in the HAR file based on inclusion and exclusion criteria.
            Optionally, return a snippet of found text around the search term.

            Args:
                has (list): List of strings to search for (must contain all by default, at least one if OR=True).
                omit (list): List of strings to exclude (if a URL contains any, it's omitted).
                OR (bool): If True, URLs matching at least one item in `has` are included; otherwise, all must be present.
                ext (str): File extension filter (currently unused, but included for future use).
                caseSensitive (bool): Whether the search should be case-sensitive.
                snip (int): Number of characters to include with search term in middle, breaking on `\n` on both ends.

            Returns:
                dict: URLs matching the criteria, optionally with text snippets.
            """
            matching_results = {}
            flags = 0 if caseSensitive else re.IGNORECASE

            for entry in self.entries:
                url = entry["request"]["url"]
                if not ext is None and not url.endswith(ext): continue
                request_content = entry.get("request", {}).get("postData", {}).get("text", "")
                response_content = entry.get("response", {}).get("content", {}).get("text", "")
                full_text = f"{url} {request_content} {response_content}"

                if not caseSensitive:
                    full_text = full_text.lower()
                    has = [term.lower() for term in has]
                    omit = [term.lower() for term in omit]

                # Exclude URLs that contain any of the omit terms
                if any(term in full_text for term in omit):
                    continue

                # Check for presence of `has` terms
                if has:
                    found = False
                    for term in has:
                        if term in full_text:
                            found = True
                            if not OR:
                                continue
                            break
                    if not found:
                        continue

                if snip > 0:
                    snippets = []
                    for term in has:
                        for match in re.finditer(term, full_text, flags):
                            start = max(0, match.start() - snip // 2)
                            end = min(len(full_text), match.end() + snip // 2)
                            snippet = full_text[start:end]
                            snippet = snippet.split("\n", 1)[-1].rsplit("\n", 1)[0]
                            snippets.append(snippet)
                    matching_results[url] = snippets if snippets else "No snippet found"
                else:
                    matching_results[url] = None

            return matching_results


# Example Usage
# har_tool = HarTool("example.har")  # Pass a file path
# har_tool = HarTool(pre_loaded_dict)  # Pass a pre-loaded HAR dictionary
