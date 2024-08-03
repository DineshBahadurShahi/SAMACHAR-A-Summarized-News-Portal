<div style="text-align:center;">
  <img src="/InNews-master/Meta/samachar.jpg" alt="screenshot" style="width:300px;height:auto;">
</div>


## SAMACHAR: A Summarized News 📰 Portal
A Streamlit-based web application that offers summarized news from various sources. Users can access trending news, search by custom topics, or explore news in specific categories. This project uses RSS feeds from Google News and the Newspaper3k library to provide concise summaries and relevant images for each news article.


## Features

- **Trending News**: Displays the latest trending news from Google News.
- **Search by Topic**: Allows users to search for news articles based on custom topics.
- **Category News**: Browse news in predefined categories such as World, Business, Technology, Entertainment, Sports, Science, and Health.
- **Summarized Articles**: Provides concise summaries of news articles with the ability to read more.
- **Image Support**: Displays images associated with news articles.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/DineshBahadurShahi/News-Summerizer-Portal.git
   cd News-Summerizer-Portal

2. **Set up a virtual environment**:
```sh
    python -m venv venv 
```
3. **Activate the virtual environment**:
```sh
    venv\Scripts\activate
```
4.  **Install the required packages**:
```sh
    pip install -r requirements.txt
``` 
5.  **Download NLTK resources**:
```sh
    python -m nltk.downloader punkt
```


## Project Structure
```
SAMACHAR/
│
├── App.py                       # Main application file
├── sample_news_scrap.py         # Sample news scraping script
├── requirements.txt             # Required Python packages
├── Meta/                        # Directory containing image assets
│   ├── newspaper.ico
│   ├── samachar11.png
│   ├── no_image.jpg
│   ├── default_image.png
│   └── screenshot.jpg           # Screenshot of the application
└── README.md                    # Project documentation
```

## Screenshots
<img src="/InNews-master/Meta/screenshot.jpg" alt="screenshot" style="max-width:100%;height:auto;">



## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact
For any inquiries, please contact Dinesh Bahadur Shahi at [imdineshbdr@gmail.com](mailto:imdineshbdr@gmail.com).







