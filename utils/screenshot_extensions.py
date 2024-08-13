from datetime import datetime
import os
import time


class ScreenShotExtensions():
    @staticmethod
    def take_standard_screenshot(driver, file_name):
        # Get the current date and time
        current_time = datetime.now()

        # Format the date and time in a string format suitable for folder names
        # Example: '2024-08-13_14-30-00'
        folder_name = current_time.strftime("%Y-%m-%d_%H-%M-%S")

        # Define the path for the "screenshot" folder
        parent_dir = os.path.join(os.getcwd(), "screenshot")

        # Ensure the "screenshot" directory exists
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        # Create the current datetime folder inside the "screenshot" folder
        path = os.path.join(parent_dir, folder_name)
        os.makedirs(path)

        # Step 4: Take a screenshot and save it to the folder
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_path = os.path.join(path, f'{file_name}_{timestamp}.png')
        driver.save_screenshot(screenshot_path)
