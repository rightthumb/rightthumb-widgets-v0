@echo off
@REM %signtool% sign /f "D:\websites\domains\signtool\scott_reph\scott_reph.crt" /t http://timestamp.digicert.com /fd SHA256 /a %1
@REM %signtool% sign /f "D:\websites\domains\signtool\scott_reph.der" /t http://timestamp.digicert.com /fd SHA256 /a %1
@REM %signtool% sign /f D:\websites\domains\signtool\scott_reph\SSL_COM_CODE_SIGNING_INTERMEDIATE_CA_RSA_R1.crt /t http://timestamp.digicert.com /fd SHA256 /a %1
@REM %signtool% sign /f "D:\websites\domains\signtool\scott_reph\SSL_COM_ROOT_CERTIFICATION_AUTHORITY_RSA.crt" /t http://timestamp.digicert.com /fd SHA256 /a %1
@REM %signtool% sign /f "D:\websites\domains\signtool\scott_reph.p7b" /t http://timestamp.digicert.com /fd SHA256 /a %1
@REM %signtool% sign /fd sha256 /a %1
@REM %signtool% sign /fd sha256 /tr http://ts.ssl.com /td sha256 /sha1 certificate thumbprint 
if not exist signed (
    mkdir signed
)

set path=%path%;D:\websites\domains\signtool\CodeSignTool-v1.3.0-windows

call p. code-sign-vars > "%stmp%\sign.bat"
call "%stmp%\sign.bat"
call rm "%stmp%\sign.bat" > nul
if [%2] == [] (
    @REM %signtool% sign /fd sha256 /tr http://ts.ssl.com /td sha256 /sha1 certificate thumbprint %1
    CodeSignTool sign -credential_id=%sign_credential% -username=%sign_username% -password="%sign_password%" -output_dir_path=signed -input_file_path=%1
) else (
    echo CodeSignTool sign -credential_id=%sign_credential% -username=%sign_username% -password="%sign_password%" -output_dir_path=signed -input_file_path=%1
)
