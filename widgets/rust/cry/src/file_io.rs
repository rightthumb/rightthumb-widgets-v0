use std::fs::{File, OpenOptions};
use std::io::{Read, Write, Error};
use reqwest::blocking::get;

/// Reads a file as a string.
// pub fn read_file(filename: &str) -> Result<String, Error> {
//     let mut file = File::open(filename)?;
//     let mut content = String::new();
//     file.read_to_string(&mut content)?;
//     Ok(content)
// }

/// Reads a file as binary.
pub fn read_binary_file(filename: &str) -> Result<Vec<u8>, Error> {
    let mut file = File::open(filename)?;
    let mut content = Vec::new();
    file.read_to_end(&mut content)?;
    Ok(content)
}

/// Writes a string to a file.
pub fn write_file(filename: &str, data: &str) -> Result<(), Error> {
    let mut file = OpenOptions::new().write(true).create(true).truncate(true).open(filename)?;
    file.write_all(data.as_bytes())?;
    Ok(())
}

/// Writes binary data to a file.
pub fn write_binary_file(filename: &str, data: &[u8]) -> Result<(), Error> {
    let mut file = OpenOptions::new().write(true).create(true).truncate(true).open(filename)?;
    file.write_all(data)?;
    Ok(())
}

/// Downloads a file from a URL and detects whether it's binary or text.
pub fn download_file(url: &str, filename: &str) -> Result<(), Box<dyn std::error::Error>> {
    let response = get(url)?;
    let bytes = response.bytes()?;


    let mut file = File::create(filename)?;
    file.write_all(&bytes)?;



    Ok(())
}
