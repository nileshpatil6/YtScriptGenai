# YouTube Idea Generator for AI/ML Content

The **YouTube Idea Generator** is a web application designed to help content creators in the AI/ML niche generate detailed and well-formatted YouTube video scripts quickly. Leveraging the power of the Gemini 2.0 Flash API for text generation, this project offers an engaging, modern UI with glassmorphism aesthetics, smooth animations, and full markdown rendering for scripts.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

The YouTube Idea Generator allows you to:
- **Select a Predefined Topic:** Choose from a curated list of popular AI/ML topics.
- **Use Custom Prompts:** Enter your own prompt for script generation.
- **Render Markdown:** The API responses are in markdown, which is rendered beautifully for readability.
- **Copy Scripts Easily:** A dedicated copy button lets you quickly copy the generated script for further use.

The application features a responsive, modern UI with a glassmorphic design and smooth animations, ensuring an excellent user experience across devices.

---

## Features

- **Predefined Topic Selection:** Instantly generate a script by clicking on a topic card.
- **Custom Prompt Input:** Enter your own ideas or prompts to generate tailored scripts.
- **Markdown Formatting:** Properly formatted output with headings, bold text, lists, code blocks, and more.
- **Responsive & Modern UI:** Uses glassmorphism styling with smooth animations.
- **Preloader Spinner:** Indicates processing while waiting for the script generation.
- **Horizontally Scrollable Output:** Handles wide content such as code blocks without breaking the layout.
- **Copy-to-Clipboard Functionality:** Easily copy the generated script with a single click.

---

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Text Generation:** Gemini 2.0 Flash API
- **Markdown Parsing:** [marked.js](https://marked.js.org/)
- **Design:** Glassmorphism, responsive design, modern animations

---

## Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/youtube-idea-generator.git
   cd youtube-idea-generator