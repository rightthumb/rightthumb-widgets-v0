
import os
import re
import regex

class FileAnalyzer:
	class fn:

		@staticmethod
		def scrape_urls(text):
			pattern = r'https?://[^\s\'",;]+'
			return set(re.findall(pattern, text))

		@staticmethod
		def scrape_windows_file_paths(text):
			text = text.replace('\\\\', '\\')
			pattern = r'\b[a-zA-Z]:\\(?:[^\\<>:"|?*\r\n]+\\)*[^\\<>:"|?*\r\n]+\b'
			return re.findall(pattern, text)

		@staticmethod
		def scrape_windows_file_paths2(text):
			text = text.replace('\\\\', '\\')
			pattern = r'(?:[a-zA-Z]:)?(?:[\\/])?(?:[^<>:"\\/|?*\s]+[\\/])+(?:[^<>:"\\/|?*\s]+[\\/]?)*'
			return re.findall(pattern, text)

		@staticmethod
		def scrape_linux_file_paths(text):
			text = text or ''
			for url in FileAnalyzer.fn.scrape_urls(text):
				text = text.replace(url, '')
			pattern = r'(?<!https?:)(?:~\/|\/)(?:[^\/\0\s]+\/)*[^\/\0\s]*'
			return list(set(regex.findall(pattern, text)))

		@staticmethod
		def sanitize_filename(filename):
			return re.sub(r'[<>:"/\\|?*\n\r\t]', '_', filename).strip()

		@staticmethod
		def save_file_safe(base_folder, relative_path, content, fallback_name='file.txt'):
			relative_path = relative_path.replace('\\', os.sep).replace('/', os.sep).strip()
			if relative_path.startswith('#!'):
				relative_path = 'env_header.txt'
			if relative_path.startswith('~'):
				relative_path = relative_path.replace('~', 'home', 1)
			if relative_path.lower() in ['pre', 'code', 'script', 'style']:
				relative_path += '_.txt'
			if not relative_path or relative_path.strip() in ['.', '..']:
				relative_path = fallback_name
			if not os.path.splitext(relative_path)[1]:
				relative_path += '.txt'

			parts = relative_path.split(os.sep)
			safe_parts = [FileAnalyzer.fn.sanitize_filename(part) for part in parts]
			safe_path = os.path.join(base_folder, *safe_parts)
			os.makedirs(os.path.dirname(safe_path), exist_ok=True)
			with open(safe_path, 'w', encoding='utf-8') as f:
				f.write(content)
			return safe_path

		@staticmethod
		def extract_name_tokens(content):
			return re.findall(r'\b[\w\-]+\.(js|html|json|py|txt|css|ts|rs)\b', content)

		@staticmethod
		def generate_patterns_dict(data):
			result = {}
			for key, text in data.items():
				text = text.replace("'", " ").replace('"', " ")
				tokens = text.split()
				patterns = set()
				for token in tokens:
					for i in range(len(token) - 1):
						patterns.add(token[i:i+2])
				result[key] = patterns
			return result

		@staticmethod
		def compare_patterns_dicts(target_dict, source_dict, threshold=0.25):
			results = {}
			for t_key, t_patterns in target_dict.items():
				matches = []
				for s_key, s_patterns in source_dict.items():
					if not t_patterns or not s_patterns:
						continue
					intersection = t_patterns & s_patterns
					union = t_patterns | s_patterns
					score = len(intersection) / len(union)
					if score >= threshold:
						matches.append((s_key, round(score, 3)))
				matches.sort(key=lambda x: -x[1])
				results[t_key] = matches
			return results

		@staticmethod
		def determine_best_filename(file, all_files):
			name = file.get('name', '').replace('📁', '').strip()
			content = file.get('content', '')
			fallback = name or 'unknown.txt'

			file_dict = {f.get('name', '').replace('📁', '').strip(): f.get('content', '') for f in all_files}
			name_patterns = FileAnalyzer.fn.generate_patterns_dict(file_dict)

			references = {}
			for fname, text in file_dict.items():
				tokens = FileAnalyzer.fn.extract_name_tokens(text)
				for t in tokens:
					references[t] = text

			ref_patterns = FileAnalyzer.fn.generate_patterns_dict(references)
			matches = FileAnalyzer.fn.compare_patterns_dicts(ref_patterns, name_patterns, threshold=0.25)

			for ref, match_list in matches.items():
				for match_name, score in match_list:
					if match_name == name:
						return ref
			return fallback

		@staticmethod
		def score_file_likelihood(name, content, cross_references):
			name = name.strip().lower()
			score = 0.0

			if '.' in name and ':' not in name:
				score += 0.4
			if content.strip()[:64].lower().startswith(('<!doctype', '#!', '{', 'def ', 'function ', 'import ', 'export ')):
				score += 0.3
			for ref in cross_references:
				if name in ref:
					score += 0.2
					break
			if os.path.splitext(name)[1] in ['.js', '.html', '.json', '.py', '.txt', '.css', '.ts', '.rs']:
				score += 0.1
			return round(score, 3)




'''
Here are **2 simple examples** showing how to use your `FileAnalyzer.fn` class 
	for other tasks — both focused on pattern analysis but usable for any part of the system.

---

### ✅ Example 1: Compare Two Texts Using Pattern Similarity

```python
from FileAnalyzer import FileAnalyzer  # if in its own module

text1 = "The quick brown fox jumps over the lazy dog"
text2 = "The fast brown animal hops over a lazy dog"

data = {
    'text1': text1,
    'text2': text2
}

patterns = FileAnalyzer.fn.generate_patterns_dict(data)
results = FileAnalyzer.fn.compare_patterns_dicts({'text1': patterns['text1']}, {'text2': patterns['text2']})

print('Similarity score between text1 and text2:', results['text1'])
```

🔍 **What it does**: Detects overlap in adjacent-character pairs (bigrams) between two similar texts.

---

### ✅ Example 2: Find Closest Filename Match Among Many

```python
data = {
    'popup.js': "document.getElementById('run')",
    'main.html': "<script src='popup.js'></script>",
    'config.json': '{ "version": "1.0" }'
}

references = {
    'popup.js': "main.html includes <script src='popup.js'>",
    'config.json': "used by native_host.py"
}

patterns_data = FileAnalyzer.fn.generate_patterns_dict(data)
patterns_ref = FileAnalyzer.fn.generate_patterns_dict(references)

matches = FileAnalyzer.fn.compare_patterns_dicts(patterns_ref, patterns_data)

for ref, hits in matches.items():
    print(f'\nClosest matches for: {ref}')
    for name, score in hits:
        print(f'  → {name} (score={score})')
```

🔍 **What it does**: Matches inferred file references to actual filenames based on pattern overlap.

'''
