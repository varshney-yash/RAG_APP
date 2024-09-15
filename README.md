## Setup

1. Build the docker image
   ```
   docker build -t ragapp .
   ```

2. Run the docker image with appropriate environment variables:
   - PINECONE_API_KEY
   - PINECONE_INDEX_NAME
   - GOOGLE_API_KEY
    ```
   docker run -e PINECONE_API_KEY='' -e PINECONE_INDEX_NAME='' -e GOOGLE_API_KEY='' -p 8000:8000 ragapp
   ```

3. Head on over to localhost:8000/docs to test the API endpoints

## Endpoints

- POST /upload: Upload and process PDF documents and store in pinecone vector database
- POST /similarity: Perform similarity search on processed documents
- POST /summarize: Summarize given text using Gemini model

## Project Structure

The project follows a modular structure with separate files for configuration, dependencies, models, services, and API endpoints. This structure allows for easy maintenance and scalability.