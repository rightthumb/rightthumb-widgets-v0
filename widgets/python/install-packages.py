import subprocess
import os

# 🧠 Your original list of modules (case-insensitive)
raw_modules = '''
AES AESGCM AesEverywhere AppKit AudioFile AudioSegment Bar BeautifulSoup Blowfish Flask Calendar ChromeDriverManager Cipher Client CodeIndexerPygments Controller Crypto Cython DNSException Database Database2 Databases ECCMan FTP Fernet Fields Fore Gtk HMAC HTMLParser HTTPDigestAuth HTTPServer HarTool Hasher IMDb IP2Location IPAddress IPNetwork Image Instaloader KMeans Key Keys List Listener MIMEMultipart MIMEText MP3File Manager MdFig MdFigParser MessagingResponse MinThread MongoClient NSWorkspace NameOID Nominatim Observer OpenRGBClient OpenSSL OptionParser Options OrderedDict PBKDF2 PBKDF2HMAC PIL Parser Path PatternMatchingEventHandler PdfReader Pinterest Popen PorterStemmer PyKeyboardEvent PyPDF2 PyQt4 PythonLexer QtCore Queue RGBColor RSCodecError ReedSolomonError SSHClient SSHTunnelForwarder S_ISDIR Select Server Service ServiceAccountCredentials SignedJwtAssertionCredentials SimpleGUICS2Pygame SimpleHTTPRequestHandler StaleElementReferenceException StringIO Structure Style Switches Tables Tee Terminal256Formatter TerminalFormatter Thread ThreadPoolExecutor ThreadingMixIn Threads Timer Tk Token UnQLiteMgr WebDriverWait ZipFile absolute_ actual_function aes256 all_timezones app argv array arrow ast astor audioio auditSQL base batch_c batch_cc batch_theUSB batch_timestamp bcrypt binaryornot binascii bkExpire blank board browsermobproxy bs4 c calendar call ceil cgi chardet choice classic clockwork colorama colored colorsys combinations con config conn copy copyfile count createParser create_backup_filename crypt cryptography cssselect currentframe cv2 cythonize date datefinder dateutil dbapi2 decodebytes default_backend defaultdict dic_key_sort2 digitalio dill dir0 distro distutils division dns docx docx2txt docx_utils duckdb encryptedpickle ensurepip example_forms1 exifCompare expanduser expected_conditions extractMetadata fcntl fcrypt fileBackup findKey formatSize four ftplib func gTTS gcal2jd genForm generateRelevantFolders geodesic geopy get_mac_address get_next_entry get_random_bytes getaddrinfo getmac getmtime getpass gh_md_to_html gi googlesearch gspread gtts gzip hachoir hashes helper hexColor hexColors hexlify highlight hls_to_rgb iName iPath icalendar ics imdb imdbApp index indexText instaloader ipaddress isDate is_binary isfile islice itemgetter jd2gcal jdcal join jsonStructure jsonlines keyboard keys lex liaison lib simplejson lib2to3 lib3to2 library load lorem lxml magic main mean messagebox mimetypes move movieTitle mp3_tagger mpu mss msvcrt my_module mysql namedtuple native_web_app netaddr nltk num2word numpy oauth2client odf opc_to_flat_opc openai openrgb operator optparse orjson pack pad padding pandas paramiko parse parse_header parse_qs parso path pbkdf2 pgeocode phonenumbers piexif pinterest pocketsphinx poplib printVarSimpleFake2 print_ progress psutil psycopg2 pulseio py2exe pyAesCrypt pyColor py_compile pyautogui pydub pygame pygments pykeyboard pylnk3 pymongo pymysql pynput pyodbc pyperclip pysqlcipher3 pytesseract pytz pyzipper randint randomTool randrange redirect_stdout reduce regImp regex relativedelta requests rightthumb rrule rsa saveCryptTable schedule scrapy search selenium sep serialization server settings setup setuptools shlex simplegui simpleio sin sklearn sleep socket socketserver soundcard sounddevice speech_recognition speedtest split_on_silence sql sqliteMgr sshtunnel stickytape stopwords string struct system tabulate template termcolor text textract theParentItem tiktoken timedelta tkinter tldextract tqdm ttk twilio txtBackup2 ujson unhackable unicodedata unistego unpad unqlite unquote urlextract urljoin urllib2 urllib3 urlopen urlparse urlsafe_b64encode urlsplit usaddress vIndex vault_helper vindex watchdog webdriver webdriver_manager websockets whois win32api win32clipboard win32com win32con win32file win32gui winreg winsound with_statement wmi wnck word_tokenize x509 xtarfile yaml youtube_dl zlib
'''


# Clean and deduplicate
all_modules = set()
for line in raw_modules.strip().split():
    # Remove weird punctuation
    cleaned = line.strip(",;()").replace(' ', '')
    if cleaned:
        all_modules.add(cleaned.lower())  # use lowercase for pip

success = []
fail = []

print(f"🔍 Attempting to install {len(all_modules)} modules...\n")

for module in sorted(all_modules):
    print(f"📦 Installing: {module}")
    if os.path.isfile('/usr/local/bin/pip3.11'):
        result = subprocess.run(['/usr/local/bin/pip3.11', 'install', module], capture_output=True, text=True)
    else:
        result = subprocess.run(['pip3', 'install', module], capture_output=True, text=True)
    if result.returncode == 0:
        success.append(module)
    else:
        fail.append(module)
        print(f"❌ Failed: {module}\n{result.stderr.splitlines()[-1]}")

print("\n✅ Done")
print(f"✔️  Success: {len(success)}")
print(f"❌ Failed: {len(fail)}")

if fail:
    print("\nFailed installs:")
    for m in fail:
        print(f" - {m}")
