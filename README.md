# AgriHub

AgriHub is a web application built with Flask that serves as a comprehensive platform for farmers and buyers in the agricultural sector. It includes a crop recommendation system powered by machine learning, farmer and buyer dashboards, a news API for agriculture-related news, and a market price feature for displaying current crop prices.

## Features

### Crop Recommendation System
AgriHub's crop recommendation system utilizes machine learning algorithms to analyze various factors such as soil type, climate conditions, and historical crop performance data. Based on this analysis, it provides personalized crop recommendations to farmers, aiming to optimize crop selection and maximize yield.

### Farmer Dashboard
The farmer dashboard is designed to streamline agricultural activities and facilitate communication with buyers. Key features include:
- Crop management: Farmers can monitor the progress of their crops, receive notifications for important tasks, and track growth stages.
- Communication with buyers: Farmers can connect with potential buyers, negotiate prices, and finalize transactions.
- Market analysis: Farmers can access market prices for various crops to make informed decisions about crop selection and pricing.

### Buyer Dashboard
The buyer dashboard enables buyers to connect with farmers and purchase crops at suitable prices. Features include:
- Product catalog: Buyers can browse through available crops, view detailed information, and place orders.
- Price negotiation: Buyers can negotiate prices with farmers and customize orders based on quantity and delivery preferences.
- Communication with farmers: Buyers can communicate with farmers regarding product inquiries, order status, and delivery arrangements.

### News API Integration
AgriHub integrates a news API to provide users with the latest agriculture-related news and updates. Users can stay informed about industry trends, government policies, and technological advancements, helping them make informed decisions and stay ahead in their agricultural endeavors.

### Market Price Feature
AgriHub's market price feature displays real-time market prices for various crops, allowing users to monitor price fluctuations and make data-driven decisions. Users can access current prices, historical trends, and regional variations to optimize their buying and selling strategies.

## Technologies Used
- Flask: A micro web framework for Python used for building the web application.
- Machine Learning Libraries: Libraries such as scikit-learn are employed for developing the crop recommendation system.
- News API: Integration with a third-party API for fetching agriculture-related news articles.
- HTML/CSS/JavaScript: Frontend technologies utilized for designing interactive user interfaces.
- SQLite: Database management systems for storing user data, crop information, and transaction records.

## Installation
1. Clone the repository:
   `git clone https://github.com/itsdheerajdp/agrihub.git`.
2. Install dependencies:
  `pip install -r requirements.txt`
3. Run the Flask application:
  `flask --app run run`
4. Access the application in your web browser at `http://localhost:5000`.

## Contributing
Contributions to AgriHub are welcome! If you have suggestions for new features, bug fixes, or improvements, please feel free to submit a pull request or open an issue on GitHub.

