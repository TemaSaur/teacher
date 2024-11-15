FROM python:3.12-alpine

# RUN curl -sSL https://install.python-poetry.org | python3 -

WORKDIR /app

# Copy the pyproject.toml file to the working directory
COPY pyproject.toml .

# Install the dependencies using Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-dev

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port the application will run on
EXPOSE 8000

# Run the command to start the application when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

