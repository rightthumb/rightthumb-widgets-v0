<?php
if ($argc !== 3) {
    fwrite(STDERR, "Usage: php obfuscate.php input.php output.py\n");
    exit(1);
}

$input  = $argv[1];
$output = $argv[2];

if (!file_exists($input) || !is_readable($input)) {
    fwrite(STDERR, "Error: Cannot read input file: $input\n");
    exit(2);
}

$source = file_get_contents($input);
if ($source === false) {
    fwrite(STDERR, "Error: Failed to read file contents.\n");
    exit(3);
}

$compressed = gzdeflate($source);
if ($compressed === false) {
    fwrite(STDERR, "Error: Compression failed.\n");
    exit(4);
}

$encoded = base64_encode($compressed);
if ($encoded === false) {
    fwrite(STDERR, "Error: Base64 encoding failed.\n");
    exit(5);
}

// Output as Python-compatible code
$payload = 'import zlib, base64; exec(zlib.decompress(base64.b64decode("' . $encoded . '")))';

if (file_put_contents($output, $payload) === false) {
    fwrite(STDERR, "Error: Failed to write output file: $output\n");
    exit(6);
}

echo "✅ Python-wrapped obfuscated payload written to: $output\n";
