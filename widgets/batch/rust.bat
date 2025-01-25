@echo off


echo.
call p. colorize -txt "    cargo clean \n    cargo update \n    cargo build --release %*" -hex orange -copy
echo.
echo.
echo cargo run
echo.
echo.

@REM Linux    --------------------------------------------
@REM source $HOME/.cargo/env


@REM cargo build --release %*

