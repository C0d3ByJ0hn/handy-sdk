## handy-sdk

### Overview
handy-sdk is a Python SDK for controlling the Handy device through its API. This SDK enables setting HAMP mode, adjusting speed, and configuring range parameters. It also includes an optional FastAPI server for remote control capabilities.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/C0d3ByJ0hn/handy-sdk.git
   ```
   
2. **Navigate to the Project Directory**:
   ```bash
   cd handy-sdk
   ```

3. **Install Dependencies**:
   Install the necessary packages listed in `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### 1. Importing the SDK and Initial Setup
   In your Python script, start by importing the necessary modules:
   ```python
   from handy_sdk import Handy
   ```

#### 2. Connecting to the Handy Device
   Initialize the SDK and connect to the Handy device:
   ```python
   handy = Handy()
   handy.connect("YOUR_DEVICE_KEY")
   ```

#### 3. Setting HAMP Mode
   To put the Handy into HAMP mode and control speed and range:
   ```python
   # Set to HAMP mode
   handy.set_hamp_mode()

   # Set speed (adjust value as needed)
   handy.set_hamp_velocity(speed=50)

   # Set slide range
   handy.set_hamp_slide(min_range=10, max_range=90)
   ```

#### 4. Starting and Stopping HAMP Mode
   ```python
   handy.start_hamp()
   # Perform actions while in HAMP mode...
   handy.stop_hamp()
   ```

### Optional: Running the FastAPI Server

1. **Start the FastAPI Server**:
   Run the FastAPI server to enable remote API access.
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Endpoints**:
   Once the server is running, use the following endpoints to control the Handy:
   - **`/set_hamp_mode`**: Set the Handy to HAMP mode.
   - **`/set_hamp_velocity`**: Adjust the speed in HAMP mode.
   - **`/set_hamp_slide`**: Configure the slide range.
   - **`/start_hamp`** and **`/stop_hamp`**: Start or stop HAMP mode.

3. **Test the API**:
   Go to `http://127.0.0.1:8000/docs` to access the API documentation and test the endpoints.

### Example Script
Here’s a quick example to bring everything together:

```python
from handy_sdk import Handy

# Initialize and connect
handy = Handy()
handy.connect("YOUR_DEVICE_KEY")

# Set up and start HAMP mode
handy.set_hamp_mode()
handy.set_hamp_velocity(60)
handy.set_hamp_slide(20, 80)
handy.start_hamp()

# Stop HAMP mode after a duration
import time
time.sleep(5)
handy.stop_hamp()
```

### License
This SDK is open-source and available under the [MIT License](LICENSE).

---

Met deze instructies kunnen gebruikers de SDK eenvoudig installeren, configureren en gebruiken voor verschillende toepassingen met de Handy.
