# TripMind - Hotel Recommendation System

A machine learning-powered system to provide personalized hotel recommendations based on user reviews and metadata.

## 📋 Project Overview
Trip Mind is an Intelligent Decision Support System built by our 5-member team to create a hotel recommendation application using machine learning techniques. This initial setup establishes the complete development foundation for collaborative work.

### 🎯 Primary Objective
This merge provides a standardized, production-ready project structure that enables all team members - including those new to software development - to immediately clone and contribute to the project without setup hurdles.

This project demonstrates:
- **End-to-end ML Engineering:** From data ingestion to model deployment.
- **Software Development Best Practices:** Version control, CI/CD, testing, and code quality.
- **Modern ML Tools:** Extensive use of the Python data science ecosystem.
- **Ethical AI Considerations:** Addressing bias, fairness, and privacy in recommendations.

## Dataset

### Acknowledgements
The data was scraped from Booking.com. All data in the file is publicly available to everyone already. Please be noted that data is originally owned by Booking.com.

### Data Context
This dataset contains 515,000 customer reviews and scoring of 1493 luxury hotels across Europe. Meanwhile, the geographical location of hotels are also provided for further analysis.

### Data Content
The csv file contains 17 fields. The description of each field is as below:

- Hotel_Address: Address of hotel.
- Review_Date: Date when reviewer posted the corresponding review.
- Average_Score: Average Score of the hotel, calculated based on the latest comment in the last year.
- Hotel_Name: Name of Hotel
- Reviewer_Nationality: Nationality of Reviewer
- Negative_Review: Negative Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Negative'
- Review_Total_Negative_Word_Counts: Total number of words in the negative review.
- Positive_Review: Positive Review the reviewer gave to the hotel. If the reviewer does not give the negative review, then it should be: 'No Positive'
- Review_Total_Positive_Word_Counts: Total number of words in the positive review.
- Reviewer_Score: Score the reviewer has given to the hotel, based on his/her experience
- Total_Number_of_Reviews_Reviewer_Has_Given: Number of Reviews the reviewers has given in the past.
- Total_Number_of_Reviews: Total number of valid reviews the hotel has.
- Tags: Tags reviewer gave the hotel.
- days_since_review: Duration between the review date and scrape date.
- Additional_Number_of_Scoring: There are also some guests who just made a scoring on the service rather than a review. This number indicates how many - - valid scores without review in there.
- lat: Latitude of the hotel
- lng: longtitude of the hotel

### 🏗️ Complete Project Structure Established

TRIP_MIND/
├── .github/workflows/           # CI/CD Automation
│   └── test.yml                 # Automated testing pipeline
├── config/
│   └── .pre-commit-config.yaml  # Code quality hooks
├── dataset/                     # Organized data management
│   ├── external/                # Third-party datasets
│   ├── processed_dataset/       # Cleaned & transformed data
│   └── raw_dataset/            # Original source data
├── docs/                        # Comprehensive documentation
│   ├── support_documents/
│   │   ├── images/             # Visual assets
│   │   └── approvals_and_requests/ # Project approvals
│   ├── ETHICS.md               # Ethical guidelines
│   └── LEGAL.md                # Legal considerations
├── models/                      # Trained ML models storage
├── notebooks/                   # Research & experimentation
│   ├── primary/                # Main EDA notebooks
│   │   ├── eda_01.ipynb
│   │   └── eda_02.ipynb
│   ├── secondary/              # Supplementary analysis
│   └── tertiary_eda/           # Advanced exploration
├── src/                        # Production code
│   ├── data_processing/
│   │   └── data_preprocessing.py  # Data loading & cleaning
│   ├── eda/
│   │   └── eda_util.py           # EDA helper functions
│   ├── features/               # Feature engineering
│   ├── models/                 # ML model implementations
│   ├── visualization/          # Plotting & charts
│   └── __init__.py
├── tests/                      # Test suite
├── tm_env/                     # Virtual environment
├── .env                        # Environment variables
├── .gitignore                  # Git exclusion rules
├── LICENSE                     # Project license
├── pyproject.toml             # Project configuration
├── README.md                   # Project documentation
└── requirements.txt           # Dependencies

## Getting Started

1.  Clone the repo: `git clone https://github.com/pius-alhassan/trip_mind.git`
2.  Create a virtual environment: `python -m venv venv`
3.  Activate it: `source venv/bin/activate` (or `.\venv\Scripts\activate` on Windows)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Run the EDA notebook: `jupyter notebook notebooks/01_eda.ipynb`

## Branching Strategy

- `main`: Production-ready code.
- `iteration`: Integration branch for reviewed features.
- `feature/*`: Individual feature branches. Create a PR to `iteration` when ready.
