@echo off


echo.
call p. colorize -txt "    cargo clean \n    cargo update \n    cargo build --release %*" -hex orange -copy
echo.
echo.
echo cargo run
echo.
echo.
@REM echo cargo install wasm-pack
echo cargo add obf-rs
@REM # Install wasm-pack if needed
@REM echo cargo install wasm-pack
@REM # Build WebAssembly (Wasm) for web
echo wasm-pack build --target web --release
@REM # Minify WebAssembly output
echo wasm-opt -Oz -o pkg/secure_wasm_bg.wasm pkg/secure_wasm_bg.wasm
echo.

@REM Linux    --------------------------------------------
@REM source $HOME/.cargo/env
@REM cargo build --release %*
goto:eof


wasm-pack build --target web --release
wasm-opt -Oz -o pkg/secure_wasm_bg.wasm pkg/secure_wasm_bg.wasm
@REM wasm-validate pkg/secure_wasm_bg.wasm



