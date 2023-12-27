# Password Generator 

## Video Demo

[![Watch the video](https://img.youtube.com/vi/YOUR_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

## Description

This Python project provides a simple yet powerful password generator and manager. The program allows users to generate random passwords, create custom passwords based on input text, and check the strength of passwords. Additionally, it generates a password card in PDF format for easy reference.

## Features

1. **Generate Random Passwords**: The program can generate strong, random passwords with a specified length.

2. **Generate Custom Passwords**: Users can create custom passwords based on provided text. The program intelligently combines user input with random characters for enhanced security.

3. **Check Password Strength**: Users can check the strength of a password based on various criteria, such as the presence of lowercase and uppercase letters, numbers, symbols, and length.

4. **Password Card Generation**: The program creates a visually appealing password card in PDF format. The card includes the user's name, generated password, and the associated platform. Platform logos (e.g., Facebook, LinkedIn, Instagram) are included for easy identification.

## Usage

1. **Generate Random Passwords**:
   - Select option 1.
   - Enter your name and the platform for which you need a password.
   - A PDF password card containing the generated password will be created.

2. **Generate Custom Passwords**:
   - Select option 2.
   - Enter the text for the custom password.
   - Provide your name and the platform.
   - A PDF password card with the custom password will be generated.

3. **Check Password Strength**:
   - Select option 3.
   - Enter the password you want to assess.
   - The program will evaluate the strength and provide a rating out of 10.

## Dependencies

- [FPDF](https://pypi.org/project/fpdf/): A Python library for creating PDFs.
- [string](https://docs.python.org/3/library/string.html): A module providing common string operations.
- [random](https://docs.python.org/3/library/random.html): A module for generating pseudo-random numbers.
- [re](https://docs.python.org/3/library/re.html): A module for regular expression operations.

## Setup

To run the program, make sure to install the required dependencies:

```bash
pip install fpdf
```

Ensure that the background images (`background.png`, `blue_key.jpg`, `facebook_logo.png`, `linkedin_logo.png`, `instagram_logo.jpg`) are placed in the specified directories

## Acknowledgments

This project is inspired by the need for secure and easy-to-remember passwords. Special thanks to the developers of FPDF for the PDF generation functionality.