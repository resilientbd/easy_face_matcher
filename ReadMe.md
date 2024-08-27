# Easy Face Matcher

Easy Face Matcher is a Python-based face recognition application that uses FastAPI for the backend. It provides endpoints for comparing faces from images, detecting face parameters, and calculating similarity percentages based on key facial features.

## Features

- **Face Comparison**: Compare faces from two images and get a similarity percentage.
- **Face Landmark Detection**: Detect and analyze facial landmarks for a more detailed comparison.
- **API Endpoints**: Use FastAPI to expose functionality for face comparison.

## Requirements

- Python 3.9+
- Docker
- Docker Compose

## Installation

### Using Docker

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/easy_face_matcher.git
   cd easy_face_matcher
2. **Build the Docker Image**:
   ```sh
   docker-compose build
3. **Run the Application**:
   ```sh
   docker-compose up
   
### Without Docker

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/easy_face_matcher.git
   cd easy_face_matcher
2. **Create a Virtual Enviorenment**:
   ```sh
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies:**:
   ```sh
   pip install -r requirements.txt
4. **Run the Application:**:
   ```sh
   uvicorn app.main:app --host 0.0.0.0 --port 5003
The application will be accessible at http://localhost:5003.

## API Endpoints

- Endpoint: `/compare_faces`
- Method: `POST`
- Description: Compare two images and get a similarity percentage.
- Request Body:
   ```sh
   {
  "image1": "<base64 encoded image data>",
  "image2": "<base64 encoded image data>"
   }
- Response:
  ```sh
  {
  "similarity_percentage": 95.32
  }
  
## Contribution Guidelines
- Fork the Repository: Fork the repository to your own GitHub account.
- Create a New Branch:
  ```sh
  git checkout -b feature/your-feature-name
- Make Your Changes: Implement your feature or fix a bug.
- Commit Your Changes:
  ```sh
  git add .
  git commit -m "Add a meaningful commit message"
  
- Push to Your Fork:
  ```sh
  git push origin feature/your-feature-name
  
- Create a Pull Request: Open a pull request from your forked repository to the main repository.

## Contact
For any questions or feedback, please contact `faisal.hossain.pk@gmail.com`





