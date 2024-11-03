---

# Handy SDK

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

3. **Install the SDK**:
   Run the following command to install handy-sdk along with its dependencies:
   ```bash
   pip install -e .
   ```

4. **Install Additional Requirements**:
   Ensure all dependencies in `requirements.txt` are installed:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Basic Examples

1. **Initialize and Connect to the Handy Device**:
   Start by initializing the SDK and connecting to the Handy device with your device key.
   ```python
   from handy_sdk import HandyAPI

   # Replace "YOUR_DEVICE_KEY" with the actual device key
   handy = HandyAPI("YOUR_DEVICE_KEY")
   ```

2. **Set the Handy to HAMP Mode**:
   ```python
   handy.set_hamp_mode()
   ```

3. **Control HAMP Velocity**:
   Adjust the speed of the Handy in HAMP mode. For example, set the speed to 50.
   ```python
   handy.set_hamp_velocity(velocity=50)
   ```

4. **Set the Slide Range**:
   Define the minimum and maximum range for the Handy’s slide. This example sets it from 10 to 90.
   ```python
   handy.set_hamp_slide(min_value=10, max_value=90)
   ```

5. **Start and Stop HAMP Mode**:
   To begin and end HAMP mode operations:
   ```python
   handy.start_hamp()
   # ... Perform actions while in HAMP mode ...
   handy.stop_hamp()
   ```

#### Optional: Running the FastAPI Server

The SDK includes an optional FastAPI server, allowing you to control the Handy device remotely through HTTP endpoints.

1. **Start the FastAPI Server**:
   Run the following command to start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API Endpoints**:
   With the server running, you can access the following endpoints to control the Handy:
   - **`/set_hamp_mode`**: Sets the Handy to HAMP mode.
   - **`/start_hamp`**: Starts HAMP mode.
   - **`/stop_hamp`**: Stops HAMP mode.
   - **`/set_hamp_velocity`**: Adjusts the velocity in HAMP mode (requires a `velocity` parameter).
   - **`/set_hamp_slide`**: Sets the slide range with `min_value` and `max_value` parameters.

3. **Test the API**:
   Visit `http://127.0.0.1:8000/docs` to view and test the API endpoints with an interactive Swagger UI.

### Example Script

Below is an example script demonstrating how to use **handy-sdk** to connect to the Handy, set it to HAMP mode, adjust settings, and start/stop the device.

```python
from handy_sdk import HandyAPI

# Initialize and connect to the Handy device
handy = HandyAPI("YOUR_DEVICE_KEY")

# Set Handy to HAMP mode
handy.set_hamp_mode()

# Configure speed and slide range
handy.set_hamp_velocity(velocity=60)
handy.set_hamp_slide(min_value=20, max_value=80)

# Start HAMP mode
handy.start_hamp()

# Run for a few seconds, then stop
import time
time.sleep(5)
handy.stop_hamp()
```

### License
This SDK is open-source and available under the [MIT License](LICENSE).

---
