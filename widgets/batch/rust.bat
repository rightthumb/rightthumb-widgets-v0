@echo off


call pathAdd "D:\.rightthumb-widgets\widgets\rust\_\bin\binaryen-version_90-x86-windows"

:              w   n   b   o


echo.
if [%1] == [] call p. colorize -txt "    cargo clean \n    cargo update \n    cargo build --release " -hex orange -copy

if [%1] == [w] call p. colorize -txt "    cargo clean \n    cargo update \n    wasm-pack build --target web --release " -hex orange -copy

if [%1] == [r] call p. colorize -txt "    wasm-opt -Oz %1  %1   " -hex orange -copy


if [%1] == [n] call p. colorize -txt "cargo new %1 \n    cd %1" -hex orange -copy

if [%1] == [b] call p. colorize -txt "    source $HOME/.cargo/env    " -hex orange -copy

if [%1] == [o] call p. colorize -txt "    cargo add obf-rs   " -hex orange -copy

if [%1] == [r] call p. colorize -txt "    cargo run   " -hex orange -copy

echo.
echo.

goto:eof
echo cargo add obf-rs
echo cargo run

goto:eof
cargo install wasm-pack
# Install wasm-pack if needed
cargo install wasm-pack
# Build WebAssembly (Wasm) for web
wasm-pack build --target web --release
# Minify WebAssembly output
wasm-opt -Oz -o pkg/secure_wasm_bg.wasm pkg/secure_wasm_bg.wasm
echo.

:: Linux    --------------------------------------------
:: cargo build --release %*
goto:eof


:: wasm-pack build --target web --release
:: wasm-opt -Oz -o pkg/secure_wasm_bg.wasm pkg/secure_wasm_bg.wasm
:: wasm-validate pkg/secure_wasm_bg.wasm



